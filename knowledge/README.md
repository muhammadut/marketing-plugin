---
title: "Knowledge Bundle — Marketing Plugin"
version: v0.1.0
---

# Knowledge Bundle

This directory is the marketing plugin's **bundled research foundation** — a curated set of framework extracts that the plugin's twelve agents cite from, so that no claim in the output artifacts (`plan.md`, `paid/campaign-structure.md`, `positioning/positioning.md`, `analytics/event-taxonomy.yaml`, `briefs/<channel>.md`, etc.) is hallucinated from training data.

**Rule:** agents cite from `knowledge/`, not from training data. If a framework is not in this directory, it is not citable. If a quote is not in the "Direct quotes" section of the relevant extract, it must not appear in a plugin output. This is not a style preference; it is a defensibility contract for a plugin that pushes real money to live ad accounts.

## The tier system

Every extract file carries a `tier:` field in its YAML frontmatter with one of three values. The tier is load-bearing: when an agent cites a framework, it carries the tier forward, so a human reader of the final `plan.md` can see at a glance whether a given recommendation is grounded in empirical evidence, a disciplinary scaffolding, or a shared vocabulary without predictive power.

### `tier: evidence`

The framework is either empirically grounded (controlled studies, replicated findings, large-n analyses, engineering math) or is a published platform specification with unambiguous normative language (Google Ads API docs, Meta Marketing API docs, current platform character limits). Citing an `evidence` source carries real weight — the claim it backs is defensible against a skeptical reviewer.

Examples in this bundle:
- `analytics-experimentation/kohavi-trustworthy-experiments.md` — Cambridge UP textbook from three principal authors who built and ran experimentation platforms at Bing, Google, LinkedIn. Engineering math, not opinion.
- `paid-acquisition/wordstream-localiq-home-services-2025.md` — n=3,211 home-services search campaigns, April 2024 to March 2025. Current empirical baseline for CPC, CTR, conversion rate.
- `paid-acquisition/google-ads-api-docs.md` — Google's own normative docs for the API surface and Enhanced Conversions for Leads.
- `paid-acquisition/meta-marketing-api-and-capi.md` — Meta's normative docs plus 2026 operator consensus on CAPI + Advantage+.
- `seo-content/ahrefs-state-of-seo.md` — Ahrefs' own backlink-graph studies at trillion-link scale.
- `lifecycle/klaviyo-iterable-research.md` — vendor benchmark studies at hundreds-of-millions-of-emails scale (the *numbers* are evidence; the strategy interpretation is scaffolding).
- `positioning/schwartz-5-awareness-levels.md` — sixty years of independent direct-response replication. Empirical observation about ad receptivity, not opinion.
- `analytics-experimentation/posthog-vs-growthbook-vs-statsig.md` — vendor pricing and feature facts (evidence) plus operator recommendations (scaffolding).
- `visual-ai/current-model-landscape-2026Q2.md` — evidence **with a decay clock**. Refreshed by the `paid-acquisition-researcher` on every `/marketing:research` run; stale after 90 days.
- `visual-ai/ad-creative-by-channel-best-practices.md` — character limits, aspect ratios, and runtime caps from each platform's own help center.

### `tier: scaffolding`

The framework does not predict outcomes on its own, but it forces the founder to do work they would otherwise skip. The artifact it produces is valuable even if the underlying theory is weak. Most of the classic positioning, paid-social, and lifecycle canon lives here — the books are not research, but they are disciplinary packaging that prevents lazy shortcuts.

