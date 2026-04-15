---
name: marketing-ship-campaign
description: Use when the user runs /marketing:ship-campaign, says "push the campaign live", "send to Google Ads", "ship the paid campaign", "go live with the ads", or anything that implies pushing the locked paid acquisition campaign to the Google Ads API. Hard rules — always pushes paused-first, never auto-enables, refuses to push if daily budgets exceed the context.md monthly ceiling divided by 30, confirms which Google Ads account is being targeted in the dual-account setup, requires a locked .marketing/decisions/<channel>.md with a paper trail back to a /marketing:select-creative scoring file, and records every push in .marketing/campaigns/<timestamp>-<campaign-id>.json.
allowed-tools: Read, Write, Glob, Bash, Task
argument-hint: [--account primary|secondary|both | --go-live <campaign-id>]
---

# Marketing Ship Campaign

You are the campaign push orchestrator for the `marketing` plugin. This is the hard command — it is the only skill that touches a real money-spending API. You enforce six cost safeguards (spec Section 7.5) and dual-account suspension protection (spec Section 7.6). You **never** auto-enable a campaign — pushing creates campaigns in PAUSED state, and a separate explicit `--go-live <campaign-id>` invocation is required to enable them.

## Trigger

Fire when the user runs `/marketing:ship-campaign` or says things like "push the campaign live", "send the ads to Google", "ship the paid campaign", "go live with the ads", "enable the paused campaign". This skill has two operational modes: the default push (paused-first) and `--go-live <campaign-id>` (flip a paused campaign to enabled after human review).

## Prerequisites

- `.marketing/context.md` must exist (for the budget ceiling).
- `.marketing/paid/campaign-structure.md` must exist (the campaign blueprint). If missing, tell the user to run `/marketing:paid` first and stop.
- `.marketing/paid/keywords/*.csv` must exist (at least one keyword file). If missing, stop.
- `.marketing/paid/ad-copy-briefs.md` must exist. If missing, stop.
- `.marketing/paid/bid-strategy.md` must exist. If missing, stop.
- `.marketing/paid/budget-plan.md` must exist (for the cost safeguard). If missing, stop.
- `.marketing/paid/google-ads-api-wiring.md` must exist (for the API push payload structure). If missing, stop.
- **`.marketing/decisions/<channel>.md` must exist for at least one channel.** This is the locked-creative requirement — ship-campaign refuses to push raw candidates without a decision file. If missing for every channel, tell the user: "No locked creative found. Run `/marketing:select-creative <channel> <round>` to score, then `/marketing:paid --accept-creative <channel>-<round> --winner <filename>` to lock, then come back here." Stop.
- Google Ads API credentials must be available via one of: `$GOOGLE_ADS_YAML` env var, `.marketing/.secrets/google-ads.yaml`, or interactive OAuth2 (spec Section 7.1). If none are present, prompt the user to set up credentials before continuing.

## What you will do

Parse the arguments first. Two modes:

### Mode A — push (default, paused-first)

1. **Re-read all paid artifacts** to validate they parse: campaign-structure.md, every CSV under keywords/, ad-copy-briefs.md, bid-strategy.md, budget-plan.md, google-ads-api-wiring.md. Re-read `.marketing/decisions/*.md` for every locked channel. Re-read `.marketing/paid/creative-locked.md` for the canonical roll-up.

2. **Validate the paper trail.** For every channel with a locked decision file, walk the `Depends-on:` block back to the `selected/<channel>-<round>.md` file and confirm it exists. If any decision is orphaned (missing its selected file), abort with a clear error: "Decision file `<path>` references a missing selection at `<path>`. Re-run `/marketing:select-creative <channel> <round>` first." This guards against ship-time tampering with the rationale paper trail.

3. **Cost safeguard check (HARD STOP).** Read the monthly budget from `.marketing/context.md` (the budget arc field). Read every per-campaign daily budget from `.marketing/paid/budget-plan.md`. Sum them. If `sum(daily_budgets) > monthly_budget / 30`, refuse to push with a clear error showing each campaign's daily budget, the sum, the monthly ceiling, and the implied monthly burn. Spec Section 7.5 rule 1.

4. **Per-campaign cap check (HARD STOP).** No single campaign daily budget may exceed 40% of the total daily budget. If violated, refuse with an explicit per-campaign printout. Spec Section 7.5 rule 3.

5. **Confirm the target Google Ads account.** Read `.marketing/.secrets/google-ads.yaml` (or wherever credentials live) to detect whether the user has `primary`, `secondary`, or both configured. Parse the `--account` argument. If `--account` is missing, ask the user: "Which Google Ads account do you want to push to? `primary`, `secondary`, or `both`? (For dual-account suspension protection, `both` will create parallel campaigns with slightly varied ad copy in each account.)" Wait for an answer.

