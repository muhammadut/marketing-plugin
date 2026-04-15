# Google Ads Campaign Blueprint — <campaign-slug>

Generated-by: paid-acquisition-lead
Depends-on: .marketing/context.md, .marketing/research/paid-research.md, .marketing/positioning/positioning.md, .marketing/positioning/awareness-ladder.md, .marketing/paid/budget-plan.md, .brand/voice.md
Sources-cited: <comma-separated knowledge/paid-acquisition/ files this blueprint quotes — e.g., perry-marshall-80-20.md, geddes-bid-strategy-ladder.md, wordstream-home-services-benchmarks.md>

This file is the canonical Google Ads campaign blueprint. The `paid-acquisition-lead` writes it; `/marketing:ship-campaign` reads it and pushes it via the Google Ads API. Every field below maps to a Google Ads API entity field. Cost safeguards in section 8 are enforced at push time and cannot be bypassed in v0.1.

## 1. Campaign metadata

| Field | Value |
|---|---|
| Campaign name | <e.g., `ca-on-hamilton-plumbing-emergency`> |
| Campaign type | <Search | Performance Max | YouTube | Display | Discovery | Call-only> |
| Campaign objective | <Leads | Sales | Website Traffic | Calls | App Promotion> |
| Network | <Search Network only | Search + Display | YouTube only — per type> |
| Account ID | <Google Ads customer ID, 10-digit, dashes optional> |
| Account label | <`primary` | `secondary` — keyed in `.marketing/.secrets/google-ads.yaml`> |
| Dual-account safety flag | <`independent` | `paired-with-<other-campaign-slug>` — see §8 dual-account section> |
| Created | <ISO-8601 timestamp filled in by `/marketing:ship-campaign`> |
| Status on push | **PAUSED** (always — hardcoded, not configurable) |

## 2. Budget and bidding

| Field | Value |
|---|---|
| Daily budget | <e.g., $17 CAD/day = ~$510/month> |
| Monthly budget cap (declared) | <copy from `.marketing/paid/budget-plan.md`> |
| Bidding strategy | <Manual CPC | Maximize Clicks | Maximize Conversions | Target CPA | Target ROAS> |
| Bid strategy stage (Geddes) | <Stage 0 cold start | Stage 1 calibration | Stage 2 conversion ramp | Stage 3 tCPA | Stage 4 tROAS> |
| Stage entry criterion | <e.g., "<30 conversions in last 30 days — fits cold-start"> |
| Stage exit criterion | <e.g., "≥30 conversions + CPC stabilizing → advance to Stage 1"> |
| Hard daily ceiling | <set to ≤ 40% of total daily spend across all live campaigns; enforced at push> |
| Target CPA (if Stage 3+) | <CAD value, derived from observed 30-day average> |
| Target ROAS (if Stage 4) | <decimal, e.g., 3.0 = $3 revenue per $1 spend> |

Cite Brad Geddes "Advanced Google AdWords" for the bid-strategy ladder reasoning (tier: scaffolding) and the Wordstream / LocaliQ home services benchmark (tier: evidence) for the CPA target.

## 3. Targeting

| Field | Value |
|---|---|
| Geographic targets | <e.g., Hamilton ON, Burlington ON, Stoney Creek ON, Ancaster ON — list explicit cities, not provinces> |
| Geo target type | <Presence | Presence or Interest — per Google Ads "advanced location options"> |
| Negative geo targets | <e.g., excluded postal codes outside service area> |
| Languages | <English | French | English + French — per project bilingual policy> |
| Device targeting | <Mobile / Desktop / Tablet — with bid modifiers if applicable> |
| Schedule | <e.g., "24/7 for emergency home services" or "Mon-Fri 7am-9pm + Sat 8am-6pm for non-emergency"> |
| Audience signals (PMax / Discovery only) | <list — in-market, affinity, custom audiences, customer match> |

For elocal_clone Hamilton emergency plumbing: 24/7 schedule, mobile bid modifier +20%, presence-only geo (not "interest" — non-residents searching from elsewhere are noise).

## 4. Ad groups

One section per ad group. Each ad group has a single tight theme (Perry Marshall 80/20 — tier: scaffolding — every ad group should be answerable as "what specifically is this ad group about?"). Aim for 3-7 ad groups per campaign.

### Ad group: <ad-group-slug>

**Theme:** <one sentence — e.g., "Emergency plumber searches in Hamilton with 'now' or 'tonight' modifiers">

**Awareness stage targeted (Schwartz):** <Problem-Aware | Solution-Aware | etc.>

