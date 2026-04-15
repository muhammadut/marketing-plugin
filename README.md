# Marketing Plugin

**Five sub-verticals, twelve agents, one brief-and-judge architecture for ad creative.** The marketing plugin is organized like a small marketing org: a director, five sub-vertical leads, five sub-vertical researchers who keep their domains state-of-the-art, and a shared creative-ops agent that writes channel-specific creative briefs and judges returned candidates.

## What it does

`marketing` is a planning-and-execution plugin for the demand side of a business. It's organized into exactly five sub-verticals — **Paid Acquisition**, **SEO & Content**, **Lifecycle & Retention**, **Positioning & Messaging**, and **Analytics & Experimentation** — each with its own lead agent and a dedicated researcher. The `marketing-director` agent reconciles the five sub-verticals into one coherent master plan.

For elocal_clone specifically, **Paid Acquisition** is the load-bearing sub-vertical and the only one fully built for v0.1. The other four ship with skeleton agents and researchers ready to expand in v0.2. This is by design: the founder's biggest knowledge gap is upstream ads (he's a data scientist with downstream call-routing expertise), Month 1 of the year-one master plan calls for a $1k/month Google Ads ramp scaling to $210k/month by Month 12, and the plugin must first solve that.

Ad creative generation uses the **same brief-and-judge architecture as the brand plugin**. The plugin does NOT call image or video APIs. Instead, the `creative-ops` agent writes per-channel creative briefs the user takes to whichever external tools they prefer (Nano Banana Pro, Veo 3.1, Higgsfield, Midjourney, Recraft, Ideogram, Sora 2), generates 5-15 candidates per channel per round, drops them into `.marketing/candidates/<channel>-<round>/`, and runs `/marketing:select-creative`. The creative-ops agent reads the candidates with multimodal vision and scores against a channel-fit rubric. The user iterates.

## Why it exists

Most "AI marketing" tools are either generic ad-copy generators (template slop) or vendor-locked dashboards (Adobe Marketo and friends). This plugin is neither. It is a research-grounded marketing operator that produces evidence-cited recommendations the human can defend in a board meeting and that pushes real campaigns to live Google Ads accounts via API. Six rules:

1. **Five sub-verticals, hard boundaries** — Paid, SEO, Lifecycle, Positioning, Analytics. Each has a lead and a researcher. The marketing-director reconciles. No "AI marketing assistant" sprawl.
2. **Per-sub-vertical research** — each researcher continually refreshes its domain from named sources. Paid: Wordstream/LocaliQ, Demand Curve, Common Thread Collective, Google Ads docs. SEO: Ahrefs, Semrush, Backlinko, Eli Schwartz, Ethan Smith. Lifecycle: Val Geisler, Iterable/Klaviyo research. Positioning: April Dunford, Eugene Schwartz, Andy Raskin. Analytics: Kohavi, Brian Balfour, Reforge.
3. **Real Google Ads API wiring for paid** — OAuth, paused-first campaign push, Enhanced Conversions for Leads, offline conversion upload from the elocal_clone routing engine (call-billed → Google Ads), dual-account suspension protection, hard cost safeguards, explicit confirmation gates before any spend goes live.
4. **Brief-and-judge for creative** — never API-driven. The plugin writes briefs; the user generates externally across whatever visual AI tools they prefer; the plugin judges. Same architecture as the brand plugin.
5. **Framework-tier discipline** — every cited reference in `knowledge/` is labelled `tier: evidence` (load-bearing — Kohavi experimentation math, Wordstream 2025 home services benchmarks, Google Ads API documentation, Cialdini triggers, Schwartz awareness levels), `tier: scaffolding` (forcing function — Dunford 10-step positioning, growth-loop taxonomies, Mailchimp voice/tone split), or `tier: vocabulary-only` (most positioning mad-libs, "growth hacking" frameworks, ad-copy template libraries). Agents carry tiers forward when they cite.
6. **State lives in the target project** — same composition model as `brand-plugin` and `sales-plugin`. `.marketing/` in the project root with sub-vertical subdirectories. Reentrant skills.

## The 12 agents (1 director + 5 leads + 5 researchers + 1 shared creative-ops)

