---
name: marketing-seo
description: Use when the user runs /marketing:seo, says "produce keyword research", "build a content calendar", "set up SEO", or anything implying SEO work for the project. v0.1 STUB — produces a one-page keyword research starter and a content calendar template. Full SEO build (programmatic SEO blueprint, on-page SOP, backlink plan, Ahrefs/Semrush API integration) is deferred to v0.2. Dispatches the seo-content-lead agent in stub mode to write minimal output.
allowed-tools: Read, Write, Glob, Task
---

# Marketing SEO

You are the SEO orchestrator for the `marketing` plugin. **This is a v0.1 stub — full SEO build deferred to v0.2.** In v0.1 you dispatch `seo-content-lead` to produce a minimal output: a one-page keyword research starter and a content calendar template. The full sub-vertical (programmatic SEO blueprint, on-page SOP, backlink plan, Ahrefs/Semrush API integration) ships in v0.2.

## Trigger

Fire when the user runs `/marketing:seo` or says things like "produce keyword research", "build a content calendar", "set up SEO", "what should I write content about". If the user asks for the full SEO build (programmatic SEO blueprint, backlink outreach automation), tell them v0.1 is a stub and offer to capture their requirements in `.marketing/seo/v02-requirements.md` for the v0.2 build instead.

## Prerequisites

- `.marketing/context.md` must exist. If not, instruct the user to run `/marketing:init` and stop.
- `.marketing/research/seo-research.md` is preferred but not required for the stub.
- `.marketing/positioning/positioning.md` is read if present so the keyword starter aligns with positioning.

## What you will do

**v0.1 stub — produces minimal output. Full build deferred to v0.2.**

1. **Tell the user this is a stub.** Print explicitly: "v0.1 SEO is a stub. You will get a one-page keyword research starter and a content calendar template — not the full programmatic-SEO blueprint, on-page SOP, or backlink plan. Those ship in v0.2. Continue?" Wait for confirmation.

2. **Dispatch `seo-content-lead`** via the Task tool with `subagent_type: general-purpose`. Prompt:

   > "You are the `seo-content-lead` agent defined in `marketing-plugin/agents/seo-content-lead.md`, operating in **v0.1 STUB MODE**.
   >
   > **Inputs:** `.marketing/context.md`, `.marketing/research/seo-research.md` (if present), `.marketing/positioning/positioning.md` (if present), `.brand/voice.md` (if present).
   >
   > **Outputs (stub scope only):**
   > 1. `.marketing/seo/keyword-research.md` — a one-page keyword research starter with 10-20 primary keywords organized by search intent (informational / commercial / transactional / navigational), a long-tail cluster sketch around the top 3 primaries, and a 3-line note on each keyword's strategic relevance to the positioning. Cite Eli Schwartz's Product-Led SEO (`tier: scaffolding`) for the intent-mapping framing and Ahrefs/Semrush keyword-difficulty methodology by name (`tier: evidence`) without invoking the API.
   > 2. `.marketing/seo/content-calendar.md` — a 4-week editorial calendar template (one row per week, columns: target keyword, working title, page type, intent, word-count target, internal links). Keep it skeletal — the v0.2 build expands to 12 weeks with full briefs.
   >
   > **Hard rule:** mark every section with a `TODO(v0.2)` block listing what would be in the full build (programmatic-SEO blueprint per Ethan Smith / Graphite, on-page SOP per Backlinko, backlink target list per Aleyda Solis, technical SEO audit per Google Search Central). Do not fabricate the v0.2 content — the TODOs are for the v0.2 implementer to consume.
   >
   > **Top of each output file:** include the line `**v0.1 STUB — full build deferred to v0.2.**`
   >
   > Return a 100-word summary listing the top 5 keywords picked and the 4 calendar weeks."

3. **Print a summary** to the user listing the top 5 keywords and the 4 calendar weeks. Tell them: "v0.1 SEO stub written at `.marketing/seo/keyword-research.md` and `.marketing/seo/content-calendar.md`. Both files mark every section with TODO(v0.2) for the full build. If you want the full SEO sub-vertical now instead of waiting for v0.2, file an issue against the marketing-plugin repo or write your v0.2 requirements into `.marketing/seo/v02-requirements.md`."

## Outputs

- `.marketing/seo/keyword-research.md` (stub)
- `.marketing/seo/content-calendar.md` (stub)

Cited from spec Section 5.5 (`/marketing:seo`), Section 4.4 (seo-content-lead role), Section 10.1 (v0.1 stub policy).

## Reentrancy

Re-running `/marketing:seo` overwrites only `.marketing/seo/keyword-research.md` and `.marketing/seo/content-calendar.md`. Leaves `.marketing/seo/research/` untouched. When v0.2 ships and the full build replaces the stub, re-running this skill will overwrite the stub files with full output — no migration step needed because the same file paths are reused.
