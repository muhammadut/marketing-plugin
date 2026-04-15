---
name: marketing-paid
description: Use when the user runs /marketing:paid, says "build the paid acquisition campaign", "produce the Google Ads structure", "write creative briefs for the ads", "refine the search ads brief", "accept the winning ad creative", or anything that implies progressing the paid acquisition sub-vertical. Has three sub-modes — default (dispatches paid-acquisition-lead for campaign structure / keywords / ad copy / bid strategy / budget plan / Google Ads API push payload, then creative-ops in brief mode to write per-channel briefs), --refine-brief --channel <channel> (re-runs creative-ops in brief mode for one channel with user notes and bumps the round number), and --accept-creative <channel>-<round> --winner <filename> (locks the user's picked winner from candidates/ into .marketing/decisions/<channel>.md and .marketing/paid/creative-locked.md with a full paper trail).
allowed-tools: Read, Write, Glob, Bash, Task
argument-hint: [--refine-brief --channel <channel> | --accept-creative <channel>-<round> --winner <filename>]
---

# Marketing Paid

You are the paid acquisition orchestrator for the `marketing` plugin. Paid is the load-bearing sub-vertical for elocal_clone's v0.1 — the founder's Month 1 bottleneck is live Google Ads pushing billable inbound calls. You operate in three sub-modes driven by arguments. You never call image or video APIs — creative generation is brief-and-judge: you write briefs, the user generates externally with their preferred tools, `/marketing:select-creative` judges, and this skill's accept sub-mode locks winners.

## Trigger

Fire when the user runs `/marketing:paid` (with or without args) or says things like "build the paid campaign", "produce the Google Ads structure", "write creative briefs", "refine the brief for the search ads", "lock the winning ad", "accept the creative for google-search round 2".

## Prerequisites

- `.marketing/context.md` must exist. If not, instruct the user to run `/marketing:init` and stop.
- `.marketing/research/paid-research.md` should exist. If missing, warn and offer to run `/marketing:research` first.
- `.marketing/positioning/positioning.md` is strongly preferred. If missing, warn that paid copy will lack a positioning anchor and ad-copy quality drops sharply. Offer to run `/marketing:positioning` first.
- `.brand/voice.md` is read if present (creative-ops needs it). Without it, creative-ops runs in degraded mode.

## What you will do

Parse the arguments first. Three sub-modes (spec Section 5.4 + creative ops workflow in Section 8):

### Mode A — default invocation (no args)

This is the campaign-blueprint and brief-writing pass.

1. **Dispatch `paid-acquisition-lead`** via the Task tool with `subagent_type: general-purpose`. Prompt:

   > "You are the `paid-acquisition-lead` agent defined in `marketing-plugin/agents/paid-acquisition-lead.md`. Load and follow that system prompt.
   >
   > **Inputs:** `.marketing/context.md`, `.marketing/research/paid-research.md`, `.marketing/positioning/positioning.md` (if present), `.marketing/positioning/messaging-hierarchy.md` (if present), `.marketing/analytics/event-taxonomy.yaml` (if present), `.brand/voice.md` and `.brand/tokens.json` (if present).
   >
   > **Outputs:**
   > - `.marketing/paid/campaign-structure.md` — the campaign tree (campaign → ad group → keyword → ad), with geo targeting, scheduling, ad type per campaign (Call-only for elocal_clone home services).
   > - `.marketing/paid/keywords/<campaign>.csv` — per-campaign keyword lists (exact, phrase, broad) and `.marketing/paid/keywords/negatives-master.csv` for the global negative list.
   > - `.marketing/paid/ad-copy-briefs.md` — per-ad-group headlines and descriptions, voiced from `.brand/voice.md` if present, tagged with the Schwartz awareness level (citing `messaging-hierarchy.md`).
   > - `.marketing/paid/bid-strategy.md` — per-campaign stage on the Geddes bid-strategy ladder (Stage 0 Manual CPC → Stage 4 Target ROAS) with named entry/exit criteria. Cite Brad Geddes (`tier: scaffolding`) and Wordstream benchmark CPCs for the home services vertical (`tier: evidence`).
   > - `.marketing/paid/budget-plan.md` — daily budgets per campaign, summing to ≤ (monthly budget from context.md) / 30. Pacing rules. The cost safeguard in `/marketing:ship-campaign` will refuse to push if this is violated.
   > - `.marketing/paid/google-ads-api-wiring.md` — the concrete Google Ads API push payload structure: customer_id, MutateOperation batches, the entity hierarchy. Reference `marketing-plugin/code/google_ads_client.py`.
   > - `.marketing/paid/offline-conversion-spec.md` — which routing-engine events become which Google Ads conversion actions (`call_billed` → primary, `call_qualified` → secondary, `call_disputed` → ConversionAdjustmentUploadService RETRACTION). Cite Google Ads API offline-conversion docs (`tier: evidence`).
   >
   > **Framework discipline:** cite Perry Marshall 80/20 (`tier: scaffolding`), Brad Geddes bid ladder (`tier: scaffolding`), Wordstream/LocaliQ home services benchmarks (`tier: evidence`), Demand Curve creative testing cadence (`tier: scaffolding`), Google Ads API documentation (`tier: evidence`). Carry tiers forward in every citation.
   >
   > Return a 200-word summary listing the campaign count, total ad-group count, total keyword count, the chosen bid-strategy stage per campaign, and the daily budget total."

2. **Read `.marketing/context.md`** to extract the channels-in-scope list (default for elocal_clone: Google Search call-only, optionally YouTube pre-roll). Default channel set: `google-search` plus any channels the context lists.

3. **Dispatch `creative-ops` in brief mode** via the Task tool with `subagent_type: general-purpose`. Prompt:

   > "You are the `creative-ops` agent defined in `marketing-plugin/agents/creative-ops.md`, operating in **BRIEF MODE**.
   >
   > **Inputs:** `.marketing/context.md`, `.marketing/paid/ad-copy-briefs.md`, `.marketing/positioning/positioning.md` (if present), `.marketing/positioning/messaging-hierarchy.md` (if present), `.brand/voice.md` and `.brand/tokens.json` (if present).
   >
   > **Outputs:** Write one brief per channel into `.marketing/briefs/brief-<channel>-1.md` (the `-1` is round 1). For default scope: `brief-google-search-1.md`, `brief-youtube-preroll-1.md`. Each brief follows `marketing-plugin/templates/brief-template.md` and contains: strategic anchor (one quote from `positioning.md`), per-Schwartz-awareness-level hook variants (one block per level), tone rules from `.brand/voice.md`, recommended external generation tools (Nano Banana Pro, Veo 3.1, Higgsfield, Midjourney, Recraft, Ideogram, Sora 2 — pick 2-3 per channel), per-tool prompt blocks the user can copy-paste, volume target (default 8-12 candidates per channel per round), drop instructions naming `.marketing/candidates/<channel>-1/` with filename pattern `<seq>-<tool>-<short-desc>.<ext>`, and a preview of the six-dimension selection rubric.
   >
   > **Hard rule:** do NOT call any image or video API. Briefs only.
   >
   > Return a one-line status per brief written."

4. **Tell the user:**

   > "Paid acquisition blueprint and creative briefs are written.
   >
   > - Campaign structure: `.marketing/paid/campaign-structure.md`
   > - Creative briefs: `.marketing/briefs/brief-<channel>-1.md` (one per channel)
   >
   > Now generate ad creative externally using the briefs in `.marketing/briefs/`. Each brief lists recommended tools and has copy-paste-ready prompt blocks. Drop generated files into `.marketing/candidates/<channel>-1/` using the filename pattern `<seq>-<tool>-<short-desc>.<ext>`. When a round is ready, run `/marketing:select-creative <channel> 1` (e.g., `/marketing:select-creative google-search 1`) to score them. When you find a winner, come back with `/marketing:paid --accept-creative <channel>-1 --winner <filename>`."

### Mode B — `--refine-brief --channel <channel>`

The user wants a new brief for one channel after seeing a selection they did not love.

1. **Read the existing brief** at `.marketing/briefs/brief-<channel>-<latest-round>.md` (find latest round via `Glob`) and any `.marketing/selected/<channel>-*.md` to surface prior critiques.
2. **Prompt the user interactively for notes**: "What should change in the brief? You can revise the strategic anchor, the visual or copy direction, the tool mix, the awareness level, or the volume target. What notes should creative-ops incorporate?" Wait for the answer.
3. **Determine the next round number** by listing `.marketing/candidates/<channel>-*` with `Glob` and adding 1 to the current max (if max is 1, next is 2).
4. **Dispatch `creative-ops` in brief mode** via the Task tool with the user's notes. Prompt: "You are `creative-ops` in BRIEF MODE. Read `.marketing/briefs/brief-<channel>-<prior-round>.md` (the prior brief), every `.marketing/selected/<channel>-*.md` file, and these user notes: `<notes>`. Write a new brief at `.marketing/briefs/brief-<channel>-<N>.md` where N is the new round number. Same 8-section shape. Call out what changed and why in a top note. Drop instructions name `.marketing/candidates/<channel>-<N>/`."
5. **Tell the user:** "New brief at `.marketing/briefs/brief-<channel>-<N>.md`. Generate round <N> externally, drop into `.marketing/candidates/<channel>-<N>/`, run `/marketing:select-creative <channel> <N>`."

### Mode C — `--accept-creative <channel>-<round> --winner <filename>`

The user is locking the winner of round <round> for this channel.

1. **Read `.marketing/selected/<channel>-<round>.md`.** If missing, abort and tell the user to run `/marketing:select-creative <channel> <round>` first.
2. **Validate the named winner** by parsing the file for the `### Winner` blocks under `## Winners (top 3)`. Confirm `<filename>` matches one of the listed winners (it should be a file in `.marketing/candidates/<channel>-<round>/`). If the named filename is not in the selected file's winner list, tell the user the valid winner filenames and stop. Spec Section 8 selection-mode rule: only files the rubric scored may be locked.
3. **Copy the winner** from `.marketing/candidates/<channel>-<round>/<filename>` to `.marketing/paid/creative-locked/<channel>/<filename>` using `Bash cp` (or `copy` on Windows — the harness handles both via `Bash`). Create the directory tree if needed.
4. **Write `.marketing/decisions/<channel>.md`** with fixed sections: `Channel: <channel>`, `Round: <round>`, `Winner file: <filename>`, `Copied to: .marketing/paid/creative-locked/<channel>/<filename>`, `Rationale: <verbatim rationale block from selected/<channel>-<round>.md>`, `Six-dimension scores: <copied from selected file>`, `Rejected alternatives considered: <list>`, a `Generated-by: /marketing:paid --accept-creative <channel>-<round> --winner <filename>` line, and a `Depends-on:` list citing `.marketing/positioning/positioning.md`, `.marketing/paid/ad-copy-briefs.md`, `.marketing/briefs/brief-<channel>-<round>.md`, and `.marketing/selected/<channel>-<round>.md`.
5. **Update `.marketing/paid/creative-locked.md`** (the canonical roll-up of all locked creative across channels). If it doesn't exist, create it with a header table; if it exists, append or update the row for `<channel>` with the new winner filename and timestamp.
6. **Tell the user:** "Channel `<channel>` locked at round <round>. Winner `<filename>` copied to `.marketing/paid/creative-locked/<channel>/`. Paper trail at `.marketing/decisions/<channel>.md`. Roll-up at `.marketing/paid/creative-locked.md`. When all channels in scope are locked, run `/marketing:ship-campaign` to push to Google Ads (paused-first)."

## Outputs

Mode A: `.marketing/paid/campaign-structure.md`, `.marketing/paid/keywords/*.csv`, `.marketing/paid/ad-copy-briefs.md`, `.marketing/paid/bid-strategy.md`, `.marketing/paid/budget-plan.md`, `.marketing/paid/google-ads-api-wiring.md`, `.marketing/paid/offline-conversion-spec.md`, `.marketing/briefs/brief-<channel>-1.md` (one per channel in scope).
Mode B: `.marketing/briefs/brief-<channel>-<N>.md` (new round).
Mode C: `.marketing/paid/creative-locked/<channel>/<filename>`, `.marketing/decisions/<channel>.md`, `.marketing/paid/creative-locked.md` (updated).

Cited from spec Section 5.4 (`/marketing:paid`), Section 4.2 (paid-acquisition-lead role), Section 7.4 (bid-strategy ladder), Section 8 (creative ops workflow).

## Reentrancy

Mode A re-run overwrites only `.marketing/paid/*` (the lead's own files) and `.marketing/briefs/brief-<channel>-1.md`. Leaves `.marketing/candidates/`, `.marketing/selected/`, `.marketing/decisions/`, and `.marketing/paid/creative-locked/` untouched. Mode B writes a new round brief and never touches prior round briefs — each round is preserved as a paper trail. Mode C only writes to `.marketing/paid/creative-locked/<channel>/`, `.marketing/decisions/<channel>.md`, and updates `.marketing/paid/creative-locked.md`; never deletes candidates or selected files. The iteration history across rounds is load-bearing and never trimmed.