| Agent | Role | Sub-vertical |
|---|---|---|
| **marketing-director** | Reconciler — produces the master marketing plan integrating all 5 sub-verticals | (cross-cutting) |
| **paid-acquisition-lead** | Campaign structure, ad copy, bidding, offline conversion upload, dual-account safety | Paid Acquisition |
| **paid-acquisition-researcher** | Refreshes Wordstream/LocaliQ/Demand Curve/CTC/Google Ads landscape | Paid Acquisition |
| **seo-content-lead** | Keyword research, content calendar, on-page SOP, programmatic SEO | SEO & Content |
| **seo-content-researcher** | Refreshes Ahrefs/Semrush/Backlinko/Schwartz/Smith landscape | SEO & Content |
| **lifecycle-lead** | Email/SMS flows, onboarding sequence, winback, churn prevention | Lifecycle & Retention |
| **lifecycle-researcher** | Refreshes Geisler/Iterable/Klaviyo/Reforge landscape | Lifecycle & Retention |
| **positioning-lead** | ICP, competitive positioning, messaging hierarchy, awareness ladders | Positioning & Messaging |
| **positioning-researcher** | Refreshes Dunford/Schwartz/Raskin/Moore landscape | Positioning & Messaging |
| **analytics-experimentation-lead** | Event taxonomy, dashboards, experimentation framework, growth loops | Analytics & Experimentation |
| **analytics-experimentation-researcher** | Refreshes Kohavi/Reforge/Balfour/PostHog landscape | Analytics & Experimentation |
| **creative-ops** | Two-mode (brief mode writes channel-specific creative briefs; selection mode reads candidates and scores) | Shared utility |

## Workflow

```
empty dir
   ↓
/marketing:init       →  interview, define objective, pick sub-verticals in scope
/marketing:research   →  all 5 researchers run in parallel
/marketing:plan       →  marketing-director reconciles into master plan
/marketing:positioning →  positioning-lead produces positioning + messaging hierarchy
/marketing:paid       →  paid-acquisition-lead produces campaign structure + creative briefs
   ↓
   user generates externally (Nano Banana Pro, Veo 3.1, Higgsfield, Midjourney, Recraft…)
   user drops candidates into .marketing/candidates/<channel>-<round>/
   ↓
/marketing:select-creative <channel> <round>
                     →  creative-ops scores candidates, writes selected/<channel>-<round>.md
   user reviews and decides:
      • /marketing:paid --accept-creative <channel>-<round> --winner <filename>
      • /marketing:paid --refine-brief --channel <channel>
   ↓
/marketing:ship-campaign  →  paid-acquisition-lead pushes the campaign to Google Ads (paused-first, then user confirms going live)
   ↓
/marketing:seo / /marketing:lifecycle / /marketing:analytics  →  v0.2 sub-verticals
/marketing:status     →  state reporter (any time, reentrant)
```

Active plugin time for the v0.1 paid acquisition workflow: ~90-180 minutes plus user-driven creative generation time.

## Composition with sibling plugins

- **`brand`** — reads `.brand/voice.md` and `.brand/tokens.json` so ad copy and creative briefs are in-voice and on-style. Locked logos and motion reels in `.brand/logo/` and `.brand/motion/` are referenced by creative briefs.
- **`sales`** — receives inbound waitlist leads from `.marketing/leads/` for outbound sequences; sales pushes closed/lost feedback back into `.marketing/attribution/`.
- **`greenfield`** — reads `.greenfield/data-model.md` to know which events exist for attribution; writes event taxonomy into `.greenfield/events.yaml` so the app instruments them at build time.

This plugin reads from `.brand/`, `.sales/`, `.greenfield/` if present, never writes outside `.marketing/`.

## State directory

All output lives in `.marketing/` in the target project. Per-sub-vertical organization:

- `plan.md` — the master plan
- `paid/` — campaign structures, creative briefs, ship logs
- `seo/` — keyword research, content calendar (v0.2 stubbed)
- `lifecycle/` — email flows (v0.2 stubbed)
- `positioning/` — positioning statement, messaging hierarchy
- `analytics/` — event taxonomy, experiment registry
- `briefs/` — per-channel creative briefs
- `candidates/<channel>-<round>/` — user-dropped externally generated assets
- `selected/<channel>-<round>.md` — creative-ops scoring + winners + rationale
- `decisions/<channel>.md` — locked creative picks per channel
- `campaigns/` — live campaign state (Google Ads JSON snapshots)
- `experiments/` — A/B test registry

## Status

**v0.1.0** — first release. Twelve agents, eleven skills (init, research, plan, positioning, paid, seo, lifecycle, analytics, select-creative, ship-campaign, status), 23 knowledge framework extracts organized into six sub-vertical directories with tier annotations, brief-and-judge templates for ad creative, Google Ads API wiring patterns. **Paid Acquisition and Positioning are fully built (positioning is load-bearing for paid); SEO, Lifecycle, and Analytics ship with skeleton leads and researchers ready to expand in v0.2.** Iterate from real use on `elocal_clone` Track D (upstream call supply).

## License

MIT