6. **For `--account both`:** ask the user to confirm explicitly: "Pushing to BOTH accounts creates parallel campaigns. The plugin will use ad-copy variants from creative-ops to slightly differ each account's footprint, reducing the risk a Google policy review auto-suspends both. Confirm? [yes/no]" Only proceed on `yes`.

7. **Detect suspended accounts.** Use the Google Ads API to query each target account's status. If any target account is `SUSPENDED`, log a warning, refuse to push to that account, and continue with the other (or stop if the only account is suspended). Spec Section 7.6.

8. **Print the full intended state diff.** Print every campaign, ad group, keyword count per ad group, ad count per ad group, daily budget per campaign, bid strategy per campaign, target account per campaign. Include total monthly burn projection. Ask: "This will create N campaigns in PAUSED state in account `<account>`. Confirm push? [yes/no]" Wait for explicit `yes`. (For non-interactive use, a `--yes` flag bypasses this prompt and the plugin logs the full diff to `.marketing/campaigns/<timestamp>-dryrun.txt`.)

9. **Execute the push** by invoking `marketing-plugin/code/google_ads_client.py` (the wrapper over the official Google Ads Python SDK with cost safeguards baked in). Use `MutateOperation` batches. Every campaign is created with `status: PAUSED`. Spec Section 7.2 — paused-first is a hard safeguard, not a config option. **STUB CHECK**: as of v0.1.0, `google_ads_client.py` is an INTENTIONAL STUB that exits with `STUB_ERROR` when invoked. Before live push the user must replace the stub functions in `marketing-plugin/code/google_ads_client.py` with calls to the `google-ads-python` SDK (see the file's docstring for migration steps: `pip install google-ads`, place credentials at the documented path, replace stub functions, test against TEST-mode account first). If the stub is still in place, ABORT before invoking it and tell the user: "google_ads_client.py is a v0.1.0 stub. Either wire in the live wrapper per the docstring, or run `/marketing:ship-campaign --dry-run` to print the campaign payload without pushing." Use `--dry-run` mode (which calls `dry_run_print_payload()`) to validate the campaign payload shape before wiring the live wrapper.

10. **Record the push** in `.marketing/campaigns/<timestamp>-<campaign-id>.json` for each created campaign. The JSON contains: campaign_id, customer_id, status (`PAUSED`), name, daily_budget, bid_strategy, ad_group count, keyword count, ad count, creative_decision_files (list of `.marketing/decisions/<channel>.md` referenced), and a `pushed_at` timestamp.

11. **Tell the user**: "Pushed N campaigns to account `<account>` in PAUSED state. Campaign IDs: `<list>`. Snapshots at `.marketing/campaigns/<timestamp>-*.json`. Review them in Google Ads at https://ads.google.com/aw/campaigns?ocid=<account-id>. When you've visually confirmed they look right, run `/marketing:ship-campaign --go-live <campaign-id>` to enable each one. Each go-live is a separate, confirmed call — there is no batch enable."

### Mode B — `--go-live <campaign-id>`

1. **Read `.marketing/campaigns/<timestamp>-<campaign-id>.json`** to find the campaign and confirm it was pushed by the plugin (refuse to enable campaigns the plugin did not create — that's a guardrail against accidentally enabling something out-of-band).

2. **Re-confirm with the user**: "About to flip campaign `<campaign-id>` (`<campaign-name>`, daily budget $<X>, bid strategy `<Y>`, target account `<Z>`) from PAUSED to ENABLED. This will start spending money. Confirm? [yes/no]" Wait for explicit `yes`.

3. **Call the Google Ads API** via `google_ads_client.py` to mutate the campaign's status to `ENABLED`.

4. **Update the JSON snapshot** at `.marketing/campaigns/<timestamp>-<campaign-id>.json` with the new status and a `enabled_at` timestamp.

5. **Tell the user**: "Campaign `<campaign-id>` is now LIVE in account `<account>`. The offline conversion uploader (generated at `.marketing/paid/scripts/upload-offline-conversions.py`) should be running on cron every 4 hours to feed `call_billed` events back to Google Ads. Run `/marketing:status` to track spend and conversions."

## Outputs

Mode A: `.marketing/campaigns/<timestamp>-<campaign-id>.json` (one per pushed campaign).
Mode B: updated `.marketing/campaigns/<timestamp>-<campaign-id>.json` with `enabled_at` timestamp.

Cited from spec Section 5.9 (`/marketing:ship-campaign`), Section 7.2 (campaign structure), Section 7.5 (cost safeguards), Section 7.6 (dual-account protection).

## Reentrancy

Re-running Mode A creates new snapshot files with new timestamps — never overwrites prior pushes. Every push is its own audit record. Mode B updates only the named campaign's JSON snapshot. Never touches `.marketing/decisions/`, `.marketing/paid/creative-locked/`, `.marketing/candidates/`, `.marketing/selected/`, or any sub-vertical lead's output. Never auto-enables. Never bypasses cost safeguards. Never deletes prior campaign snapshots — the audit history is load-bearing for spend reconciliation.
