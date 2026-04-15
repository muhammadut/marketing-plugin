---
title: "Ad Creative by Channel — Specs, Character Limits, and Format Best Practices"
author: Google Ads Help, Meta Ads Help, TikTok for Business, LinkedIn Marketing Solutions (consolidated)
year: 2026
type: docs
tier: evidence
url: https://support.google.com/google-ads/answer/7684791
sub-vertical: visual-ai
cited-by-agents: [creative-ops, paid-acquisition-lead]
---

# Ad Creative by Channel — Specs and Best Practices

## One-line summary
A consolidated, source-cited reference for the channel-specific creative requirements (character limits, aspect ratios, hook windows, runtime constraints) every channel-specific brief must comply with — pulled from each platform's own published documentation so creative-ops never produces a spec that violates the platform's hard limits.

## Why this tier
Evidence. Every number in this file is published by the platform itself and enforced at the ad-upload step — exceed Google's 30-character headline limit and the upload is rejected; exceed Meta's video runtime cap and the platform truncates. These are not opinions; they are constraints. The tier is `evidence` because the source is the platform's own normative documentation. Decay note: platforms change specs annually (typically in Q1); the paid-acquisition-researcher should reverify against each platform's help center quarterly.

## Key concepts

### Google Search — Responsive Search Ads (RSA)
- **Headlines.** Up to **15 headlines**, each up to **30 characters**. Minimum 3 headlines required; Google strongly recommends supplying all 15 to maximize asset combinations.
- **Descriptions.** Up to **4 descriptions**, each up to **90 characters**. Minimum 2 required.
- **Display URL paths.** 2 path fields, each up to 15 characters.
- **What Google shows.** 2-3 headlines per ad and 1-2 descriptions per ad from your provided options, dynamically assembled per query.
- **Character counting.** Letters, numbers, spaces, and punctuation each count as 1. Emoji count as 2 (sometimes more). Most special characters count as 1.
- **Pinning.** Headlines and descriptions can be pinned to specific positions, but pinning reduces the assembly variety Google has to optimize against — pin sparingly.
- **Source.** [support.google.com/google-ads/answer/7684791](https://support.google.com/google-ads/answer/7684791) — *About responsive search ads*.

### YouTube Pre-Roll (TrueView In-Stream)
- **Hook window.** The first **5 seconds** decide everything — that is the skippable threshold. The opening frame and the first audible line have to be the entire promise of the ad in compressed form. Brand reveal, value prop, and call-to-engage all in 5 seconds.
- **Optimal runtime.** 15 seconds is the sweet spot for completion rate; 30 seconds is acceptable for narrative ads but expect skip rate to dominate beyond the 5-second mark.
- **Aspect ratio.** 16:9 horizontal is canonical for desktop YouTube; 9:16 vertical for YouTube Shorts.
- **Source.** Google Ads Help and YouTube Creator Academy — verify exact specs at upload time.

### Meta Feed (Facebook + Instagram)
- **Aspect ratios.** 1:1 square is the universal-fit default (works on both Facebook and Instagram feed). 4:5 vertical maximizes feed real estate on mobile. 1.91:1 horizontal still works but is the weakest mobile format.
- **Image specs.** Recommended 1080×1080 (1:1) or 1080×1350 (4:5).
- **Primary text.** 125 characters before truncation in feed; longer text is allowed and shown in full when expanded.
- **Headline.** 27 characters before truncation.
- **Description.** 27 characters.
- **Video specs.** 1:1 or 4:5 aspect ratio for feed; max runtime 240 minutes (practical: keep under 60 seconds for performance creative).
- **Source.** Meta Business Help Center *Facebook Feed* and *Instagram Feed* ad specs pages.

### Meta Stories and Reels
- **Aspect ratio.** **9:16 vertical only.** Square or horizontal will be letterboxed and underperform.
- **Image specs.** 1080×1920.
- **Video specs.** 9:16, max 60 seconds for Reels, 15 seconds per Story card.
- **Safe area.** Top 250 pixels and bottom 250 pixels of the 1920px frame are reserved for platform UI (profile, CTA buttons). Critical content must live in the middle 1420 pixels.
- **Hook window.** First 1-3 seconds. Stories and Reels users swipe faster than feed users.
- **Source.** Meta Business Help Center *Stories* and *Reels* ad specs.

### TikTok In-Feed Ads
- **Aspect ratio.** **9:16 vertical only**, 1080×1920.
- **Runtime.** 9-15 seconds is the sweet spot; up to 60 seconds is allowed but completion rate falls off rapidly.
- **Hook window.** First 1-2 seconds. TikTok users are even less patient than Reels users.
- **Sound on.** Unlike Meta feed (where sound-off is the norm), TikTok plays sound on by default. Audio is part of the creative spec.
- **Native fit.** TikTok creative that "looks like an ad" underperforms creative that "looks like a TikTok." This is documented in TikTok's own creative best-practices guide.
- **Caption.** 100 characters; supports hashtags.
- **Source.** TikTok for Business *Creative Specs* documentation.

### LinkedIn Sponsored Content
- **Single image ad headline.** 200 characters max; ~70 characters before truncation in feed.
- **Introductory text.** 600 characters max; ~150 characters before truncation.
- **Image specs.** 1.91:1 horizontal recommended (1200×627); 1:1 square also supported.
- **Video specs.** 1:1 or 16:9; 3 seconds to 30 minutes runtime; under 60 seconds is the practical performance sweet spot.
- **Voice.** LinkedIn audiences are professional context; copy that works on Meta feed often fails on LinkedIn for tonal mismatch alone.
- **Source.** LinkedIn Marketing Solutions *Sponsored Content Specifications*.

## Direct quotes (fair use, attributed)

1. "You can add up to 15 headlines to each RSA, with each headline being up to 30 characters long. You must provide at least 3 headlines and 2 descriptions, though Google strongly recommends providing all 15 headlines and all 4 descriptions for maximum optimization." — paraphrase of Google Ads Help, *About responsive search ads*, [support.google.com/google-ads/answer/7684791](https://support.google.com/google-ads/answer/7684791).

2. "Google allows you to input 4 descriptions in an RSA, with each description being up to 90 characters long." — paraphrase of Google Ads Help, *About responsive search ads*.

3. "Every letter, number, space, and punctuation mark counts as one character. Emoji count as 2 characters (sometimes more, depending on the emoji)." — paraphrase of Google Ads character-counting documentation.

*(All three quotes are paraphrases of help-center content rather than verbatim quotes from a specific page; the creative-ops agent should verify exact field limits against each platform's help center before generating briefs.)*

## When to cite
Cited by `creative-ops` in every per-channel brief (`briefs/google-search.md`, `briefs/meta-feed.md`, `briefs/meta-stories.md`, `briefs/tiktok.md`, `briefs/youtube.md`, `briefs/linkedin.md`). Each brief specifies the exact channel constraints from this file, and the candidate-generation step has to comply or the creative will be rejected at upload. Cited by `paid-acquisition-lead` when sizing creative production budgets — the channel constraints determine how many distinct assets a single concept produces.

## Anti-citation guidance
Do not cite this file as a substitute for checking each platform's current specs at the moment of upload — platforms change limits without notice, and the file is a snapshot. Do not assume the spec is the same as the *best practice* — Google's RSA limit is 30 characters per headline, but the best-performing headlines are usually 20-25 characters, and the limit is just the wall the ad bounces off if it's too verbose. Do not paste a single creative across all channels — every channel rewards format-native creative, and channel-cross-posted ads underperform.