**Default max CPC bid:** <CAD value if Manual CPC>

**Keywords (exact match):**
```
[emergency plumber hamilton]
[plumber hamilton now]
[24 hour plumber hamilton]
...
```

**Keywords (phrase match):**
```
"emergency plumber hamilton ontario"
"plumber hamilton tonight"
...
```

**Keywords (broad match — only if Smart Bidding stage 2+):**
```
emergency plumbing hamilton
burst pipe hamilton plumber
...
```

(For elocal_clone: keep broad match minimal until Stage 2; broad match without conversion data wastes spend per Perry Marshall §4.)

**Ad-group-specific negatives:**
```
-diy
-how to
-youtube
-cheap
```

(Cite `paid/keywords/<campaign-slug>.csv` for the full keyword export. The CSV is the source of truth; this template is the human-readable overlay.)

**Master negative list reference:** `.marketing/paid/keywords/negatives-master.csv`

### Ad group: <next-ad-group-slug>

(repeat for each ad group)

## 5. Ads

One section per ad group above.

### Ad group: <ad-group-slug>

**Ad type:** <Responsive Search Ad (RSA) | Call-only Ad | Image Ad | Video Ad>

For Search campaigns, use Responsive Search Ads. For elocal_clone home services pay-per-call, **Call-only Ads** are non-optional — the click directly initiates a phone call, GCLID is captured, and the routing engine attributes the call to the ad.

**Headlines (RSA — 15 required):**

1. <Headline 1, ≤30 chars, primary message>
2. <Headline 2, ≤30 chars, geographic specificity — "Hamilton Plumber">
3. <Headline 3, ≤30 chars, urgency — "Emergency Response 24/7">
4. <Headline 4, ≤30 chars, proof — "Licensed & Insured">
5. <Headline 5, ≤30 chars, CTA — "Call Now">
6. <Headline 6, ≤30 chars, awareness-stage-specific copy from creative-ops>
7. <Headline 7>
8. <Headline 8>
9. <Headline 9>
10. <Headline 10>
11. <Headline 11>
12. <Headline 12>
13. <Headline 13>
14. <Headline 14>
15. <Headline 15>

(Google rotates these; pin only headlines that MUST appear in position 1 — typically the brand name or primary value prop. Pinning more than 2-3 reduces RSA optimization.)

**Descriptions (RSA — 4 required):**

1. <Description 1, ≤90 chars>
2. <Description 2, ≤90 chars>
3. <Description 3, ≤90 chars>
4. <Description 4, ≤90 chars>

**Display URL paths:**
- Path 1: <≤15 chars, e.g., "Hamilton">
- Path 2: <≤15 chars, e.g., "Emergency">

**Final URL:** <full https URL to landing page>

**Final URL suffix (tracking):** <`gclid={gclid}&utm_source=google&utm_medium=cpc&utm_campaign=<campaign-slug>&utm_content=<adgroup-slug>` or equivalent>

**Sitelinks (4-6 recommended):**
- <Sitelink 1: e.g., "24/7 Emergency Service" → /emergency-plumber-hamilton>
- <Sitelink 2: "Drain Cleaning" → /drain-cleaning>
- <Sitelink 3: "Water Heater Repair" → /water-heater-hamilton>
- <Sitelink 4: "Pricing & Quotes" → /pricing>

**Callouts (4-10):**
- <Callout 1: e.g., "Licensed & Insured">
- <Callout 2: "Free Estimates">
- <Callout 3: "30-Min Response">
- <Callout 4: "Senior Discount Available">

**Structured snippets:**
- Header: <Services | Brands | Models — pick one>
- Values: <up to 10, e.g., "Drain Cleaning, Water Heater, Sump Pump, Burst Pipe, Toilet Repair">

**Call extension:** <phone number — for elocal_clone, this is the routing-engine tracking number for this specific ad group>

## 6. Conversion tracking

