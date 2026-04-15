# Marketing Plugin — Design Document

> v0.1.0 — synthesized from `plugin-specs/marketing-plugin-spec.md` and pattern-matched against `brand-plugin/docs/`.

## Purpose

`marketing` is a Claude Code plugin for the demand-generation phase of a business. It runs after brand and greenfield, and is organized as **five clearly bounded sub-verticals inside one plugin shell**: Paid Acquisition, SEO and Content, Lifecycle and Retention, Positioning and Messaging, and Analytics and Experimentation. Each sub-vertical has its own lead agent, its own dedicated researcher who keeps the lead's domain state-of-the-art, and its own state subdirectory. A single `marketing-director` agent reconciles the five into a coherent master plan. A single shared `creative-ops` agent writes ad-creative briefs and judges returned candidates.

**What it explicitly does NOT do:** PR or media relations, influencer marketing, event marketing, brand-building per se (logos, voice, archetype — that is `brand-plugin`'s job, this plugin only *reads from* `.brand/`), sales pipeline management or SDR sequences (that is `sales-plugin`'s job, this plugin only *hands off to* `.sales/`), product analytics beyond the marketing attribution slice. The plugin is a planning-and-execution layer for the upstream demand side; everything else lives in a sibling.

## The 5 sub-verticals

**Paid Acquisition.** The lead owns Google Ads, Meta Ads, TikTok, LinkedIn, landing-page tests, creative ops, bidding, and offline conversion uploads. The researcher refreshes Wordstream/LocaliQ benchmark reports, the Google Ads Developer Blog, Demand Curve playbooks, Common Thread Collective and Andrew Foxwell, Meta Marketing API and CAPI docs. **v0.1 status: fully built** — this is the load-bearing sub-vertical for `elocal_clone`'s Month 1 bottleneck and the only one with a complete knowledge base, full skill set, and live Google Ads API push.

**SEO and Content.** The lead owns keyword research, editorial calendar, on-page SEO SOP, programmatic SEO blueprints, internal linking, backlink targets, and E-E-A-T compliance. The researcher refreshes Ahrefs, Semrush, Backlinko, Eli Schwartz, Ethan Smith / Graphite, Kevin Indig, Aleyda Solis, Google Search Central, MozCon talks. **v0.1 status: stub** — agent files and skill files exist, knowledge base is sparse, output is a thin memo. Full build in v0.2.

**Lifecycle and Retention.** The lead owns email, SMS, push, onboarding sequences, retention flows, winback programs, transactional messaging, and channel strategy. The researcher refreshes Val Geisler, Chad White, Customer.io, Klaviyo, Braze, Iterable, Intercom, Reforge Retention course extracts. **v0.1 status: stub** — same shape as SEO. Full build in v0.2.

**Positioning and Messaging.** The lead owns ICP definition, competitive alternatives, messaging hierarchy, value-prop map, awareness-level ladder, and the canonical positioning one-pager every other agent reads. The researcher refreshes April Dunford, Andy Raskin, Eugene Schwartz, Geoffrey Moore, Donald Miller. **v0.1 status: partial** — the lead exists in stub form but the bits Paid Acquisition needs are wired up. Specifically, Paid Acquisition reads `.marketing/positioning/positioning.md` and `.marketing/positioning/awareness-ladder.md` to pick ad-copy variants per Schwartz awareness level, so positioning must produce at least those two files even in v0.1. Full Dunford 10-step build in v0.2.

**Analytics and Experimentation.** The lead owns event taxonomy, attribution model, A/B testing framework, dashboard specs, and experiment backlog. The researcher refreshes Ronny Kohavi, Reforge Growth Series, Brian Balfour, Andrew Chen, PostHog, GrowthBook, Statsig. **v0.1 status: stub** — agent and skill files exist; the full Kohavi-grade experimentation framework lands in v0.2.

## The brief-and-judge architecture for ad creative

This is the load-bearing architectural choice for the creative side of the plugin and the one most worth defending. It mirrors `brand-plugin`'s brief-and-judge architecture exactly, just for ad creative instead of logos.

