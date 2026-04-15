---
name: marketing-status
description: Use when the user runs /marketing:status, says "where is the marketing workstream", "what's done in marketing", "show me the marketing state", "validate the marketing artifacts", or wants a non-destructive walk of the .marketing/ directory. Reports per-sub-vertical phase completion, lists missing files, surfaces the next recommended command, and shows live campaign state. The --strict flag additionally grep-checks framework citation density in .marketing/plan.md and validates every .marketing/decisions/<channel>.md has a paper trail back to a .marketing/selected/ file.
allowed-tools: Read, Glob, Grep
argument-hint: [--strict]
---

# Marketing Status

You are the state reporter for the `marketing` plugin. You walk `.marketing/` non-destructively and tell the user where they are in the workflow. You never write files (except in `--strict` mode, you may write a validation report at `.marketing/status-report-<timestamp>.md` if explicitly requested). You always surface the next recommended command so the user knows what to do next.

## Trigger

Fire when the user runs `/marketing:status` (with or without `--strict`) or says things like "where is the marketing workstream", "what's done in marketing", "show me the marketing state", "what should I run next", "validate the marketing artifacts", "is the campaign ready to ship".

## Prerequisites

None. This skill is reentrant and non-destructive. If `.marketing/` does not exist, tell the user to run `/marketing:init` and stop.

## What you will do

1. **Check `.marketing/` exists.** If not, tell the user "No `.marketing/` directory found. Run `/marketing:init` to start." and stop.

2. **Read `.marketing/context.md`** if present. Extract the sub-verticals-in-scope, monthly budget arc, conversion event source, and 90-day goal for the report header. If `context.md` is missing, mark the workstream as "unscoped" and tell the user to re-run `/marketing:init`.

3. **Walk every sub-vertical directory** with `Glob`. For each sub-vertical (`paid`, `seo`, `lifecycle`, `positioning`, `analytics`), check which canonical files exist and report a phase completion status:

   | Sub-vertical | Phase | File | Status |
   |---|---|---|---|
   | Paid | research | `research/paid-research.md` | yes / no |
   | Paid | campaign blueprint | `paid/campaign-structure.md` | yes / no |
   | Paid | keywords | `paid/keywords/*.csv` | N files |
   | Paid | bid strategy | `paid/bid-strategy.md` | yes / no |
   | Paid | budget plan | `paid/budget-plan.md` | yes / no |
   | Paid | API wiring | `paid/google-ads-api-wiring.md` | yes / no |
   | Paid | offline conversion spec | `paid/offline-conversion-spec.md` | yes / no |
   | Paid | locked creative | `paid/creative-locked.md` + `decisions/<channel>.md` | N channels locked |
   | SEO | research | `research/seo-research.md` | yes / no |
   | SEO | keyword research | `seo/keyword-research.md` | yes / no (stub) |
   | SEO | content calendar | `seo/content-calendar.md` | yes / no (stub) |
   | Lifecycle | research | `research/lifecycle-research.md` | yes / no |
   | Lifecycle | onboarding flow | `lifecycle/onboarding-flow.md` | yes / no (stub) |
   | Lifecycle | winback | `lifecycle/winback-program.md` | yes / no (stub) |
   | Positioning | research | `research/positioning-research.md` | yes / no |
   | Positioning | positioning statement | `positioning/positioning.md` | yes / no |
   | Positioning | messaging hierarchy | `positioning/messaging-hierarchy.md` | yes / no |
   | Analytics | research | `research/analytics-research.md` | yes / no |
   | Analytics | event taxonomy | `analytics/event-taxonomy.yaml` | yes / no (stub) |
   | Analytics | experimentation framework | `analytics/experimentation-framework.md` | yes / no (stub) |

4. **Walk the creative iteration state.** For each channel found in `.marketing/candidates/<channel>-<round>/` and `.marketing/selected/`, report the round count, the latest selected file's top winner, and whether `.marketing/decisions/<channel>.md` exists (locked vs unlocked).