Conversion actions tied to this campaign. Cite [Manage offline conversions | Google Ads API](https://developers.google.com/google-ads/api/docs/conversions/upload-offline) (tier: evidence).

| Conversion action name | Type | Counting | Attribution | Value |
|---|---|---|---|---|
| Billed Call | Imported (offline) | One per click | Last-click | <CAD per call, e.g., $25> |
| Qualified Call | Imported (offline) | One per click | Last-click | $0 (secondary signal) |
| Disputed Call | Imported (negative — RETRACTION) | One per click | n/a | $0 |
| Phone Call (>60s) | Phone calls from ads | One per click | Last-click | $0 (proxy until offline conversions kick in) |

**Primary optimization target:** "Billed Call" — Smart Bidding optimizes for this once Stage 2+ kicks in.

**Enhanced Conversions for Leads:** enabled. Hashed phone number + email uploaded with each offline conversion when GCLID is unavailable. Cite [Upload Enhanced Conversions for Leads](https://developers.google.com/google-ads/api/samples/upload-enhanced-conversions-for-leads) (tier: evidence).

**Offline conversion upload script:** generated at `.marketing/paid/scripts/upload-offline-conversions.py`. Cron cadence: every 4 hours. Reads from the routing engine's call event store, dedupes by GCLID + conversion_action_id + conversion_date_time.

## 7. Pause-first deployment

This blueprint will be pushed to the Google Ads API by `/marketing:ship-campaign` in **PAUSED state**. The plugin will:

1. Validate this file parses and references all referenced CSVs and briefs.
2. Run pre-flight cost safeguards (section 8).
3. Print the full intended state change for human review.
4. Wait for explicit "push" confirmation.
5. Create all entities via `MutateOperation` batches in the Google Ads API.
6. Verify all entities created in PAUSED status.
7. Print the created entity IDs.
8. Write the campaign snapshot to `.marketing/campaigns/live/<campaign-id>.yaml`.

Going live requires a separate `/marketing:ship-campaign --enable` invocation with a fresh confirmation. There is no auto-enable flag in v0.1 and no plan to add one.

## 8. Cost safeguards

Hard rules enforced at push time. The plugin REFUSES to push if any of these fail.

- [ ] **Daily budget within monthly cap.** Sum of daily budgets across all live + about-to-push campaigns ≤ declared monthly budget / 30. Calculated from `.marketing/paid/budget-plan.md`.
- [ ] **Single-campaign cap.** This campaign's daily budget ≤ 40% of total daily spend across all live campaigns.
- [ ] **Account not suspended.** Google Ads API `customer.status` is not `SUSPENDED`. If suspended, push refuses and warns the user.
- [ ] **Developer token approved.** Token has been approved for the customer account. Plugin prints a clear error if not.
- [ ] **OAuth refresh token valid.** Plugin attempts a no-op API call before any mutation; if auth fails, refuses to mutate and prompts re-OAuth.
- [ ] **Geo targets all valid.** Each city/region resolves via the Google Ads `geo_target_constant` lookup. Invalid targets refuse the push with a list of which targets failed.
- [ ] **Schedule does not exceed 168 hours/week.** Sanity check.
- [ ] **No bid floor below the Wordstream benchmark for this vertical.** Floor at 30% below benchmark CPC. (Cite `paid-research.md` for the benchmark value.)
- [ ] **Alert threshold set.** Daily spend > 90% of daily budget triggers a `marketing-status` alert in the next status run.

| Rule | Status | Notes |
|---|---|---|
| <each rule above with a check on push>| ✓ / ✗ | <error message if failed> |

## 9. Dual-account suspension protection

Per [[06-call-supply-strategy]] dual-account structure. The plugin supports running parallel campaigns across two accounts (`primary` and `secondary`) to reduce single-policy-review-suspension risk.

| Field | Value |
|---|---|
| Push to | <`primary` | `secondary` | `both`> |
| Paired campaign slug (if `both`) | <other campaign slug> |
| Ad-copy variation between accounts | <required if `both`; cite which variants are used per account from `.marketing/paid/creative/copy-variants/`> |

When pushing to `both`, the plugin creates parallel campaigns with slightly varied ad copy from the creative-ops variant library so the two accounts don't have identical footprints. If one account is detected as `SUSPENDED` at any point, the plugin logs a warning, refuses to push to it, and continues with the other.

## 10. Approval gate

Before going live, the user must:

- [ ] Read `/marketing:ship-campaign`'s dry-run output in full
- [ ] Confirm the daily budget, the bid strategy stage, and the target geos
- [ ] Confirm the push completed in PAUSED state by checking `campaigns/live/<campaign-id>.yaml`
- [ ] Log into the Google Ads UI and visually confirm campaign structure, ad copy, keywords, and budget all look correct
- [ ] Run `/marketing:ship-campaign --account <acct> --enable` with explicit confirmation

**No campaign goes live without this gate. There is no override.** Cite `docs/known-gaps.md` "no autonomous spend" rule.

The user is the only entity that can flip a campaign from PAUSED to ENABLED via this plugin in v0.1. This is a load-bearing safety property.