Examples in this bundle:
- `paid-acquisition/marshall-ultimate-guide-google-ads.md` — Marshall's Campaign → Ad Group → Keyword → Ad → Landing Page hierarchy with 80/20 discipline.
- `paid-acquisition/demand-curve-growth-playbooks.md` — angle taxonomy and creative-testing cadence.
- `paid-acquisition/common-thread-collective-paid-social.md` — the Prophit System (anchor every ad decision to gross profit, not ROAS) and the bid-strategy ladder.
- `seo-content/schwartz-product-led-seo.md` — product as SEO asset, not blog as SEO asset.
- `seo-content/smith-graphite-programmatic-seo.md` — category page vs item page archetypes.
- `seo-content/backlinko-brian-dean.md` — Skyscraper Technique and on-page SEO checklist.
- `lifecycle/geisler-dinner-party-onboarding.md` — six-step onboarding metaphor.
- `lifecycle/eyal-hooked.md` — Hook Model (Trigger → Action → Variable Reward → Investment).
- `positioning/dunford-obviously-awesome.md` — 10-step positioning, competitive alternatives discipline. Cross-pollinated from brand-plugin with marketing application notes.
- `positioning/raskin-strategic-narrative.md` — Name the Change, Name the Enemy, Promise the Promised Land, Show Obstacles, Show Evidence.
- `positioning/moore-crossing-the-chasm.md` — beachhead segment discipline, whole product, references from people like me.
- `analytics-experimentation/balfour-growth-loops.md` — loops vs funnels, 4 Fits framework.
- `analytics-experimentation/croll-yoskovitz-lean-analytics.md` — One Metric That Matters per stage.

### `tier: vocabulary-only`

The framework sounds rigorous but does not predict outcomes. Its value is that it gives a team a **shared language** for things that would otherwise be argued about in vague terms. It is dangerous if treated as authority on customer behavior, because it is not that. Vocabulary-only citations MUST carry the tier tag forward so the reader of the marketing plan can see that the recommendation is vocabulary, not prediction.

The marketing-plugin v0.1 bundle contains no `vocabulary-only` extracts at this time. The most common candidates (Pirate Metrics AARRR, AIDA / PAS / FAB ad copy templates, generic "Forrester customer journey" maps, viral-coefficient math) are deliberately omitted from v0.1 — they would dilute the bundle and give agents a license to wave at vocabulary instead of doing the work. If a future v0.2 release adds them, they should be tagged honestly and the README should be updated to list them here.

## The 23 extracts in this bundle

### `paid-acquisition/`
1. `wordstream-localiq-home-services-2025.md` — evidence — n=3,211 home-services campaigns, 2024-2025 CPC/CTR/CVR baseline.
2. `google-ads-api-docs.md` — evidence — official API + Enhanced Conversions for Leads + Data Manager API.
3. `meta-marketing-api-and-capi.md` — evidence — Meta Marketing API + CAPI + Advantage+.
4. `marshall-ultimate-guide-google-ads.md` — scaffolding — Campaign → Ad Group → Keyword hierarchy + 80/20 + 100-click test.
5. `demand-curve-growth-playbooks.md` — scaffolding — angle taxonomy, kill-or-scale criteria, 3-5 angles/week cadence.
6. `common-thread-collective-paid-social.md` — scaffolding — Prophit System, bid-strategy ladder, 50% rule.

### `seo-content/`
7. `ahrefs-state-of-seo.md` — evidence — backlink-graph statistics at trillion-link scale.
8. `schwartz-product-led-seo.md` — scaffolding — product as SEO asset.
9. `smith-graphite-programmatic-seo.md` — scaffolding — category page vs item page archetypes.
10. `backlinko-brian-dean.md` — scaffolding — Skyscraper Technique + on-page SEO checklist.

### `lifecycle/`
11. `geisler-dinner-party-onboarding.md` — scaffolding — six-step onboarding metaphor.
12. `eyal-hooked.md` — scaffolding — Hook Model + B=MAT.
13. `klaviyo-iterable-research.md` — evidence (numbers) + scaffolding (strategy) — flow vs broadcast benchmarks.

### `positioning/`
14. `dunford-obviously-awesome.md` — scaffolding — 10-step positioning + competitive alternatives. Cross-pollinated from brand plugin.
15. `schwartz-5-awareness-levels.md` — evidence — Unaware → Problem-Aware → Solution-Aware → Product-Aware → Most-Aware ladder.
16. `raskin-strategic-narrative.md` — scaffolding — five-element strategic narrative.
17. `moore-crossing-the-chasm.md` — scaffolding — beachhead segment + whole product.

