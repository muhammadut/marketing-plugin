---
title: "Google Ads API — Conversion Management, Enhanced Conversions for Leads, and Data Manager API"
author: Google for Developers
year: 2026
type: docs
tier: evidence
url: https://developers.google.com/google-ads/api/docs/conversions/overview
sub-vertical: paid
cited-by-agents: [paid-acquisition-lead, paid-acquisition-researcher, marketing-director]
---

# Google Ads API — Conversions and Enhanced Conversions for Leads

## One-line summary
The official Google Ads API documentation for pushing campaigns programmatically and uploading offline conversions (closed calls / billed jobs) back to Google Ads via Enhanced Conversions for Leads — the load-bearing API surface for elocal_clone's paid acquisition program.

## Why this tier
Evidence. This is Google's own normative documentation for how to integrate. Every claim here is checkable against developers.google.com and every API constraint is enforced server-side. The reason it is load-bearing for the elocal_clone project specifically: the project's value proposition to the paid acquisition program depends on uploading **call-billed** events from the Twilio routing engine back to Google Ads as offline conversions, so Google's bid strategies (Max Conversions, tCPA, Maximize Conversion Value) optimize toward billed calls instead of form-fills. Without this loop the bidder is flying blind. Decay note: Google Ads API has annual deprecation cycles (current API version v21 as of late 2025); the paid-acquisition-researcher must reverify endpoints and field names every quarter, and Google announced February 2026 stricter conversion data requirements that any new build must comply with.

## Key concepts
- **Conversion management overview.** The API surface for creating ConversionAction resources, uploading ClickConversion objects, and querying conversion attribution. Documented at `developers.google.com/google-ads/api/docs/conversions/overview`.
- **Enhanced Conversions for Leads (ECfL).** The upgraded version of legacy "offline conversion import" — instead of relying solely on GCLID matching (which decays as cookies expire), ECfL accepts hashed first-party identifiers (email, phone) on the imported conversion record. Google then performs identity resolution against signed-in user data to recover attribution that GCLID alone would miss.
- **ClickConversion object.** The wire format for an offline conversion upload. Required fields include conversion_action (resource name), conversion_date_time, conversion_value, currency_code, and either a gclid OR (for ECfL) a user_identifiers list of hashed email/phone records.
- **Hashing requirement.** Emails must be lowercased, trimmed, and SHA-256 hashed before upload. Phone numbers must be normalized to E.164 format then SHA-256 hashed. Google rejects unhashed PII at the API boundary.
- **Data Manager API.** Google's recommended successor to the Google Ads API conversion endpoints for new offline conversion workflows. Provides a unified ingestion surface with better developer ergonomics and access to additional features like Customer Match upload alongside ECfL. Per Google: "we don't recommend implementing new offline conversion workflows using the Google Ads API" — new builds should target Data Manager API.
- **OAuth 2.0 + developer token.** Two credentials required: a Google Ads developer token (granted at the manager-account level) and an OAuth 2.0 refresh token (granted by the advertiser account on first authorization). Tokens have suspension risk if API requests violate policy — dual-account safety pattern is to maintain a sandbox manager account for testing and a production manager account for live spend, never share refresh tokens across the boundary.
- **February 2026 conversion data changes.** Google Ads API tightened required fields on imported conversions in February 2026; new builds must submit consent_status, ad_user_data, and ad_personalization signals on every ClickConversion or risk silent drops.

## Direct quotes (fair use, attributed)

1. "Enhanced conversions for leads is an upgraded version of offline conversion import that uses user-provided data, such as email addresses, to supplement imported offline conversion data to improve accuracy and bidding performance." — Google Ads Help, *About enhanced conversions for leads*, [support.google.com/google-ads/answer/15713840](https://support.google.com/google-ads/answer/15713840).

2. "Google recommends upgrading your offline conversions workflows to the Data Manager API for an improved developer experience and access to additional features. We don't recommend implementing new offline conversion workflows using the Google Ads API." — Google for Developers, *Manage offline conversions*, paraphrased from the documentation lead-in.

3. "Implementation involves configuring tagging, normalizing/hashing user data, populating ClickConversion objects with identifiers and details, and importing them via the API." — paraphrased from the *Upload Enhanced Conversions for Leads* code-sample documentation.

*(Quotes 2 and 3 are paraphrased rather than verbatim; the paid-acquisition-researcher should verify exact wording on the next refresh.)*

## When to cite
Cited by `paid-acquisition-lead` in `offline-conversion-spec.md` (which events to upload, with what cadence, and which ClickConversion fields to populate) and in `google-ads-api-wiring.md` (the integration-level spec the engineering side will implement). Cited by `paid-acquisition-researcher` when refreshing `paid-research.md` quarterly.

## Anti-citation guidance
Do not cite this as authority for choosing between Search, PMax, and Demand Gen campaign types — the API documents *how* to push campaigns of each type, not *which* type is right for the use case. Do not assume the API surface is stable across versions; cite the version (e.g., v21) when quoting field names. Do not cite this for legacy "offline conversion import" patterns when building new — Google has explicitly flagged Data Manager API as the path forward.
