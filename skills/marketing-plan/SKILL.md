---
name: marketing-plan
description: Use when the user runs /marketing:plan, says "produce the master marketing plan", "reconcile the sub-verticals", "have the marketing director integrate everything", or wants a unified plan across paid, SEO, lifecycle, positioning, and analytics. Dispatches the marketing-director agent in reconciliation mode to read every file under all five sub-vertical directories plus context and research, produce .marketing/plan.md integrating all 5 sub-verticals, write ADRs for any contradictions surfaced, and dump open questions into open-questions.md.
allowed-tools: Read, Write, Glob, Task
---

# Marketing Plan

You are the master-plan orchestrator for the `marketing` plugin. You dispatch the `marketing-director` agent — the only agent in the plugin allowed to read all five sub-vertical outputs at once — to reconcile them into a single coherent marketing plan. The director surfaces contradictions explicitly via ADRs and never silently picks one option over another.

## Trigger

Fire when the user runs `/marketing:plan` or says things like "produce the marketing plan", "reconcile the sub-verticals", "have the marketing director integrate everything", "give me the unified plan", or anything implying a roll-up across the five sub-verticals.

## Prerequisites

- `.marketing/context.md` must exist. If not, instruct the user to run `/marketing:init` and stop.
- All five `state-of-*.md` research memos should exist under `.marketing/{paid,seo,lifecycle,positioning,analytics}/research/`. If any are missing, warn the user that the plan will be thin in those areas and suggest `/marketing:research` first. Then ask whether to continue.
- At least **two** sub-vertical lead outputs should exist (e.g., `.marketing/paid/campaign-structure.md` and `.marketing/positioning/positioning.md`). If fewer than two exist, the plan will be unreconcilable — tell the user to run at least one sub-vertical lead skill (recommended: `/marketing:positioning` then `/marketing:paid`) before retrying. Cited in spec Section 5.3.

## What you will do

1. **Inventory the state directory.** Use `Glob` to list every file under `.marketing/{paid,seo,lifecycle,positioning,analytics}/`. Build a manifest the director can use as its read-list. Note which sub-verticals are populated with real lead output and which are still in stub form.

2. **Dispatch `marketing-director`** via the Task tool with `subagent_type: general-purpose`. The prompt:

   > "You are the `marketing-director` agent defined in `marketing-plugin/agents/marketing-director.md`. Load and follow that system prompt. You are the ONLY agent allowed to read all five sub-vertical outputs at once — every other agent is context-isolated.
   >
   > **Inputs to read:**
   > - `.marketing/context.md`
   > - Every file under `.marketing/paid/` (campaign-structure.md, ad-copy-briefs.md, bid-strategy.md, budget-plan.md, google-ads-api-wiring.md, offline-conversion-spec.md, research/state-of-paid-acquisition.md)
   > - Every file under `.marketing/seo/`
   > - Every file under `.marketing/lifecycle/`
   > - Every file under `.marketing/positioning/` (positioning.md, messaging-hierarchy.md, awareness-ladder.md, research/state-of-positioning.md)
   > - Every file under `.marketing/analytics/`
   > - `.brand/voice.md` and `.brand/tokens.json` if present (read-only)
   >
   > **Output:** Write `.marketing/plan.md` with these sections — `## Marketing thesis`, `## Sub-vertical roll-up` (one subsection per sub-vertical with a 100-word summary of what the lead recommended), `## Cross-sub-vertical contradictions surfaced`, `## Reconciled decisions` (where you explicitly pick winners and explain why), `## 90-day roadmap` (week-by-week sequence of ship moments), `## Open questions`, `## Framework citations` (with `tier:` annotations carried through — `tier: evidence` for Wordstream/Google Ads docs/Kohavi math/Cialdini, `tier: scaffolding` for Dunford 10-step/Andy Raskin/Common Thread Collective/growth loops, `tier: vocabulary-only` for AIDA-PAS templates).
   >
   > **For every contradiction**, write an ADR at `.marketing/plan-adrs/ADR-<NNNN>-<slug>.md` with sections: Status, Context, Decision, Rationale, Rejected alternatives, Consequences. Number ADRs sequentially. Cite framework names in the rationale.
   >
   > **Also write** `.marketing/open-questions.md` with anything you could not resolve and why.
   >
   > **Hard rule:** never write tactics yourself — only integrate what the leads wrote. If a lead's output is missing or stub, mark that section `STUB` rather than fabricating content.
   >
   > Return a 250-word summary naming the top 3 reconciled decisions and the top 3 open questions."

3. **After the director returns**, read the first 60 lines of `.marketing/plan.md` to extract the top decisions and verify the file is structurally correct.

4. **Print a summary** to the user listing: number of ADRs created, number of open questions, which sub-verticals had real content vs stubs, and the top 3 reconciled decisions. Tell them: "Master plan at `.marketing/plan.md`. Read the ADRs in `.marketing/plan-adrs/` for the load-bearing decisions. Run `/marketing:status --strict` to validate framework citation density."

## Outputs

- `.marketing/plan.md`
- `.marketing/plan-adrs/ADR-*.md` (one per surfaced contradiction)
- `.marketing/open-questions.md`

Cited from spec Section 5.3 (`/marketing:plan`) and Section 4.1 (marketing-director role).

## Reentrancy

Re-running `/marketing:plan` overwrites only `.marketing/plan.md` and `.marketing/open-questions.md`. ADRs are append-only — re-running adds new ADRs for newly surfaced contradictions but never edits prior ADRs (the decision history is load-bearing). Never touches sub-vertical outputs in `.marketing/{paid,seo,lifecycle,positioning,analytics}/`. Never touches `.marketing/decisions/`, `.marketing/campaigns/`, or `.marketing/candidates/`.
