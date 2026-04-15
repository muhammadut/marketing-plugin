# Known Gaps — marketing-plugin v0.1.0

A running list of known limitations, deferred features, and reviewer-flagged items the v0.1.0 ship intentionally does not address. Update this file every release; do not silently fix items here without updating the spec or the release notes.

## Architectural by-design (not bugs)

These are *features* of the v0.1.0 architecture, captured here so a new reader does not mistake them for oversights.

- **Visual ad creative generation is human-driven, not API-driven.** The plugin writes per-channel creative briefs and judges returned candidates with multimodal vision; it never calls Nano Banana Pro, Veo 3.1, Higgsfield, Midjourney, Recraft, Ideogram, Sora 2, or any other image/video API directly. Reasons: tool diversity (the visual-AI landscape shifts quarterly), cost control (the user already has subscriptions on the tools they prefer), multimodal LLM judgement is the right LLM use case, the user's taste is load-bearing. See `docs/design.md` "Why brief-and-judge for ads" and spec §8. This is not a gap — it is the architecture.
- **Google Ads API push is paused-first, always.** Every `/marketing:ship-campaign` lands campaigns in PAUSED state. Live activation requires a separate `--enable` invocation and a fresh confirmation. There is no auto-enable, no "skip confirmation" flag, no override for production pipelines. This is by design and not a config knob.
- **No autonomous spend.** The plugin will never push a campaign to live state without explicit human confirmation. Users who want automation must wrap `/marketing:ship-campaign --enable` themselves and accept the risk explicitly.
- **State lives in the target project, not the plugin.** All output goes to `.marketing/` in the user's repo. The plugin itself is read-only from the project's perspective. Same composition model as `brand-plugin` and `greenfield-plugin`.

## v0.1 sub-vertical status

- **Paid Acquisition: fully built.** Lead, researcher, full knowledge base, full skill set (`/marketing:paid`, `/marketing:ship-campaign`), full Google Ads API wiring (auth, paused-first push, offline conversion upload, Enhanced Conversions for Leads, bid-strategy ladder, dual-account support, hard cost safeguards), creative-ops in both modes for paid channels.
- **Positioning: partial.** Lead and researcher exist, but the v0.1 implementation produces only what Paid Acquisition needs: `positioning.md` (one-pager), `awareness-ladder.md` (Schwartz 5-level mapping for ad copy variants), and a thin `messaging-hierarchy.md`. Full Dunford 10-step implementation, full strategic-narrative (Andy Raskin), and full competitive-alternatives matrix land in v0.2.
- **SEO and Content: stub.** Agent files and skill files exist; output is a thin memo citing the top 2 sources from the knowledge base and deferring tactics to v0.2 with `TODO(v0.2)` markers. Full keyword research, content calendar, programmatic SEO blueprint in v0.2.
- **Lifecycle and Retention: stub.** Same shape as SEO. Full Val Geisler dinner-party 6-step, retention flows, winback program, channel strategy in v0.2.
- **Analytics and Experimentation: stub.** Same shape as SEO. Full Kohavi-grade experimentation framework, event taxonomy generator, attribution model, dashboard specs, experiment backlog in v0.2.

The `marketing-director` reconciles whatever exists. In v0.1 it produces a thin master plan with one full sub-vertical (Paid) and four stub sub-verticals — still useful, just not complete.

## v0.2 deferrals

Features the v0.1 build deliberately stubbed or skipped, scheduled for the v0.2 sweep:

- **Full Positioning, Analytics, SEO, Lifecycle sub-verticals.** See above.
- **Meta Marketing API live push.** v0.1 ships `code/meta_ads_client.py` as a stub with the same interface shape as the Google Ads client. v0.2 implements the live push, with the same paused-first contract and the same Conversions API (CAPI) wiring for server-side event tracking.
- **TikTok Ads API and LinkedIn Ads API.** Stubbed to v0.2 or post-v0.2. v0.1 generates creative briefs for these channels but does not push.
- **Data Manager API as alternate backend for offline conversions.** Google's developer blog (March 2026) recommends Data Manager API for new workflows. v0.1 uses Google Ads API directly because the Python SDK is more mature; v0.2 adds Data Manager API as a pluggable backend behind the same `upload_conversion()` shim.
- **Ahrefs / Semrush API integration.** v0.1 SEO researcher reads blog posts and benchmark reports manually. v0.2 wires the APIs directly for keyword-difficulty and backlink data.
- **Customer.io / Klaviyo integration for lifecycle.** v0.1 lifecycle stub references the tools by name. v0.2 generates platform-specific flow definitions.
- **PostHog / GrowthBook / Statsig integration for analytics.** v0.1 analytics stub references the tools. v0.2 generates platform-specific experiment definitions.
- **Migration story for projects upgrading from v0.1 to v0.2.** Not designed yet. Document on v0.2 release.