The obvious design is "plugin calls image API" — the user types `/marketing:paid`, the plugin hits Nano Banana Pro, hands back four PNGs, user picks one. That design is rejected. This plugin splits generation from judgement: the `creative-ops` agent (in **brief mode**, invoked from `/marketing:paid`) reads `.brand/voice.md`, `.brand/tokens.json`, `.marketing/positioning/awareness-ladder.md`, and `.marketing/paid/ad-copy-briefs.md`, then writes one channel-specific creative brief per channel to `.marketing/briefs/brief-<channel>.md` (where channel is `google-search`, `google-pmax`, `meta-static`, `meta-reels`, `tiktok`, `youtube`, `linkedin`). The user takes that brief to whichever external tools they prefer — Nano Banana Pro for static, Veo 3.1 for video, Higgsfield for motion, Midjourney for stylized, Recraft for vector, Ideogram for typography, Sora 2 for cinematic — generates 5-15 candidates per channel per round, drops them into `.marketing/candidates/<channel>-<round>/`, and runs `/marketing:select-creative <channel> <round>`.

The `creative-ops` agent then re-invokes in **selection mode** and reads every candidate with multimodal vision. It scores each candidate against a six-dimension rubric:

1. **Brand alignment** — does it express the voice and tokens from `.brand/`?
2. **Channel fit** — does it match the channel's native aesthetic, aspect ratio, length limits, and viewer attention pattern?
3. **Awareness stage match** — does it speak to the Schwartz awareness level the brief targeted (Unaware / Problem-Aware / Solution-Aware / Product-Aware / Most-Aware)?
4. **Message hierarchy** — does primary / secondary / proof come through in the right order?
5. **Creative quality** — composition, balance, typography, legibility, motion craft, audio (where applicable).
6. **A/B variation potential** — does this candidate offer a meaningfully different testable angle from the other winners, or is it a near-duplicate?

The output lands at `.marketing/selected/<channel>-<round>.md` with winners, rejected, cited rationale, and an iteration suggestion. The user then takes one of three exits: **accept** (lock the winner), **refine the brief** (adjust visual direction, tool mix, or per-tool prompts and regenerate), or **refine the positioning** (the misalignment is upstream of creative — go back and revise `.marketing/positioning/`).

## Why brief-and-judge for ads?

Four reasons, all of them mirroring brand's reasoning and all of them more pointed in the marketing context because ad creative is generated at much higher volume than brand identity work.

1. **Tool diversity.** The visual-AI landscape shifts quarterly. Nano Banana Pro leads static today; Veo 3.1 owns short-form video; Higgsfield owns camera moves; Midjourney owns stylized; Recraft owns vectors; Ideogram owns typography; Sora 2 owns cinematic. A plugin locked to one or two APIs freezes in 90 days. An ad campaign that wants 5 statics for Meta plus 3 reels for TikTok plus 1 hero video for YouTube wants to cross-pollinate across four tools in the same round. Briefs port across tools; API wrappers do not.

2. **Cost control.** Visual generation is metered. The user already has subscriptions across the tools they prefer. Putting the plugin beneath those subscriptions (instead of duplicating spend with plugin-held API keys) keeps the burn on the user's existing meters. The plugin separately holds a *spend safeguard* on the Google Ads side (Section 7 below) — that is a different problem and one where API-mediated control is essential.

3. **Multimodal LLM judgement is the right LLM use case.** Claude can read a dropped PNG, MP4, or GIF and reason about composition, attention path, brand expression, channel fit, and message hierarchy against a written brief. That is exactly where vision models add value — not as generators competing with specialist diffusion models, but as disciplined judges with a rubric and cited sources. Generation is a commodity; judgement is where the plugin differentiates.

4. **The user's taste is load-bearing.** This plugin's first user has explicit artistic instincts. Selection-with-rationale — not generation — is the plugin's job. The plugin amplifies the user's taste; it does not replace it.

The contrast with the anti-pattern is sharp. A "plugin calls API" design concentrates three failure modes: vendor lock-in, opaque cost, and the flattening of the user's taste into whatever the single chosen model happens to excel at this quarter. Brief-and-judge accepts a little more friction (the user copies prompts to tools) in exchange for a dramatically more durable architecture.

## Google Ads API wiring

This is where the marketing plugin does something `brand-plugin` never does: it talks to a paid third-party API and pushes real campaigns that, once enabled, will spend the user's money.

