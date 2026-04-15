---
title: "Lean Analytics: Use Data to Build a Better Startup Faster"
author: Alistair Croll, Benjamin Yoskovitz
year: 2013
type: book
tier: scaffolding
url: https://www.oreilly.com/library/view/lean-analytics/9781449335687/
sub-vertical: analytics
cited-by-agents: [analytics-experimentation-lead, marketing-director]
---

# Croll & Yoskovitz — Lean Analytics

## One-line summary
The book that gave the early-stage startup community the discipline of "One Metric That Matters" per stage — picking one number that captures the most important question for the company right now, and reorganizing every dashboard, standup, and ritual around it.

## Why this tier
Scaffolding. Croll and Yoskovitz are operators (Croll built Coradiant; Yoskovitz built and sold multiple startups before joining Highline Beta), and the book is operator distillation, not academic research. The taxonomy of stages (Empathy → Stickiness → Virality → Revenue → Scale) and the per-stage OMTM (One Metric That Matters) recommendations are the authors' opinionated framework, not measured findings. What makes the framework load-bearing as scaffolding is the **discipline of picking one metric**: most startup dashboards have 30 metrics that mean nothing in aggregate, and the OMTM constraint forces a hard prioritization conversation that usually changes how the team works. The forcing function is the contribution.

## Key concepts
- **One Metric That Matters (OMTM).** Pick the single most important number for the company at this exact stage. Not a balanced scorecard; not a North Star plus three secondaries; one number, displayed prominently, owned by the founder. The OMTM changes as the company moves through stages.
- **The five stages.** Empathy (do customers have the problem?), Stickiness (do they keep coming back?), Virality (do they bring others?), Revenue (do they pay enough?), Scale (can the business grow profitably?). Each stage has different OMTM candidates.
- **Stage-appropriate metrics.** Stickiness stage: retention curves, DAU/MAU, repeat usage. Virality stage: K-factor, viral cycle time, organic share of new acquisitions. Revenue stage: CAC, LTV, payback period, contribution margin. Scaling too early to revenue or virality before stickiness is established is the most common failure mode.
- **The line in the sand.** Pre-commit to a numeric threshold for the OMTM that separates "good enough to move to the next stage" from "not yet." Without the line in the sand, teams move on to the next stage based on hope rather than data.
- **Six business model archetypes.** E-commerce, SaaS, free mobile app, media, user-generated content, two-sided marketplace. Each archetype has different OMTM defaults at each stage. (For elocal_clone, the relevant archetype is two-sided marketplace, which has supply-side and demand-side OMTMs that have to be balanced.)
- **Vanity metrics vs actionable metrics.** A vanity metric goes up and to the right and makes everyone feel good but doesn't change any decision. An actionable metric ties to a behavior the team can change. Total signups is a vanity metric; activated-this-week / signups-this-week is actionable.
- **Cohort analysis is non-negotiable.** Time-aggregate metrics (overall conversion rate, overall retention) hide everything; cohort analysis (conversion rate by signup week, retention curve by signup month) is the minimum bar for honest analytics.

## Direct quotes (fair use, attributed)

1. "The One Metric That Matters is the one number you care about most right now. It changes as you grow." — Croll & Yoskovitz, *Lean Analytics*, 2013, paraphrased from Chapter 6.

2. "If you cannot draw a line in the sand for what 'good enough' looks like before you start measuring, you have not picked a metric — you have picked a vibe." — paraphrase of *Lean Analytics* discipline framing.

3. "A vanity metric is a number that always goes up, that makes you feel good, and that doesn't change any decision. The opposite of a vanity metric is an actionable metric — one that ties directly to a behavior you can change." — paraphrase of *Lean Analytics* Chapter 2.

*(All three quotes are paraphrases of book content rather than verbatim; the analytics-experimentation-researcher should pull exact citations from the published edition.)*

## When to cite
Cited by `analytics-experimentation-lead` in `event-taxonomy.yaml` (the OMTM choice anchors what events the project actually needs to instrument) and in `dashboards.md` (the OMTM is the single hero number on the dashboard). Cited by `marketing-director` when sub-vertical leads are proposing dashboards with too many headline metrics — the One Metric discipline is the editor.

## Anti-citation guidance
Do not cite *Lean Analytics* as evidence that the five-stage taxonomy is a measured finding — it is the authors' opinionated framework, and many companies do not move through the stages in order. Do not cite the per-stage OMTM defaults as binding for every project — they are starting points that need to be adapted. Do not use the OMTM discipline to ignore the rest of the dashboard — the right interpretation is "one number gets the hero treatment," not "delete every other metric."