## v1.0 deferrals

- **All five sub-verticals fully fleshed out.** The full `/marketing:plan` reconciliation only earns its keep when there are five real sub-vertical outputs to reconcile.
- **First live A/B test feedback loop.** creative-ops marks A/B winners and writes them back to `.brand/export-kit/ads/`. Requires Meta API integration and a working analytics-experimentation pipeline.
- **Automated experiment readout.** The analytics-experimentation-lead drafts the experiment, the user runs it, and the plugin pulls results and writes a structured readout in `experiments/{id}/results.md`.

## Permanent out-of-scope

These will never be in the plugin. Document here so reviewers don't propose them.

- **PR, media relations, analyst relations.** Use a dedicated tool.
- **Influencer marketing.** Use Aspire / Grin.
- **Event marketing and field marketing.** Out of scope.
- **Brand identity, logo design, brand voice authoring.** That is `brand-plugin`'s job. This plugin reads from `.brand/` but never writes a new brand voice.
- **Sales pipeline management, CRM, SDR sequences.** That is `sales-plugin`'s job. This plugin hands off `.marketing/leads/` and reads back closed-loop attribution.
- **Product analytics beyond marketing attribution.** The product team owns product instrumentation. The marketing plugin provides the event taxonomy spec, not the instrumentation.
- **Automated agent that spends money without human confirmation.** Refused. Every spend requires explicit `/marketing:ship-campaign --enable` confirmation.
- **MMM (media mix modeling).** Post-v1.0, maybe never. Requires a level of data volume most users won't have.

## Phase 4 fixes already applied

These were flagged by the Phase 3 spec-compliance reviewer and the plugin-validator and fixed before this v0.1.0 ship — listed here so the audit trail is complete:

- **Research output path mismatch resolved (CRIT-1).** The 5 researcher agents declared their outputs at `.marketing/research/<sub>-research.md` (Path A) but every skill dispatched them and the 5 sub-vertical leads + creative-ops + director all read from `.marketing/<sub>/research/state-of-<sub>.md` (Path B). This would have broken the entire research → lead handoff on first run. Phase 4 picked Path A (matches the agents and is simpler) and ran a 5-pattern sed substitution across the 7 affected skill files (marketing-research, marketing-paid, marketing-seo, marketing-lifecycle, marketing-positioning, marketing-analytics, marketing-status) to align them.
- **Knowledge directory rename (CRIT-2).** `knowledge/analytics-experimentation/` was the actual directory but every analytics agent + 2 templates referenced `knowledge/analytics/`. Phase 4 renamed the directory to `knowledge/analytics/` (matching the four other sub-verticals' single-word directory names: `paid-acquisition`, `seo-content`, `lifecycle`, `positioning`).
- **`creative-ops.md` decision-commit vocabulary fixed (4 places).** The agent file documented the decision-commit path as `/marketing:select-creative --accept-round <N> --channel <channel>` (a command that doesn't exist) — the actual command implemented by `marketing-paid` is `/marketing:paid --accept-creative <channel>-<round> --winner <filename>`. Also fixed the locked-winner destination from `.marketing/paid/creative/approved/<channel>/` (doesn't exist) to `.marketing/paid/creative-locked/<channel>/` (matches the marketing-paid skill).
- **`positioning-lead` skill expanded to write all 5 outputs.** The skill originally only wrote `positioning.md` and `messaging-hierarchy.md`, but `paid-acquisition-lead`, `creative-ops`, and `lifecycle-lead` all read `awareness-ladder.md`, `competitive-alternatives.md`, and `strategic-narrative.md`. Phase 4 expanded the dispatch prompt to instruct positioning-lead to write all five files. The `awareness-ladder.md` file is explicitly flagged as load-bearing for paid acquisition and creative-ops.
- **`code/google_ads_client.py` and `code/offline_conversion_uploader.py` stubs added.** The marketing-ship-campaign and marketing-paid skills referenced `marketing-plugin/code/google_ads_client.py` but the directory and file didn't exist. Phase 4 added stub Python files that document the contract surface, fail loudly with a clear error message when invoked (so the user knows the wrapper needs to be wired in), and provide a `dry_run_print_payload()` function the user can use to inspect what the campaign push WOULD send. The full wrapper is a v0.1.1 step.
- **README skill count fixed.** Said "ten skills" — actual count is eleven (init, research, plan, positioning, paid, seo, lifecycle, analytics, select-creative, ship-campaign, status). Updated to "eleven skills" with the full list.
- **`event-taxonomy.md` → `event-taxonomy.yaml` reconciled (5 files).** Some agents/skills referenced `.marketing/analytics/event-taxonomy.md` while others referenced `.yaml`. The actual template is `.yaml`. Phase 4 sed-fixed the references in marketing-paid SKILL, knowledge/README, knowledge/analytics/croll-yoskovitz-lean-analytics, docs/workflow, and docs/agent-roster to standardize on `.yaml`.

## Reviewer-flagged polish (deferred to v0.1.1)

Phase 3 reviewers flagged additional issues that are stylistic, cosmetic, or non-blocking. Accepted as-is for v0.1.0 and scheduled for the v0.1.1 sweep.

- **`code/google_ads_client.py` is a stub, not a working wrapper.** v0.1.1 should either implement the live wrapper using the `google-ads-python` SDK (currently 28.x as of April 2026) or document the manual integration steps in `docs/google-ads-setup.md`. v0.1.0 ships the contract surface so the skill references resolve; live push requires user to wire in their own credentials and SDK installation.
- **`docs/agent-roster.md` and `docs/workflow.md`** still show some old channel slugs (`google-pmax`, `meta-static`, `meta-reels`) and brief filenames without round suffixes (`brief-google-search.md` instead of `brief-google-search-1.md`). The actual canonical channel set is in `creative-ops.md` line 51 (`google-search`, `youtube-pre-roll`, `meta-feed`, `meta-stories`, `tiktok`, `linkedin-feed`, `display`). v0.1.1 reconciles the docs.
- **`marketing-seo`, `marketing-lifecycle`, `marketing-analytics` skills' Output filenames diverge from agent declarations.** E.g., `marketing-seo` writes `keyword-research.md` and `content-calendar.md` but `seo-content-lead` agent file says `keywords.md` and `calendar.md`. Same pattern in lifecycle (`onboarding-flow.md`/`winback-program.md` vs `flows.md`) and analytics (`experimentation-framework.md` vs `experiments.md`). v0.1.1 picks the agent declarations as canonical and updates the skill dispatch prompts.
- **`marketing-analytics` skill** reads `.greenfield/data-model.md`, but spec §9.3 and the analytics-lead agent file say `.greenfield/research/data-architecture.md`. v0.1.1 picks one.
- **`lifecycle-lead` reads `.marketing/analytics/event-taxonomy.yaml`** as a "critical" step, but analytics is a v0.1 stub that may not produce the file. v0.1.1 either declares `/marketing:analytics` as a hard prerequisite for `/marketing:lifecycle` or adds graceful-degradation language to lifecycle-lead.
- **`paid-acquisition-lead` has Bash in its tools list** but in v0.1 only writes specs (the actual API push is `marketing-ship-campaign`'s job). v0.1.1 may want to drop Bash from `paid-acquisition-lead` to enforce minimum-tool-surface.
- **No `color:` field on any of the 12 agents.** The plugin-validator flagged this as info-only. If Claude Code's runtime supports per-agent color rendering for multi-agent dispatches, v0.1.1 should add colors (e.g., paid-acquisition-lead: cyan, seo-content-lead: green, lifecycle-lead: yellow, positioning-lead: magenta, analytics-experimentation-lead: blue, creative-ops: red, marketing-director: white, researchers all dimmer variants).
- **Marketing-init interview question 4** asks which sub-verticals are in scope, but in v0.1 only Paid Acquisition + Positioning are fully built. The interview should note that SEO/Lifecycle/Analytics will run as v0.1 stubs regardless of the user's selection.
- **Skill `Task` dispatches use `subagent_type: general-purpose`** rather than the plugin's auto-discovered subagent types. This means agent frontmatter `tools:` and `model:` declarations become documentation rather than enforcement. v0.1.1 may switch to using each agent's own name as the subagent_type if Claude Code auto-discovery is wired up.

## How to update this file

When a v0.1.x or v0.2 release ships, move resolved items to a "Resolved in v0.X.Y" section at the bottom and add new gaps as they are discovered. Do not silently delete items — the change history is load-bearing for understanding why decisions were made.