**The plugin DOES** — push campaign structures via the Google Ads API, upload offline conversions back to Google Ads (the killer feedback loop for `elocal_clone`'s pay-per-call routing engine), upload Enhanced Conversions for Leads, run dual-account suspension protection, enforce a bid-strategy ladder per Brad Geddes (Manual CPC → Maximize Clicks → Maximize Conversions → Target CPA → Target ROAS), and write a generated Python script the user runs on a cron to keep conversions flowing.

**The plugin DOES NOT** — push live campaigns without explicit user confirmation, ever. The contract is hard: *every* Google Ads API push lands campaigns in **PAUSED** state. Going live requires a separate `--enable` invocation and a fresh confirmation. There is no auto-enable, no "skip confirmation" config, no override flag for production pipelines. If the user wants automation, the user writes their own wrapper around `/marketing:ship-campaign --enable` and accepts the risk explicitly.

**Hard cost safeguards** enforced at push time (Section 7.5 of the spec):

- Sum of daily budgets ≤ declared monthly budget / 30. Overrun is blocked with a clear error.
- Always paused on first push. Enable is a separate, confirmed command.
- Max daily spend per single campaign capped at 40% of total. No single campaign eats the whole budget.
- Shared budgets require explicit opt-in.
- Pre-flight dry run prints the full intended state change and requires explicit confirmation.
- Weekly spend report flags overruns.
- Dual-account check refuses to push to a `SUSPENDED` account and warns the user.

These safeguards are non-negotiable. They live in `code/google_ads_client.py` as preconditions, not as config knobs.

Meta Marketing API, TikTok Ads API, and LinkedIn Ads API are stubbed in v0.1 — the structural shape exists in `code/meta_ads_client.py` so v0.2 can fill it in without changing callers. v0.1 ships Google Ads only because that is what `elocal_clone`'s Month 1 path requires.

## State ownership

All plugin output lives in `.marketing/` inside the **target project**, never inside the plugin directory. This matches `brand-plugin`'s `.brand/` and `greenfield-plugin`'s `.greenfield/` exactly.

- **Reentrant.** Every skill is idempotent on its inputs. Re-running `/marketing:paid` overwrites only `.marketing/paid/*`; it does not touch `.marketing/research/`, `.marketing/positioning/`, `.marketing/candidates/`, `.marketing/selected/`, or `.marketing/decisions/`. Partial workflows resume cleanly.
- **Per-sub-vertical subdirectories.** `.marketing/{paid,seo,lifecycle,positioning,analytics}/` each hold the lead's outputs. `.marketing/research/` holds the researcher memos. `.marketing/briefs/`, `.marketing/candidates/`, `.marketing/selected/`, `.marketing/decisions/` are shared by all channels.
- **Git-committable.** The user commits `.marketing/` and treats it as project source of truth. The plugin itself is read-only from the project's perspective.
- **Composable.** Sibling plugins read from `.marketing/` without coupling to the plugin's internals. If the plugin is uninstalled, the project's `.marketing/` directory still holds the campaign blueprint.

See `docs/workflow.md` for the full directory tree.

## Framework-tier discipline

Every cited reference in `knowledge/` is labelled with one of three tiers. This exists to prevent framework-citation theater — the habit of salting output with big-name references to look rigorous while the underlying reasoning is unchanged. The tiers are borrowed wholesale from `brand-plugin` and apply identically here.

- **`tier: evidence`** — the load-bearing ones. Kohavi/Tang/Xu experimentation math. Wordstream 2025 Home Services Benchmarks. Google Ads API documentation. Eugene Schwartz's awareness levels (treated as evidence because the empirical case for funnel-stage matching is strong). Cialdini's six weapons of influence (treated as evidence with minor caveats; the underlying experiments replicate). If an agent cites an `evidence` source, the claim stands or falls on the source being correct.
- **`tier: scaffolding`** — forcing functions. April Dunford's 10-step positioning process. Brian Balfour's growth-loop taxonomy. Brad Geddes's bid-strategy ladder. Demand Curve's creative-testing cadence. These are disciplines the agent follows to structure its thinking; they shape the output's shape more than its content.
- **`tier: vocabulary-only`** — conceptual labels the agent uses to communicate, without treating them as predictive models. StoryBrand's seven-part framework. AIDA. Most "growth hacking" frameworks. These are useful shared vocabulary between the agent, the user, and downstream humans, but they should not be cited as if they predict consumer behavior.

Agents carry the tier forward when they cite. A creative brief that says "target audience: solution-aware (Schwartz, *Breakthrough Advertising* — tier: evidence)" is honest about what work the citation is doing. A creative brief that says "narrative arc: hero's journey (Campbell — tier: vocabulary-only)" is honest that the framework is communicative scaffolding, not predictive science.

See `knowledge/README.md` for the full tier catalog.

## Composition with sibling plugins

`marketing` sits downstream of `brand` and `greenfield`, parallel to `sales`. It composes via file boundaries; never cross-writes.

- **`brand-plugin`** — reads `.brand/voice.md` and `.brand/tokens.json`. The `creative-ops` agent enforces voice on every copy variant and pulls colors and type tokens into every creative brief. Reads `.brand/logo/`, `.brand/wordmark.svg`, and `.brand/motion/` as locked assets that creative briefs reference. Writes A/B winners back to `.brand/export-kit/ads/{campaign}/{variant_id}/` so the brand plugin can later bless them as canonical — this is the only write outside `.marketing/`, and it is governed by an explicit flag in `.marketing/context.md`.

- **`sales-plugin`** — provides leads to `.marketing/leads/inbound-{date}.csv`, which the sales-plugin's importer consumes. Reads back `.sales/closed-lost.md` and `.sales/outcomes/closed-won-{date}.csv` to feed `analytics-experimentation-lead`'s attribution model — a lead only counts as a marketing conversion if sales actually closes it, not at form-fill time. This is the marketing-qualified vs sales-qualified loop.

- **`greenfield-plugin`** — reads `.greenfield/data-model.md` and `.greenfield/research/data-architecture.md` to know which events the application already instruments, then writes `.greenfield/events.yaml` (the marketing event taxonomy) so greenfield's scaffolder can instrument them at build time. This is the plugin's most interesting bi-directional integration: marketing and greenfield can run in either order and the events.yaml file converges.

If a sibling is absent, `marketing` runs in a degraded mode with explicit warnings — never silently. If `.brand/` is missing, `creative-ops` warns that voice is unenforced and offers to create a minimal `voice.md` on the fly while telling the user the brand plugin should be run for a proper definition.

## Why 12 agents

`brand-plugin` has 6. `greenfield-plugin` has 9. This plugin has 12: one director plus five lead-and-researcher pairs plus one shared creative-ops. The size is justified, not casual.

The five sub-verticals each represent a genuinely independent expertise. A paid-acquisition lead and an SEO lead read different sources, follow different frameworks, optimize different metrics, and break in different ways. Collapsing two sub-verticals into one agent loses the research-freshness advantage and collapses back into the "generic AI marketing assistant" category this plugin is trying to escape.

Why each sub-vertical needs *both* a lead and a researcher is the harder question. The split mirrors how real marketing teams work: one person acts on knowledge, a different person keeps the knowledge fresh. The researcher's job is **not** to write strategy; it is to fetch the most recent state of the domain from named sources and stamp the memo with the fetch date. The lead reads the researcher's memo and writes the strategy. Splitting them keeps two failure modes apart: stale knowledge (researcher's job to prevent) and bad reasoning over fresh knowledge (lead's job to prevent). Collapsing them risks both failures collapsing into the same agent's context window.

`marketing-director` is the reconciler — the only agent allowed to read all five sub-vertical outputs at once. It surfaces contradictions explicitly (Paid says target problem-aware, Positioning says target solution-aware) and writes ADRs for every resolved contradiction.

`creative-ops` is shared because creative cuts across sub-verticals — Paid needs it heavily, Lifecycle needs email visuals, the others need it occasionally. It operates in two modes (brief mode and selection mode) from a single agent file, mirroring `brand-plugin`'s `creative-director` precedent. See `docs/agent-roster.md` for the two-mode discussion.

`brand-plugin`'s `agent-roster.md` warns: do not add an agent that "re-frames an existing charter." This plugin honors that discipline. An earlier draft considered splitting `creative-ops` into `copy-ops` and `visual-ops`. Those collapsed cleanly — the same taste model that scores headlines also scores hero images, and splitting them would duplicate the brand-voice context in two system prompts. Twelve is the floor, not the ceiling, but every additional agent must justify itself against the same rule.
