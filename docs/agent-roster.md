# Agent Roster & Handoff Protocol

## The 12 agents (13 mode-rows because creative-ops has two)

Twelve agents organized by sub-vertical: one director, five lead-and-researcher pairs, one shared creative-ops. Each agent produces one or more artifacts in `.marketing/`. No agent reads its own output. The `creative-ops` agent is the only one that operates in two modes from a single file — both modes share a single agent definition (`agents/creative-ops.md`) and dispatch via different skills (`/marketing:paid` for brief mode, `/marketing:select-creative` for selection mode). It is shown as two rows below for clarity.

| Agent | Sub-vertical | Mode | Primary input | Primary output | Model |
|---|---|---|---|---|---|
| `marketing-director` | global | single | `.marketing/context.md`, every `research/*.md`, every sub-vertical output | `plan.md`, `plan-adrs/ADR-*.md`, `open-questions.md` | opus |
| `paid-acquisition-lead` | Paid | single | `context.md`, `research/paid-research.md`, `positioning/positioning.md`, `analytics/event-taxonomy.yaml`, `.brand/voice.md`, `.brand/tokens.json` | `paid/campaign-structure.md`, `paid/keywords/*.csv`, `paid/ad-copy-briefs.md`, `paid/bid-strategy.md`, `paid/budget-plan.md`, `paid/google-ads-api-wiring.md`, `paid/offline-conversion-spec.md` | opus |
| `paid-acquisition-researcher` | Paid | single | `context.md`, live web | `research/paid-research.md` | sonnet |
| `seo-content-lead` | SEO | single | `context.md`, `research/seo-research.md`, `positioning/positioning.md`, `.brand/voice.md` | `seo/keyword-research.md`, `seo/content-calendar.md`, `seo/onpage-sop.md`, `seo/programmatic-seo-blueprint.md`, `seo/backlink-plan.md` | opus |
| `seo-content-researcher` | SEO | single | `context.md`, live web | `research/seo-research.md` | sonnet |
| `lifecycle-lead` | Lifecycle | single | `context.md`, `research/lifecycle-research.md`, `positioning/positioning.md`, `.greenfield/data-model.md`, `.brand/voice.md` | `lifecycle/onboarding-flow.md`, `lifecycle/retention-flows.md`, `lifecycle/winback-program.md`, `lifecycle/transactional-specs.md`, `lifecycle/channel-strategy.md` | opus |
| `lifecycle-researcher` | Lifecycle | single | `context.md`, live web | `research/lifecycle-research.md` | sonnet |
| `positioning-lead` | Positioning | single | `context.md`, `research/positioning-research.md`, `.brand/voice.md` | `positioning/positioning.md`, `positioning/messaging-hierarchy.md`, `positioning/competitive-alternatives.md`, `positioning/awareness-ladder.md`, `positioning/strategic-narrative.md` | opus |
| `positioning-researcher` | Positioning | single | `context.md`, live web | `research/positioning-research.md` | sonnet |
| `analytics-experimentation-lead` | Analytics | single | `context.md`, `research/analytics-research.md`, `.greenfield/data-model.md`, all sub-vertical outputs | `analytics/event-taxonomy.yaml`, `analytics/attribution-model.md`, `analytics/experimentation-framework.md`, `analytics/dashboard-specs.md`, `analytics/experiment-backlog.md`, `.greenfield/events.yaml` (if greenfield present) | opus |
| `analytics-experimentation-researcher` | Analytics | single | `context.md`, live web | `research/analytics-research.md` | sonnet |
| `creative-ops` | shared | brief | `paid/ad-copy-briefs.md`, `positioning/awareness-ladder.md`, `.brand/voice.md`, `.brand/tokens.json`, `.brand/logo/`, `.brand/motion/` | `briefs/brief-<channel>.md`, `paid/creative/copy-variants/{campaign}/{adgroup}.md` | opus |
| `creative-ops` | shared | selection | `candidates/<channel>-<round>/`, `briefs/brief-<channel>.md`, `.brand/voice.md`, `positioning/awareness-ladder.md` | `selected/<channel>-<round>.md` | opus |

`marketing-status` is **a skill, not an agent** — it reads the `.marketing/` tree and prints a console report without dispatching any agent. See `skills/marketing-status/SKILL.md`. Skills under `skills/` are the user-facing entry points; they invoke the agents above. See `docs/workflow.md` for the phase-by-phase dispatch table.

## Handoff protocol

Agents never talk to each other directly. All communication is via files in `.marketing/`. Each agent:

1. Reads its declared inputs (table above).
2. Writes its declared output.
3. Emits a short (<300 word) summary back to the orchestrating skill.

Every output file has a fixed header block with three fields — `Generated-by:`, `Depends-on:`, `Sources-cited:`. The `marketing-status` skill validates these on every run. A file without the header is a bug; a file whose `Depends-on:` points at a missing input is a bug; a file whose `Sources-cited:` is empty when the agent's contract requires citations is a bug.