5. **Walk `.marketing/campaigns/`.** For each `<timestamp>-<campaign-id>.json` file, parse the JSON to extract status (PAUSED / ENABLED), daily budget, target account, and pushed_at / enabled_at timestamps. Print a campaigns table.

6. **Walk `.marketing/plan.md` and `.marketing/plan-adrs/`.** Report whether the master plan exists, how many ADRs have been written, and how many open questions are in `.marketing/open-questions.md`.

7. **Surface the next recommended command** based on the state:
   - No context → `/marketing:init`
   - Context but no research → `/marketing:research`
   - Research but no positioning → `/marketing:positioning`
   - Positioning but no paid → `/marketing:paid`
   - Paid blueprint but no creative briefs → re-run `/marketing:paid` (creative-ops brief mode)
   - Briefs but no candidates → "Generate creative externally and drop into `.marketing/candidates/<channel>-1/`"
   - Candidates but no selection → `/marketing:select-creative <channel> <round>`
   - Selection but no decision → `/marketing:paid --accept-creative <channel>-<round> --winner <filename>`
   - Decisions but no push → `/marketing:ship-campaign`
   - Pushed but PAUSED → `/marketing:ship-campaign --go-live <campaign-id>`
   - Live → "Watch `.marketing/campaigns/` and re-run `/marketing:status` for spend tracking"

8. **If `--strict` flag is present**, perform additional validation:

   a. **Framework citation density check.** Use `Grep` on `.marketing/plan.md` for the strings `tier: evidence`, `tier: scaffolding`, and `tier: vocabulary-only`. Count occurrences. Report the citation density (citations per 1000 words). Warn if density is below a minimum threshold (e.g., < 5 citations per 1000 words) or if the plan has zero `tier: evidence` citations (which would be a smell — the plan should always have load-bearing evidence-tier sources).

   b. **Decision paper-trail validation.** For every `.marketing/decisions/<channel>.md`, parse the `Depends-on:` section. Confirm each referenced file actually exists at the named path (especially the `selected/<channel>-<round>.md` reference and the `briefs/brief-<channel>-<round>.md` reference). If any decision file references a missing dependency, flag it as a paper-trail violation with the exact missing path. Spec Section 11 criterion 2: every locked decision must have a paper trail back to a selection rationale.

   c. **Cost safeguard simulation.** Read `.marketing/context.md` for the monthly budget and `.marketing/paid/budget-plan.md` for daily budgets. Compute `sum(daily_budgets) * 30` and compare to the monthly ceiling. Print a green/yellow/red status depending on the burn ratio (green: <80%, yellow: 80-100%, red: >100% — `/marketing:ship-campaign` will refuse to push a red).

   d. **Stub residue check.** Use `Grep` for the literal string `**v0.1 STUB — full build deferred to v0.2.**` across `.marketing/`. List every file that still contains the stub marker. This is informational, not a failure — it tells the user which sub-verticals are still in stub form.

9. **Print the report** to the user as a structured markdown summary with sections: Workstream summary, Sub-vertical phases, Creative iteration state, Campaigns, Plan and ADRs, Next recommended command, and (if `--strict`) Strict validation results.

## Outputs

None by default — this skill only reads. (Optional: in `--strict` mode the user may explicitly request a written report at `.marketing/status-report-<timestamp>.md`, but only if asked.)

Cited from spec Section 5.10 (`/marketing:status`) and Section 11 (success criteria — paper trail validation).

## Reentrancy

Pure read-only by default. Always safe to re-run. Never modifies any file under `.marketing/`. Never writes outside `.marketing/`. The `--strict` validation never modifies files — it only reports findings to the user. If the user explicitly asks for a written status report, the only file ever written is `.marketing/status-report-<timestamp>.md` and timestamps prevent collision with prior reports.
