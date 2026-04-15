---
title: "Programmatic SEO Archetypes — The Ultimate Guide to SEO (Lenny's Podcast interview)"
author: Ethan Smith (Graphite)
year: 2023
type: playbook
tier: scaffolding
url: https://www.lennyspodcast.com/the-ultimate-guide-to-seo-ethan-smith/
sub-vertical: seo
cited-by-agents: [seo-content-lead, seo-content-researcher]
---

# Smith / Graphite — Programmatic SEO Archetypes

## One-line summary
Ethan Smith (founder of Graphite, an SEO consultancy known for taking marketplaces and SaaS products from zero to millions of organic sessions) frames programmatic SEO in terms of **two archetype shapes — category pages and item pages** — and argues that getting the archetype right is more important than any tactical SEO move.

## Why this tier
Scaffolding. Smith is an operator and consultant; the framework is distilled from running SEO programs at Thumbtack, Eventbrite, Ticketmaster, and many marketplace-shaped clients — but it is operator pattern-matching, not academic research. What makes it load-bearing for a project like elocal_clone (which is shaped like a directory marketplace at its core) is that it gives the founder a vocabulary to think clearly about the difference between a category template (Plumbers in Toronto), an item template (Mike's Plumbing — Toronto), and an editorial post (How to fix a leaky faucet) — and to make staffing, content, and crawl-budget decisions based on which archetype is doing which job.

## Key concepts
- **Category pages.** The "browse and discover" surface. URL pattern: `/plumbers/toronto`. Search intent: "find me options." Page job: list the items, surface filters, push the user toward a comparison decision. Internal link role: hub. Optimization levers: filter UX, item-count signaling, structured data (LocalBusiness, ItemList), curated subcategory cross-linking.
- **Item pages.** The "decide and convert" surface. URL pattern: `/plumbers/toronto/mike-plumbing`. Search intent: "tell me about this specific option." Page job: present the entity in depth, build trust, surface the conversion CTA. Internal link role: spoke. Optimization levers: rich entity data, social proof, schema (LocalBusiness, AggregateRating), unique content per item to avoid thin-page penalties.
- **The hub-and-spoke link graph.** Category pages link to item pages; item pages link back to their category and laterally to similar items; both link up to a city or region hub. The graph shape is the SEO unit — designing it deliberately is part of the product spec, not an afterthought.
- **Demand validation per template.** Before building a template, count the queries the template would target (volume × number of generated pages × expected CTR × expected conversion rate) to compute the upper bound of organic traffic. If the upper bound is small, the template is not worth building; if it's large, the template is the priority.
- **Thin-content risk.** Every generated page must have something that distinguishes it from its siblings — a unique listing set, unique reviews, unique data, unique copy. If two generated pages are word-for-word identical except for the variable, Google will treat them as duplicate / thin and de-index them.
- **Editorial vs programmatic vs technical SEO are different jobs.** Smith is explicit (echoing Schwartz) that the staffing model differs across these three. Programmatic SEO is closer to product engineering than to content marketing.
- **Indexation as a managed resource.** For large templates (millions of generated pages), forced indexation is wasteful — instead, ship the highest-priority subset, monitor what Google actually crawls and ranks, then expand outward from the proven tier.

## Direct quotes (fair use, attributed)

1. "Programmatic SEO is not 'AI content' — it's product. You're building a database-driven page template that becomes the answer to a class of queries." — paraphrase of Smith's framing on Lenny's Podcast, [lennyspodcast.com](https://www.lennyspodcast.com/the-ultimate-guide-to-seo-ethan-smith/).

2. "Get the archetype right and the SEO follows. Get it wrong and no amount of tactical optimization will save you." — paraphrase of Smith's "category page vs item page" framing.

3. "Every generated page needs a reason to exist that isn't just the variable in the URL. If two pages are functionally identical, Google will eventually merge them or drop them." — paraphrase of Smith's thin-content risk discussion.

*(All three quotes are paraphrases of podcast content rather than verbatim — the seo-content-researcher should pull exact transcript text from Lenny's Podcast when refreshing.)*

## When to cite
Cited by `seo-content-lead` in `programmatic-seo-blueprint.md` (the category vs item archetype is the structural starting point for any template-driven SEO plan) and in `keyword-research.md` (the demand-validation math sets the priority order on which templates to build first). Cited by `seo-content-researcher` as one of the canonical operator references for marketplace SEO.

## Anti-citation guidance
Do not cite Smith for editorial-content strategy — the framework is specifically about programmatic / template-driven SEO and doesn't apply cleanly to a single-product SaaS or a media business. Do not assume "build the template and they will come" — Smith is explicit that demand validation has to come first, and the most common failure mode is teams that build elaborate templates for queries no one searches.
