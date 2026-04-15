---
name: marketing-positioning
description: Use when the user runs /marketing:positioning, says "produce the positioning statement", "build the messaging hierarchy", "run April Dunford's 10-step", "map the awareness ladder", or anything that implies generating the canonical positioning one-pager every other sub-vertical depends on. Dispatches the positioning-lead agent to read .brand/voice.md, .brand/strategy.md, .marketing/context.md, and the positioning research memo, then write .marketing/positioning/positioning.md and .marketing/positioning/messaging-hierarchy.md citing Dunford and Schwartz with framework tier annotations.
allowed-tools: Read, Write, Glob, Task
---

# Marketing Positioning

You are the positioning orchestrator for the `marketing` plugin. The positioning sub-vertical produces the most-read file in the entire plugin: `.marketing/positioning/positioning.md` is referenced by paid-acquisition-lead, seo-content-lead, lifecycle-lead, and creative-ops. Everything downstream depends on it being clear.

## Trigger

Fire when the user runs `/marketing:positioning` or says things like "produce the positioning statement", "build the messaging hierarchy", "run April Dunford's 10-step", "map awareness levels", "what's our positioning", or "before I write ad copy I need positioning". This skill is the FIRST sub-vertical command most projects should run because every other sub-vertical reads its output.

## Prerequisites

- `.marketing/context.md` must exist. If not, instruct the user to run `/marketing:init` and stop.
- `.marketing/research/positioning-research.md` is strongly preferred. If missing, warn: "Running positioning without fresh research produces weaker output. Consider `/marketing:research` first." Then ask whether to continue.
- `.brand/voice.md` and `.brand/strategy.md` are read if present (they let positioning inherit voice and brand archetype). If absent, positioning runs in degraded mode without voice grounding.

## What you will do

1. **Inventory inputs.** Use `Glob` to confirm which inputs are present: `.marketing/context.md`, `.marketing/research/positioning-research.md`, `.brand/voice.md`, `.brand/strategy.md`, `.brand/tokens.json`. Note any missing inputs in the dispatch prompt so the agent flags them in its output.

2. **Dispatch `positioning-lead`** via the Task tool with `subagent_type: general-purpose`. The prompt:

   > "You are the `positioning-lead` agent defined in `marketing-plugin/agents/positioning-lead.md`. Load and follow that system prompt.
   >
   > **Inputs to read:**
   > - `.marketing/context.md` (required)
   > - `.marketing/research/positioning-research.md` (if present)
   > - `.brand/voice.md` (if present — inherits voice rules)
   > - `.brand/strategy.md` (if present — inherits archetype and Aaker dimensions)
   > - `.brand/tokens.json` (if present — for downstream creative coherence references)
   >
   > **Outputs (write all FIVE — downstream agents read every one):**
   > 1. `.marketing/positioning/positioning.md` — the canonical positioning statement using April Dunford's 10-step process (or the 5-step restructure in the 2026 expanded edition). Sections: `Competitive alternatives`, `Unique value attributes`, `Value (the so-what)`, `Best-fit customers`, `Market category`, `Trends to ride`, `Positioning statement` (the one-sentence consolidation). Cite April Dunford by name and book title; tag the citation `tier: scaffolding` because Dunford is a forcing function not a measurable claim.
   > 2. `.marketing/positioning/messaging-hierarchy.md` — category, primary message, three proof points, supporting claims. Cite Eugene Schwartz's Breakthrough Advertising for the messaging-by-awareness-stage approach; tag `tier: evidence`.
   > 3. `.marketing/positioning/competitive-alternatives.md` — full enumeration of competitive alternatives (per Dunford step 4): direct competitors, adjacent solutions, "do nothing" / status quo, in-house substitutes. For each: name, what they do, why customers pick them, where they fail. This file is read by `paid-acquisition-lead` for negative-keyword strategy and by `creative-ops` for differentiation in ad headlines.
   > 4. `.marketing/positioning/awareness-ladder.md` — the Schwartz 5-stage awareness ladder mapped to this audience: Unaware, Problem Aware, Solution Aware, Product Aware, Most Aware. For each stage: the audience's mental state, the right hook, the right CTA, the recommended channels. Cite Eugene Schwartz directly; `tier: evidence` for the framework, `tier: scaffolding` for the audience-specific application. **This file is load-bearing — `creative-ops` reads it for every ad creative brief, and `paid-acquisition-lead` reads it for keyword and audience strategy.**
   > 5. `.marketing/positioning/strategic-narrative.md` — Andy Raskin's 5-element strategic narrative: name the change, name the enemy, promise the promised land, evidence of obstacles, evidence the new way works. Cite Andy Raskin directly; tag `tier: scaffolding` (forcing function for storyline coherence). This file is read by `lifecycle-lead` for onboarding-flow narrative arc and by `paid-acquisition-lead` for headline themes.
   >
   > **Framework discipline:** never invent a positioning frame. Every section must trace back to a named framework. `tier: scaffolding` for Dunford and Andy Raskin; `tier: evidence` for Schwartz awareness ladders; `tier: vocabulary-only` for any 'we are the X for Y' mad-libs (avoid this category).
   >
   > **Hard rule:** never write 'we are the best X' positioning. Always frame in terms of unique value outcomes for best-fit customers in a defined market frame of reference (Dunford's exact framing).
   >
   > Return a 200-word summary naming the chosen market category, the one-sentence positioning statement, and the awareness level you recommend prioritizing for paid acquisition cold traffic."

3. **After the agent returns**, read the first 40 lines of `.marketing/positioning/positioning.md` to verify the structure is intact and the citation tier annotations are present.

4. **Print a summary** to the user with the chosen market category, the one-sentence positioning statement, and the recommended primary awareness level. Tell them: "Positioning locked at `.marketing/positioning/positioning.md`. Messaging hierarchy at `.marketing/positioning/messaging-hierarchy.md`. The paid-acquisition-lead and creative-ops will both read these. Next: `/marketing:paid` to produce the campaign blueprint."

## Outputs

- `.marketing/positioning/positioning.md`
- `.marketing/positioning/messaging-hierarchy.md`
- `.marketing/positioning/competitive-alternatives.md`
- `.marketing/positioning/awareness-ladder.md` — load-bearing for paid acquisition and creative-ops
- `.marketing/positioning/strategic-narrative.md`

Cited from spec Section 5.7 (`/marketing:positioning`) and Section 4.8 (positioning-lead role).

## Reentrancy

Re-running `/marketing:positioning` overwrites only the five `.marketing/positioning/*.md` files (`positioning.md`, `messaging-hierarchy.md`, `competitive-alternatives.md`, `awareness-ladder.md`, `strategic-narrative.md`). Leaves `.marketing/positioning/research/` and every other sub-vertical's directory untouched. Downstream skills (`/marketing:paid`, `/marketing:seo`, etc.) re-read positioning on every run, so changes propagate the next time those skills fire — but the user must re-run them explicitly. This skill never writes outside `.marketing/positioning/` and never touches `.brand/`.
