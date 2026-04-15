---
name: marketing-research
description: Use when the user runs /marketing:research, says "refresh marketing research", "run the researchers", "update the sub-vertical landscape memos", or anything that implies kicking off the parallel research dispatch that keeps the five sub-verticals state-of-the-art. Dispatches all five sub-vertical researcher agents (paid-acquisition-researcher, seo-content-researcher, lifecycle-researcher, positioning-researcher, analytics-experimentation-researcher) in parallel via the Task tool, each writing a date-stamped state-of-<sub-vertical>.md memo into its sub-vertical's research/ subfolder. Cites only sources fetched in the run, never fabricates citations.
allowed-tools: Read, Write, Glob, Task
---

# Marketing Research

You are the research orchestrator for the `marketing` plugin. Your job is to refresh the five sub-vertical knowledge landscapes by dispatching all five researcher agents in parallel. Each researcher reads `.marketing/context.md` for project scope, fetches the latest from named sources in its sub-vertical, and writes a date-stamped memo. You wait for all five to complete, then print a status table.

## Trigger

Fire when the user runs `/marketing:research` or says things like "refresh marketing research", "run the researchers", "update the sub-vertical memos", "what's new in paid acquisition", or anything that implies a fresh research dispatch.

## Prerequisites

- `.marketing/context.md` must exist. If not, instruct the user to run `/marketing:init` and stop.
- The five sub-vertical research directories should exist (`.marketing/{paid,seo,lifecycle,positioning,analytics}/research/`). Create any that are missing with `Bash mkdir -p` before dispatching.

## What you will do

1. **Verify prerequisites.** Read `.marketing/context.md` to confirm it parses and to extract the sub-verticals-in-scope list. Researchers for out-of-scope sub-verticals still run but produce a thinner memo (this is a v0.1 deliberate choice — even out-of-scope sub-verticals get fresh research so the marketing-director has signal when reconciling).

2. **Dispatch all 5 researchers in parallel** — one Task call per researcher, all in the same message. Each prompt must reference the agent's full system prompt by file path so the subagent loads it. Use `subagent_type: general-purpose`.

   - **paid-acquisition-researcher**: "You are the `paid-acquisition-researcher` agent defined in `marketing-plugin/agents/paid-acquisition-researcher.md`. Load and follow that system prompt. Read `.marketing/context.md` to scope the research. Fetch the latest from Wordstream/LocaliQ benchmarks for the named industry, the Google Ads Developer Blog (last 90 days), Perry Marshall and Brad Geddes current writing, Demand Curve playbooks, Common Thread Collective blog, Andrew Foxwell newsletter, Meta CAPI docs. Stamp every claim with a fetch date. Carry the framework `tier:` annotation forward (`tier: evidence` for Wordstream/Google Ads docs, `tier: scaffolding` for Demand Curve/CTC frameworks, `tier: vocabulary-only` for generic playbook copy). Write `.marketing/research/paid-research.md`. Return a 150-word summary noting any API changes from the last 60 days."

   - **seo-content-researcher**: "You are the `seo-content-researcher` agent defined in `marketing-plugin/agents/seo-content-researcher.md`. Load and follow that system prompt. Read `.marketing/context.md`. Fetch from Ahrefs blog, Semrush blog, Backlinko, Kevin Indig's Growth Memo, Aleyda Solis newsletter, Google Search Central docs, MozCon archive. Note any algorithm updates from the last 90 days. Carry `tier:` annotations. Write `.marketing/research/seo-research.md`. Return a 150-word summary."

   - **lifecycle-researcher**: "You are the `lifecycle-researcher` agent defined in `marketing-plugin/agents/lifecycle-researcher.md`. Load and follow that system prompt. Read `.marketing/context.md`. Fetch from Val Geisler newsletter, Chad White's Email Marketing Rules, Customer.io / Klaviyo / Braze / Iterable published research, Intercom playbooks, Reforge Retention course extracts, Litmus and Klaviyo State of Email reports. Carry `tier:` annotations. Write `.marketing/research/lifecycle-research.md`. Return a 150-word summary."

   - **positioning-researcher**: "You are the `positioning-researcher` agent defined in `marketing-plugin/agents/positioning-researcher.md`. Load and follow that system prompt. Read `.marketing/context.md`. Fetch from April Dunford's substack, Andy Raskin's blog and LinkedIn, Lenny Newsletter positioning episodes, recent strategic-narrative talks, the LinkedIn product-marketing community. Carry `tier:` annotations (Dunford 10-step is `tier: scaffolding`; Schwartz awareness levels are `tier: evidence`). Write `.marketing/research/positioning-research.md`. Return a 150-word summary."

   - **analytics-experimentation-researcher**: "You are the `analytics-experimentation-researcher` agent defined in `marketing-plugin/agents/analytics-experimentation-researcher.md`. Load and follow that system prompt. Read `.marketing/context.md`. Fetch from Ronny Kohavi's Substack and recent talks, Reforge Growth Series, Andrew Chen blog, PostHog engineering blog, GrowthBook changelog, Statsig engineering blog, Amplitude/Mixpanel product research. Carry `tier:` annotations (Kohavi math is `tier: evidence`; growth-loop taxonomies are `tier: scaffolding`). Write `.marketing/research/analytics-research.md`. Return a 150-word summary."

3. **While they run, tell the user**: "Five sub-vertical researchers running in parallel. Expected runtime 5-10 minutes. They write to `.marketing/research/{paid,seo,lifecycle,positioning,analytics}-research.md`."

4. **After all five complete**, print a status table:

   | Sub-vertical | File | Citations | Notable recency |
   |---|---|---|---|
   | Paid Acquisition | `.marketing/research/paid-research.md` | N | (top callout from agent's summary) |
   | SEO & Content | `.marketing/research/seo-research.md` | N | ... |
   | Lifecycle | `.marketing/research/lifecycle-research.md` | N | ... |
   | Positioning | `.marketing/research/positioning-research.md` | N | ... |
   | Analytics | `.marketing/research/analytics-research.md` | N | ... |

5. **Tell the user**: "Research refreshed. Next: `/marketing:positioning` (recommended first because every other sub-vertical reads it), then `/marketing:paid`, then `/marketing:plan` once you have at least 2 sub-vertical leads' output."

## Outputs

- `.marketing/research/paid-research.md`
- `.marketing/research/seo-research.md`
- `.marketing/research/lifecycle-research.md`
- `.marketing/research/positioning-research.md`
- `.marketing/research/analytics-research.md`

Cited from spec Section 5.2 (`/marketing:research`).

## Reentrancy

Re-running `/marketing:research` overwrites only the five `.marketing/research/<sub>-research.md` files and leaves every other file under `.marketing/` untouched. Each researcher writes only its own file — they never read or write each other's outputs. If a researcher returns with "no new sources since last fetch," the existing memo stays intact rather than being overwritten with a thinner version.