### `analytics-experimentation/`
18. `kohavi-trustworthy-experiments.md` — evidence — Cambridge UP, the definitive A/B testing text.
19. `balfour-growth-loops.md` — scaffolding — loops vs funnels, 4 Fits framework.
20. `croll-yoskovitz-lean-analytics.md` — scaffolding — One Metric That Matters.
21. `posthog-vs-growthbook-vs-statsig.md` — evidence (facts) + scaffolding (recommendations) — bootstrapper experimentation tool comparison.

### `visual-ai/`
22. `current-model-landscape-2026Q2.md` — evidence with decay clock — Nano Banana Pro, Veo 3.1, Higgsfield, Midjourney, Ideogram, Recraft, Sora 2 / Kling / Runway.
23. `ad-creative-by-channel-best-practices.md` — evidence — character limits, aspect ratios, hook windows by channel.

### `knowledge/` (top-level)
24. `README.md` — this file.

**Tier count:** 10 evidence (with 2 mixed evidence/scaffolding files), 11 pure scaffolding, 0 vocabulary-only. Total: 23 extracts.

## How agents should use this directory

1. **Read before citing.** When an agent needs a framework citation, it reads the relevant extract file in `knowledge/` first. It does not reach into training-data memory for quotes, page numbers, or framework details.

2. **Quote only from the "Direct quotes" section.** Every extract has a "Direct quotes" section with attributed, fair-use quotes (≤200 words each). Agents may paste these into output verbatim with attribution. Quotes outside that section are out of scope.

3. **Carry the tier forward.** When an agent cites a framework in `plan.md`, `positioning.md`, `campaign-structure.md`, `experiment-spec.md`, or any brief / selection file, the citation format must include the tier tag. Example:

   > "We allocate the Month 1 ad budget to Google Search at the Solution-Aware stage (Schwartz, *Breakthrough Advertising* 1966 — `tier: evidence`) using Single Theme Ad Groups (Marshall, *Ultimate Guide to Google Ads* — `tier: scaffolding`) and the LocaliQ 2025 home-services CPC of $7.85 (`tier: evidence`) as the upper bound for our manual-CPC test phase. The 4-Fits diagnostic (Balfour — `tier: scaffolding`) frames the kill criterion: if Channel-Model fit fails at three weeks, we re-plan, not re-bid."

   That is an honest citation. The reader knows at a glance which claims are research-grounded, which are operator scaffolding, and where the recommendation is taking interpretive risk.

4. **Refresh evidence-tier files on schedule.** `visual-ai/current-model-landscape-2026Q2.md`, `paid-acquisition/wordstream-localiq-home-services-2025.md`, `paid-acquisition/google-ads-api-docs.md`, `paid-acquisition/meta-marketing-api-and-capi.md`, `seo-content/ahrefs-state-of-seo.md`, `lifecycle/klaviyo-iterable-research.md`, `analytics-experimentation/posthog-vs-growthbook-vs-statsig.md`, and `visual-ai/ad-creative-by-channel-best-practices.md` all carry implicit decay clocks. The relevant researcher (`paid-acquisition-researcher`, `seo-content-researcher`, `lifecycle-researcher`, `analytics-experimentation-researcher`) refreshes them on every `/marketing:research` run. If a snapshot is older than 90 days, the agent must not use its numbers in any artifact that drives real money without revalidation.

5. **The canonical bundle is frozen per release.** Researchers can add new extracts during `/marketing:research` (writing to `.marketing/research/*.md` in the target project), but the canonical bundle in `knowledge/` is frozen per plugin release and only updated on plugin version bumps. This keeps the version contract tight: a `marketing-plugin@0.1.0` knowledge bundle is the same set of files for every project that pins to that version.

## How a reader of `plan.md` should use the tier tags

When reading the final marketing plan, look at the tier tag on every citation. A plan that leans heavily on `tier: scaffolding` citations has disciplined process but does not claim to predict outcomes — it is a forcing function on the founder, not a model of customer behavior. A plan with meaningful `tier: evidence` citations (Wordstream benchmarks, Kohavi experimentation math, channel platform docs) is the most defensible against a skeptical reviewer. A plan that contains `tier: vocabulary-only` citations (none in v0.1, but possible in later releases) should be read as expressing internal alignment rather than external defensibility on those points. The mix is up to the founder; the plugin's job is to make the mix legible.
