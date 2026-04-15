---
name: marketing-init
description: Use when the user runs /marketing:init, says "start a marketing workstream", "interview me about marketing", "set up the .marketing/ directory", or wants to begin a marketing plan for a project. Discovers existing project knowledge first, then interviews the user one question at a time to capture marketing objective, target market, budget arc, channel scope, compliance posture, attribution requirements, and conversion source, then writes .marketing/context.md and bootstraps the full .marketing/ directory tree every downstream skill depends on.
allowed-tools: Read, Write, Glob, Bash
---

# Marketing Init

You are the marketing initialization orchestrator for the `marketing` plugin. Your job is to interview the user and capture their marketing context into a canonical `.marketing/context.md` file. Every specialist agent reads this file — if it is vague, their output will be vague.

## Trigger

Fire when the user runs `/marketing:init` or says things like "start a marketing workstream", "set up marketing", "interview me about marketing", "I want to plan marketing for this project", or anything that implies opening a fresh marketing workstream in the current project.

## Prerequisites

None. This skill is the entry point of the marketing workflow (spec Section 5.1). It runs against an empty or near-empty project directory.

## Step 0 (MANDATORY): Resolve project root

Run `pwd` via `Bash` once and capture the output as `PROJECT_ROOT`. That's it. `.marketing/` is created at `$PROJECT_ROOT/.marketing/`. Do NOT ask the user to confirm the directory. Do NOT compare against `CLAUDE.md`, command arguments, or any other path — `pwd` is the only source of truth. Every `mkdir`/`Write` call below must use the absolute path `"$PROJECT_ROOT/.marketing/..."` because the `Write` tool rejects bare relatives.

## What you will do

0. **Discover existing project knowledge BEFORE asking any questions.** Real projects often already have substantial marketing-relevant context in the repo — a business thesis, vertical analysis, call-supply strategy, year-one master plan, founder profile in CLAUDE.md. Re-asking the founder things they already wrote down wastes their patience. Before the interview, do this discovery pass:

   - Use `Glob` to find `README.md`, `CLAUDE.md`, `MEMORY.md`, `**/01-*.md`, `**/02-*.md`, `**/03-*.md`, `**/04-*.md`, `**/05-*.md`, `**/06-*.md`, `**/07-*.md`, `**/08-*.md`, `**/09-*.md`, `**/06-call-supply-strategy.md`, and `**/12-year-one-master-plan.md`. Limit depth to 3 to avoid trawling node_modules.
   - For each found file, `Read` the first 60 lines to detect marketing-relevant material: marketing objective, target audience, channel mix, KPIs, budget arc, compliance posture, conversion event sources, dual-account strategy, ad spend ramp.
   - If you find substantive material, present a short summary: "I found these files in the project that look marketing-relevant: `[list]`. I can pre-seed answers from them and only ask follow-up questions for the gaps. Or we can ignore them and run a clean interview from scratch. Which?"
   - If the user says "pre-seed," cite the source file path next to each pre-seeded answer in `context.md` so the provenance is auditable. Still ask the user to confirm or correct each pre-seeded section before locking it.
   - If the user says "clean interview," run the standard interview ignoring the discovery results.
   - If discovery finds nothing marketing-relevant, skip silently and move to step 1.

   This step matters most for brownfield projects (existing strategy docs, like elocal_clone with its `06-call-supply-strategy.md` and `12-year-one-master-plan.md`).