Why file-based, not message-based:

- **Context isolation.** Each agent has minimal context; no token burn on other agents' deliberations. With 12 agents this matters more than it does in a 6-agent plugin — pairwise message passing would explode.
- **Debuggability.** The user inspects what each agent actually produced — no opaque in-memory graph.
- **Resumability.** Partial workflows resume by re-running specific agents or skills.
- **Git-committable.** The filesystem is the repo's source of truth, not a live message bus.
- **Multimodal feeds.** The `creative-ops` agent in selection mode reads PNG, MP4, and GIF files directly from `candidates/`. Files-as-inputs is the only shape that accommodates multimodal reads naturally.

## `creative-ops` two-mode operation

The `creative-ops` agent is the only agent in the roster that operates in two distinct modes, and it is worth explaining why they are collapsed into one agent rather than split into two.

**Brief mode** (invoked during `/marketing:paid`): read `.marketing/paid/ad-copy-briefs.md`, `.marketing/positioning/awareness-ladder.md`, `.brand/voice.md`, `.brand/tokens.json`, and any locked visuals in `.brand/logo/` and `.brand/motion/`. Write one `briefs/brief-<channel>.md` per channel in scope (typically `google-search`, `google-pmax`, `meta-static`, `meta-reels`, `tiktok`, `youtube`, `linkedin`), each with a strategic anchor, audience awareness stage, message hierarchy, brand alignment quote, visual direction, recommended tools, per-tool prompt blocks, asset specs, volume target, drop instructions, selection criteria preview, and compliance notes. Output template: `templates/creative-brief-template.md`.

**Selection mode** (invoked during `/marketing:select-creative <channel> <round>`): read every file in `.marketing/candidates/<channel>-<round>/` with multimodal vision. Score each candidate on the six-dimension rubric (brand alignment, channel fit, awareness stage match, message hierarchy, creative quality, A/B variation potential). Write `selected/<channel>-<round>.md` with winners, rejected with reasons, a recommendation, and an iteration suggestion. Output template: `templates/selected-creative-template.md`.

These could be two separate agents — `brief-writer` and `judge`. They were collapsed into one for three reasons, mirroring `brand-plugin`'s `creative-director` precedent exactly:

1. **Identical taste model.** The same aesthetic and strategic judgement that shapes a brief also scores the results. Splitting them would require duplicating the brand-voice vocabulary, the awareness-ladder context, and the channel-fit heuristics in two system prompts, risking drift.
2. **Read the same inputs.** Both modes read `.brand/voice.md`, `.brand/tokens.json`, and `positioning/awareness-ladder.md`. The only extra input in selection mode is the `candidates/` folder. Two agents reading 90% the same context is exactly the duplication `brand-plugin`'s add/remove rule warns against.
3. **Hand-off cleanliness.** An iteration loop that ran user → brief-writer → user → judge → user → brief-writer v2 would push context back and forth unnecessarily. One agent with two modes lets the system prompt reason about "what I briefed last round" when writing the next brief after a selection.

The system prompt branches on the invoking command. `/marketing:paid` invokes brief mode; `/marketing:select-creative` invokes selection mode. See `agents/creative-ops.md` for the branching language.

## Per-sub-vertical agent pairs

Each of the five sub-verticals has both a lead and a researcher. The pairing is not casual — it mirrors how real marketing teams divide labor and it solves a specific failure mode in LLM agents.

The researcher's job is to keep the lead's domain state-of-the-art. Marketing sources change every quarter: Wordstream publishes a new home services benchmark every year, the Google Ads Developer Blog posts API changes monthly, Demand Curve updates its playbooks every few months, Ahrefs publishes new backlink studies regularly, Reforge releases new growth program content quarterly, and Kohavi's substack drops new experimentation pitfalls weekly. An agent that reads Perry Marshall's 2018 book and never refreshes will, within 18 months, be giving advice that's wrong about Quality Score weights, wrong about Smart Bidding behavior, and wrong about which campaign types exist. The researcher prevents this — every `/marketing:research` run regenerates `research/<subvert>-research.md` with a fresh fetch date and fresh citations.

The lead's job is to act on that knowledge — pick frameworks, write strategy, produce the artifacts the campaign needs. The lead reads the researcher's memo, applies its own knowledge of the structural frameworks (which are stable over decades — Dunford, Schwartz, Cialdini, Kohavi), and writes the deliverables.

Splitting these into two agents enforces a useful discipline: the researcher cannot fabricate strategy and the lead cannot pretend its training-cutoff knowledge is current. Each agent has a single charter and a single failure mode. Combined into one agent, the failure modes blur and the user cannot tell whether a stale recommendation came from stale research or stale reasoning.

