---
title: "Current Visual-AI Model Landscape — 2026 Q2 Snapshot (Marketing Plugin Copy)"
author: marketing-plugin bundle (default snapshot, refreshed by paid-acquisition-researcher and creative-ops)
year: 2026
type: playbook
tier: evidence
url: https://blog.google/innovation-and-ai/products/nano-banana-pro/
sub-vertical: visual-ai
cited-by-agents: [creative-ops, paid-acquisition-lead, paid-acquisition-researcher]
---

# Visual-AI Model Landscape — 2026 Q2 (Marketing Plugin Copy)

## One-line summary
A snapshot of leading image and video models the `creative-ops` agent references when writing per-tool creative briefs for ad creative — evidence-tier for pricing/specs at the time of writing, but explicitly decaying. The marketing plugin maintains its own copy because creative-ops cites from this file when writing channel-specific ad-creative briefs; the marketing plugin must not be coupled to the brand plugin's bundle for live-spend creative work.

## Why this tier
Evidence **with a known decay rate**. Every number in this file — pricing, reference-image count, native resolution — is a fact at the moment of writing. But the visual-AI landscape moves every quarter, and "evidence" that is 12 months old may be wrong by a factor of 2 in any direction. The plugin enforces a refresh protocol: the `paid-acquisition-researcher` (or `creative-ops` directly) must re-verify every number in this file during `/marketing:research` before writing any creative brief that references a specific tool's pricing. If the research run returns updated numbers, this file is overwritten. Treat the file as a snapshot that is evidence-tier *as of its last refresh timestamp*, scaffolding-tier otherwise.

## Key concepts
- **Nano Banana Pro (Gemini 3 Pro Image)** — Google's flagship image model, late 2025 / early 2026.
  - Native resolution up to **4096×4096** (4K, ~16-megapixel output).
  - Up to **8 reference images** supported in a single generation call (some third-party providers report up to 14); person-consistency maintained for up to 5 people across inputs.
  - Best-in-class multilingual text rendering (load-bearing for bilingual EN+FR ad creative for Quebec).
  - API pricing as of February 2026: **$0.067 per 1K image, $0.134 per 2K image, $0.24 per 4K image**. Batch API: 50% off (4K → $0.12, 2K → $0.067).
  - Source: [blog.google/innovation-and-ai/products/nano-banana-pro](https://blog.google/innovation-and-ai/products/nano-banana-pro/); pricing cross-checked against OpenRouter and Fal.
  - **Brief-writer guidance for ad creative.** Use the multi-reference feature to bundle a brand color swatch, a product/service reference, and a target audience photo as a single call. For Meta feed and Stories, generate at 2K and let the platform compress; for billboard / OOH (rare in marketing-plugin scope but possible), use 4K.
- **Google Veo 3.1** — Video model with native audio, suited for short ad creative (5-30s).
  - Three tiers: **$0.05/sec Lite, $0.15/sec Fast, $0.40/sec Standard**. All tiers include native audio at no extra cost.
  - 8-second video at Fast tier: $1.20. At Standard: $3.20. Lite roughly halves Fast cost.
  - Source: [blog.google/innovation-and-ai/technology/ai/veo-3-1-lite](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-lite/).
  - **Brief-writer guidance.** Default to Fast for performance creative (cheap, adequate quality, fast iteration); reserve Standard for hero pieces; use Lite for very-rapid concept exploration where final quality doesn't matter.
- **Higgsfield AI** — Video / character animation specialist with cinematic camera moves (push-in, dolly, orbit, crane).
  - Subscription-based; researcher refreshes per run from higgsfield.ai.
  - **Brief-writer guidance for ad creative.** Specify camera motion explicitly ("slow push-in 2s, hold 3s, slow pull-out 3s"). Higgsfield is the right tool when the ad needs a specific camera move that other tools struggle with.
- **Midjourney v7** — Still-image model with distinctive aesthetic.
  - **No public official API** as of April 2026; Discord + web interface only.
  - Commercial use rules: Pro/Mega plan required above $1M annual revenue.
  - **Brief-writer guidance.** Produce explicit `--ar`, `--style`, `--stylize`, and `--chaos` flags. Best for editorial / mood-driven ad creative; worst for ads with literal text overlays (Midjourney still struggles with in-image text relative to NBP and Ideogram).
- **Ideogram 3** — Typography specialist.
  - Beta API via Together / Fal / Kie / Runware, ~$0.06/image.
  - The model that historically nailed in-image text; still relevant in 2026 for any ad creative where the headline lives inside the image.
- **Recraft V3** — Vector-native image model with clean **SVG output**.
  - Subscription pricing.
  - Use for icons, logos, and vector illustrations destined for use across multiple ad formats and aspect ratios where re-rastering would cause artifacts.
- **Sora 2 / Kling 2.6 / Runway Gen-4.5** — Situational video alternatives.
  - Sora 2: film-grade cinematic, most expensive, longest generation time, best for hero brand video.
  - Kling 2.6: cheap social-clip tier; good for high-volume TikTok / Reels variants.
  - Runway Gen-4.5: integrated editor workflow (mask + inpaint + motion); right tool when a brief specifies edits to existing footage.

## Direct quotes (fair use, attributed)

1. "Official API pricing stands at $0.24 per 4K image as of February 2026, with the Batch API cutting that cost to $0.12. Image input (when using reference images) costs $0.0011 per image at 560 tokens each — essentially negligible even when providing the maximum eight reference images." — paraphrase of Google for Developers / Gemini API documentation cross-referenced with OpenRouter pricing data, [openrouter.ai/google/gemini-3-pro-image-preview](https://openrouter.ai/google/gemini-3-pro-image-preview).

2. "Veo 3.1 Lite is priced at approximately $0.05 per second of video generated on Vertex AI. This model costs less than 50% of the cost of Veo 3.1 Fast, but with the same speed." — paraphrase of Google's Veo 3.1 Lite announcement, [blog.google/innovation-and-ai/technology/ai/veo-3-1-lite](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-lite/).

3. "You can mix up to 8 reference images and maintain consistency of up to 5 people." — paraphrase of Nano Banana Pro / Gemini 3 Pro Image documentation, [fal.ai/models/fal-ai/gemini-3-pro-image-preview/edit](https://fal.ai/models/fal-ai/gemini-3-pro-image-preview/edit).

*(All three quotes are paraphrases of vendor and provider documentation rather than verbatim. The paid-acquisition-researcher should pull exact wording on next refresh.)*

## When to cite
Cited by `creative-ops` in every per-channel creative brief (`briefs/<channel>.md`) — the "Recommended tools" section draws from this table, and the "Per-tool prompt blocks" section uses the exact pricing tier and parameters documented here. Cited by `paid-acquisition-lead` when the campaign budget includes a creative-production line item — the pricing in this file is the input to the production-cost estimate. Cited by `paid-acquisition-researcher` quarterly to refresh the snapshot.

## Anti-citation guidance
Do not cite this file without checking its last-refresh timestamp against the current date. A snapshot older than 90 days should be flagged as stale and re-verified before any prompt block is used in a brief that will drive real money. Do not cite this file as authority for *artistic* tool choice — it documents what the tools can do, not which is right for a given brand or angle. Do not cite the pricing as if it were a guarantee — vendor pricing changes mid-year are common and the file is a snapshot, not a contract.

## Decay note
This file is a "living snapshot." The `paid-acquisition-researcher` has a standing instruction to verify every numeric claim in this file against the source URLs during `/marketing:research`, and to overwrite the file with updated numbers when anything has moved. The timestamp of the last refresh should appear as the first line of the markdown body when the researcher re-runs.