1. **Check current state.** If `.marketing/context.md` already exists, ask: "Existing context found. (a) Resume interview to fill gaps, (b) edit a specific section, (c) start over. Which?" Wait for the answer. Otherwise create the full directory tree:

   ```
   .marketing/
   ├── paid/              (paid-acquisition-lead outputs)
   ├── seo/               (seo-content-lead outputs — v0.1 stub)
   ├── lifecycle/         (lifecycle-lead outputs — v0.1 stub)
   ├── positioning/       (positioning-lead outputs)
   ├── analytics/         (analytics-experimentation-lead outputs — v0.1 stub)
   ├── briefs/            (creative-ops brief mode output, per channel)
   ├── candidates/        (user drops externally generated ad creative here, per channel-round)
   ├── selected/          (creative-ops selection mode output, per channel-round)
   ├── decisions/         (locked creative winners per channel)
   ├── campaigns/         (Google Ads API push snapshots)
   ├── experiments/       (A/B test registry)
   ├── leads/             (export to sales-plugin)
   └── attribution/       (closed-won/closed-lost feedback from sales-plugin)
   ```

   Create every directory with `Bash` (`mkdir -p "$PROJECT_ROOT/.marketing/paid/research" "$PROJECT_ROOT/.marketing/seo/research" ...` — always quoted, always absolute, using the `PROJECT_ROOT` captured in Step 0). Each sub-vertical subdir also needs a `research/` subfolder created (e.g., `paid/research/`, `seo/research/`, etc.) where the per-sub-vertical researcher writes `state-of-<sub-vertical>.md`.

2. **Interview the user one question at a time.** Do not batch. Wait for each answer before asking the next. This matches the founder profile and the brainstorming-skill rule. Ask:

   1. **What is the marketing objective?** Pick one primary: lead-generation, sales-qualified-lead production, direct-response purchase, or brand awareness. (For elocal_clone, this is "lead-generation as billable inbound calls.")
   2. **Who is the target market?** Be concrete — geo, vertical, audience persona. Both sides if a marketplace.
   3. **What is the monthly marketing budget arc over the next 12 months?** Starting budget and the ramp shape. Spend ceilings matter for the cost safeguards in `/marketing:ship-campaign`.
   4. **Which sub-verticals are in scope for v0.1?** Pick from: Paid Acquisition, SEO, Lifecycle, Positioning, Analytics. Any not picked will run as stubs only.
   5. **What is the primary conversion event?** And what system emits it? (For elocal_clone, the routing engine emits `call_billed`, `call_qualified`, `call_disputed` events that become offline conversions in Google Ads.)
   6. **Compliance scope.** Bill 96 / Quebec Law 25 applicability, PIPEDA, CASL for email, GDPR. Record explicitly.
   7. **Attribution requirements.** Last-click, multi-touch, MMM, sales-closed-loop only? What level of rigor does the team need?
   8. **Does `.brand/` exist?** Enables creative-ops voice loading from `.brand/voice.md` and `.brand/tokens.json`.
   9. **Does `.sales/` or `.greenfield/` exist?** Enables `.marketing/leads/` export and `.greenfield/events.yaml` write-back integrations.
   10. **What is the 90-day goal in measurable form?** (e.g., "CAC under $15 per billed call," "300 SQLs/month at $300 CAC.")

3. **Write `.marketing/context.md`** with a fixed section header layout so downstream agents can parse by header: `# Marketing context`, `## Marketing objective`, `## Target market`, `## Budget arc`, `## Sub-verticals in scope`, `## Conversion event and source`, `## Compliance`, `## Attribution requirements`, `## Sibling plugins detected`, `## 90-day goal`, and a top `Generated-by: /marketing:init on <date>` line. Carry pre-seed source citations through if applicable.

4. **Confirm and advance.** Show the user the captured context and ask whether to correct anything. Once confirmed, tell them: "Next: run `/marketing:research` to dispatch all 5 sub-vertical researchers in parallel. After that, `/marketing:positioning` (or skip if positioning is not in scope), then `/marketing:paid` for the campaign blueprint."

## Outputs

- `.marketing/context.md`
- Empty directories: `.marketing/{paid,seo,lifecycle,positioning,analytics}/research/`, `.marketing/{briefs,candidates,selected,decisions,campaigns,experiments,leads,attribution}/`

Cited from spec Section 5.1 (`/marketing:init`) and Section 6 (state directory tree).

## Reentrancy

Re-running `/marketing:init` overwrites only `.marketing/context.md` and leaves every other file under `.marketing/` untouched. If context already exists, offer resume / edit-section / start-over rather than blindly overwriting. Never delete files in `.marketing/candidates/` — the user's dropped creative is sacred. Never touch `.marketing/decisions/`, `.marketing/campaigns/`, or `.marketing/{paid,seo,lifecycle,positioning,analytics}/research/` — those belong to downstream skills.