The pair pattern also mirrors the marketing-team org chart most users will recognize: a paid acquisition manager who runs the campaigns and a growth analyst who keeps an eye on the landscape; an SEO strategist and an SEO researcher; a positioning lead and a competitive-intel analyst. The plugin's roster maps cleanly onto a real team, which makes it easier for the user to brief the agents and to debug their outputs.

## When to add an agent

Borrowed from `brand-plugin`'s discipline, which itself borrowed from greenfield. **Add an agent** if, and only if:

- A new deliverable is genuinely needed that doesn't fit any existing agent's charter; AND
- It has its own inputs, outputs, and tools; AND
- It represents an independent expertise that would not just re-run the same reasoning on the same files.

**Do not add** an agent if:

- The "role" is a re-framing of an existing one. An earlier draft considered splitting `creative-ops` into `copy-ops` and `visual-ops`. Those collapsed because the same taste model judges both, and splitting them would duplicate brand-voice context in two system prompts.
- The role exists only during implementation or downstream phases. Push it to the right plugin instead. ("Build my landing page" → not a marketing agent, that's a web/greenfield job.)
- Its outputs would always be read alongside, and identical-in-reasoning-to, an existing agent's outputs.

Twelve is the default for v0.1, not a mandate. For a project that has no paid acquisition need at all (e.g., a B2B that lives entirely off SEO and outbound), `paid-acquisition-lead` and `paid-acquisition-researcher` may be skipped and the workflow is `init → research → positioning → seo → analytics`. The `marketing-director` reconciles whatever exists.

## When to remove an agent

**Remove** if:

- Two agents end up reading the same inputs and writing overlapping outputs. Collapse them.
- An agent's output is consistently empty or trivial for realistic project types.
- An agent's output is always subsumed by another agent's output.

If a future user runs the plugin against a B2C app where lifecycle and creative-ops collapse into the same email-design problem, the right move is to remove the lifecycle-lead and have creative-ops own email creative. This kind of collapse is encouraged when it surfaces from real use, not before.

## Model assignment rationale

Six agents are assigned `opus`, six are assigned `sonnet`. The split tracks reasoning depth and citation density, not output length.

- **`marketing-director` → opus.** This is the highest-leverage reasoning in the entire pipeline. Reconciling five sub-vertical outputs, surfacing contradictions, and writing ADRs that justify rejected alternatives is exactly the kind of multi-document reasoning where opus's gap shows up. Getting the reconciliation wrong poisons the entire downstream plan.

- **`paid-acquisition-lead` → opus.** Designs campaign architecture across five entity levels (campaign → ad group → keyword → ad → bid strategy), reasons about bid-strategy ladders, writes Google Ads API wiring specs, and enforces cost safeguards. Cites Perry Marshall, Brad Geddes, Wordstream, and Demand Curve with tier annotations. Heavy structured reasoning over many constraints — opus earns its keep.

- **`seo-content-lead` → opus.** Distinguishes editorial SEO, programmatic SEO, and technical SEO and prescribes different approaches per page type. Cites Eli Schwartz, Ethan Smith / Graphite, Google Search Central, and Ahrefs with tier annotations. Programmatic SEO blueprints in particular require multi-step reasoning about category-page templates and internal linking rules.

- **`lifecycle-lead` → opus.** Reasons across email, SMS, push, and in-product channels, picks tools (Customer.io, Klaviyo, Resend), designs onboarding sequences (Val Geisler dinner-party 6-step), and maps retention flows to specific behavior triggers. Multi-channel reasoning with deliverability and compliance constraints — opus.

- **`positioning-lead` → opus.** Applies April Dunford's 10-step process and Eugene Schwartz's 5 awareness levels to a real ICP. Writes the canonical positioning one-pager that every other agent reads. The most-read file in the entire plugin — getting it wrong cascades. Opus.

- **`analytics-experimentation-lead` → opus.** Reasons about attribution models, experiment design, statistical power, SRM checks, and Twyman's Law (citing Kohavi). Writes event taxonomies that downstream code will instrument. Statistical reasoning under uncertainty — exactly the opus use case.

- **`creative-ops` → opus** (both modes). Brief mode writes prompts that must land well across six different visual AI tools. Selection mode applies a six-axis rubric to multimodal inputs with cited reasoning. Visual judgement with citation density is exactly the kind of work where opus shows up.

- **All five researchers → sonnet.** Their job is structured research and synthesis — fetch, summarize, organize into one file, stamp with date. No deep reasoning; the depth comes from the live sources the agent cites. Sonnet is sufficient and the cost savings matter because researchers run frequently (every `/marketing:research` invocation runs all five in parallel) and the work is high-volume.

Model assignments are declared in each agent's YAML frontmatter (`model: opus` or `model: sonnet`) and in `.claude-plugin/plugin.json`. Override per project via environment if cost is an issue — the leads in particular can fall back to sonnet for prototype runs, but production runs should use opus, especially for `marketing-director` and `paid-acquisition-lead` where bad reasoning has dollar consequences.
