---
title: "Meta Marketing API, Conversions API (CAPI), and Advantage+ Campaigns"
author: Meta for Developers
year: 2026
type: docs
tier: evidence
url: https://developers.facebook.com/docs/marketing-apis/
sub-vertical: paid
cited-by-agents: [paid-acquisition-lead, paid-acquisition-researcher, creative-ops]
---

# Meta Marketing API + CAPI + Advantage+

## One-line summary
The official Meta API surface for programmatic ad campaigns, server-side conversion tracking that bypasses iOS14 attribution loss, and Meta's automated Advantage+ campaign type — the equivalent for the Meta side of the same offline-attribution loop the paid plan runs on Google.

## Why this tier
Evidence. Meta's own normative documentation, plus published 2026 best-practice consensus from operator publications (Foxwell Founders, SMC, Triple Whale) confirming that CAPI + Advantage+ is the current Meta meta. The reason it is paired with the Google Ads doc as load-bearing for elocal_clone: Meta is the secondary paid channel after Google Search in the Track D plan, and Meta's iOS14 attribution loss is unrecoverable without server-side CAPI integration. Without CAPI, Meta's optimization runs on roughly half the signal it should have. Decay note: Meta Marketing API has annual breaking changes; the paid-acquisition-researcher reverifies quarterly.

## Key concepts
- **Marketing API.** The programmatic surface for creating Campaigns → Ad Sets → Ads, managing budgets, querying insights, and uploading custom audiences. Documented at `developers.facebook.com/docs/marketing-apis/`.
- **Conversions API (CAPI).** Server-side event delivery that bypasses the browser entirely. CAPI events post directly from the advertiser's server to Meta's `https://graph.facebook.com/v{version}/{pixel-id}/events` endpoint with a hashed user_data block. CAPI is not a replacement for the Pixel — Meta recommends running both and deduplicating by event_id.
- **Event Match Quality (EMQ).** Meta's score (0-10) for how well a CAPI event payload can be matched to a Meta user. Higher EMQ = stronger optimization signal. EMQ above 8 correlates with materially better campaign performance. Achieve high EMQ by sending hashed email, hashed phone, hashed first/last name, ZIP, city, state, country, client_user_agent, client_ip_address, fbc (click ID), and fbp (browser ID) on every event when available.
- **Advantage+ Shopping Campaigns (ASC).** Meta's most automated campaign type. Replaces manual interest/demographic targeting with model-driven audience selection. Per published 2026 operator data (multiple sources), advertisers running Advantage+ Shopping with healthy CAPI integration see roughly 22% higher ROAS than manual setups with legacy pixel-only tracking. Caveat: the 22% number is operator-quoted and not independently verified — treat as directional, not a guarantee.
- **Advantage+ Audience.** A lighter-touch automation that lets the advertiser provide an audience suggestion (custom audience, lookalike, interests) and Meta automatically expands beyond it when the model finds higher-converting users.
- **Hashing requirement.** Same as Google: SHA-256 of normalized (lowercased, trimmed) values. Meta's official `business-sdk` libraries hash for you; raw API calls require the integrator to hash before transmission.
- **Pixel + CAPI deduplication.** Meta dedupes by matching `event_id` across the pixel-fired and server-fired versions of the same event. Send the same event_id from both surfaces or the same conversion will be double-counted.
- **iOS14 / ATT signal loss.** Apple's App Tracking Transparency framework forced opt-in pixel tracking on iOS in 2021. Pixel-only tracking lost roughly 40-60% of conversions for many advertisers. CAPI restores most of that loss for users who took an action that hit the advertiser's server (form-submitted, called, completed checkout).

## Direct quotes (fair use, attributed)

1. "Use Pixel + CAPI together; redundant tracking improves reliability when properly deduplicated. Maximize event data quality by sending hashed customer information (with consent), accurate timestamps, and consistent event naming. An EMQ score above 8 typically correlates with stronger campaign performance." — paraphrased consensus from 2026 operator guides on Meta CAPI implementation (multiple sources).

2. "Advertisers utilizing Advantage+ Shopping tools alongside a healthy CAPI integration see an average 22% higher ROAS compared to those relying on manual setups and legacy tracking." — paraphrased from 2026 operator commentary; treat as directional, not as Meta's published figure.

3. "Conversions API bypasses browser restrictions, ad blockers, and iOS privacy limitations." — paraphrased from Meta for Developers, Conversions API overview.

*(All three quotes are paraphrases rather than verbatim from Meta's own documentation; the paid-acquisition-researcher should pull verbatim text on the next refresh.)*

## When to cite
Cited by `paid-acquisition-lead` in `offline-conversion-spec.md` for the Meta CAPI side of the loop, in `campaign-structure.md` when proposing Advantage+ Shopping or Advantage+ Audience, and in `creative-ops` briefs when generating Meta-format creative (because Advantage+ creative auto-optimization changes what the brief should ask for).

## Anti-citation guidance
Do not cite the "22% higher ROAS" figure as if it were a Meta-published number — it is operator commentary and the actual lift varies enormously by category, audience size, and creative quality. Do not assume CAPI alone fixes attribution — it only recovers signal for users who hit the advertiser's server, which excludes view-through and pixel-only browse traffic. Do not use Advantage+ Shopping for **lead-gen / pay-per-call** without testing — the campaign type was originally built for e-commerce and home-services lead gen has historically performed better on standard Sales Objective with manual ad-set structure plus CAPI.
