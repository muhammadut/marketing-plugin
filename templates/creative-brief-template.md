# Creative Brief — <channel-slug> — round <N>

Generated-by: creative-ops (brief mode)
Depends-on: .marketing/paid/ad-copy-briefs.md, .marketing/positioning/positioning.md, .marketing/positioning/awareness-ladder.md, .brand/voice.md, .brand/tokens.json
Sources-cited: <comma-separated list of knowledge/ files and .marketing/, .brand/ files this brief quotes>

## 1. Channel

<one sentence naming the channel and surface this round is generating for: google-search / google-pmax / meta-static / meta-reels / tiktok / youtube-skippable / youtube-bumper / linkedin-single-image / linkedin-video / display-banner. Note the network's native viewer behavior in one phrase — "thumb-stop in 1.5s," "sound-off-by-default," "8-second skip gate," "static at 1:1 in feed".>

## 2. Audience

**ICP:** <copy from `.marketing/positioning/positioning.md` target-segment section, one to two sentences>

**Awareness stage (Schwartz):** <one of: Unaware / Problem-Aware / Solution-Aware / Product-Aware / Most-Aware>

> <direct quote from `.marketing/positioning/awareness-ladder.md` for the chosen stage. Should be 2-4 sentences naming the customer's current mental state, what language they use, and what they are *not* yet ready to hear.>

**Why this stage for this round (cite `tier: evidence`):** Schwartz, *Breakthrough Advertising* (1966), tier: evidence. <one sentence on why this stage is the right one for this channel and this round, e.g., "Google Search keyword 'emergency plumber Hamilton' indicates Problem-Aware → Solution-Aware transition; the ad must name the solution category without yet selling the brand."> Cite the awareness-ladder file by section.

## 3. Message hierarchy

The candidate must communicate three things in this order:

1. **Primary** — <one sentence. The single most important thing the viewer must understand in the first second. For visual ads, this is what the eye lands on first. For video, this is the first frame and the first three words of voiceover.>
2. **Secondary** — <one sentence. The supporting claim that completes the value prop. The thing the viewer takes away if they only watch the first three seconds of a video or only glance at a static for one second.>
3. **Proof** — <one sentence. The credibility hook. A specific number, a named guarantee, a recognized logo, a real testimonial. Generic language like "trusted by thousands" is forbidden.>

Cite `.marketing/positioning/messaging-hierarchy.md` for the source of these three layers.

## 4. Brand alignment quote

> <direct multi-line quote from `.brand/voice.md` containing:
>  - the voice principles (3-5 named principles)
>  - the forbidden words list (if any)
>  - the required phrase or pronoun policy (if any)
>  - the tone target on the NN/g four axes (formal/casual, serious/funny, respectful/irreverent, matter-of-fact/enthusiastic)>

Any candidate that violates the forbidden words, ignores the required phrases, or reads as a different tone on the four axes is by definition off-brief.

**Brand colors and typography:** pull from `.brand/tokens.json` — primary/secondary/accent hex (or OKLCH) values, primary typeface family, allowed weights. The candidate's color palette must intersect the token set; the candidate's type must be the brand typeface or a defensible visual cousin if the tool can't render the exact face.

## 5. Visual direction

<5-10 sentences of aesthetic guidance. Describe what the work should *feel* like — mood, energy, lighting, composition, subject matter. Describe what it should NOT be — name the category clichés to avoid, citing `.marketing/research/paid-research.md` and any competitive-prior-art notes by section. Name reference styles only if the user's `.marketing/assets/` mood folder supports them (cite by filename: "ref-3.png recalls Patagonia's outdoor-utility shooting style"). Do not invent aesthetic lineages the user hasn't supplied references for.>

**For video / motion ads only.** Specify:
- Duration target (e.g., "5s for hook, 15s for full")
- Pacing (slow / measured / brisk)
- Audio intention (sound-off readable with captions vs sound-on-required vs ambient bed)
- First-frame requirement (the thumb-stop image)
- Last-frame requirement (the CTA card with brand mark)

## 6. Recommended tools (ranked, channel-appropriate)

Rank based on the channel's needs and the current `state-of-visual-ai` snapshot in `.marketing/research/paid-research.md`. Always offer at least 2 tools so the user can cross-pollinate.

1. **<Tool 1>** — <2-3 sentences on why this tool fits this channel best. Cite a concrete capability tied to the channel's native format: "native 1:1 at 2K" for Meta static, "8s output with sound" for Veo on TikTok, "vector-native wordmark layouts" for Recraft on display, "reference-image conditioning" for product shots. Cite `paid-research.md` for the most recent capability notes.>
2. **<Tool 2>** — <2-3 sentences on why this tool is a useful contrast — different aesthetic, different strength, different price point.>
3. (optional) **<Tool 3>** — <only if the channel benefits from a third angle, e.g., a typography specialist for headline-heavy display.>

## 7. Per-tool prompt blocks

Each block is fenced so the user can copy cleanly. Fill in parameters tuned to the tool's syntax. Include only the tool blocks for the tools listed in section 6; omit the rest.

### Nano Banana Pro (static)
```
<full prompt, 2-4 sentences of description tied to the message hierarchy in section 3>

Reference images (up to 14):
- ref-1: .brand/logo/primary.png
- ref-2: .marketing/assets/<filename>  (user mood reference if any)
- ref-3: .marketing/assets/<filename>
- ref-4: .brand/assets/color-swatch.png  (derived from tokens.json)
...

Aspect ratio: <1:1 / 4:5 / 9:16 / 16:9>  (per channel native)
Resolution: <2K for ideation, 4K for refinement>
Volume: <5-15 generations recommended for this round>
```

### Veo 3.1 (video)
```
Shot: <description tied to the first-frame requirement and message hierarchy>
Duration: <5s | 8s | 15s>
Tempo: <slow | measured | brisk>
Audio: <ambient | diegetic | voiceover-required — describe the sound intention>
Reference stills: .brand/logo/primary.png, .marketing/assets/<filename>
First frame: <one-sentence description of the thumb-stop image>
Last frame: <one-sentence description of the CTA card>
```

### Higgsfield (motion)
```
Subject: <pose, context, action — tied to the visual direction>
Camera move: <push-in | dolly-left | orbit | tilt-up | static>
Aesthetic reference: <filename or short descriptor>
Duration: <3s | 5s | 8s>
```

### Midjourney v7 (stylized)
```
<prompt text> --ar <ratio per channel> --style raw --stylize <100-400> --chaos <0-40>
```

### Recraft V3 (vector / display)
```
<brief prompt for vector or layout output>
Output format: SVG / PNG
Palette: <hex list from .brand/tokens.json>
Type: <typeface family from tokens.json>
```

### Ideogram 3 (typography-heavy)
```
Headline text: "<the primary headline from message hierarchy>"
Style descriptor: <e.g., "industrial slab serif, slight weight variation, hand-built feel">
Color palette: <hex list from tokens.json>
```

### Sora 2 (cinematic)
```
Shot description: <multi-clip narrative tied to the message hierarchy>
Duration: <up to 20s>
Audio: <required sound design>
Reference stills: .brand/logo/primary.png, mood references from .marketing/assets/
```

## 8. Asset specs

Channel-specific. Fill in for the channel this brief targets.

| Spec | Value |
|---|---|
| Aspect ratio(s) | <1:1, 4:5, 9:16, 16:9 — per channel> |
| Length / duration | <static | 5s | 15s | 30s — per channel max> |
| Min resolution | <2K | 1080p | 4K> |
| Max file size | <per Google Ads / Meta / TikTok limits, MB> |
| Format | <PNG | JPG | MP4 | MOV | GIF> |
| Safe area | <% inset for native UI overlays where applicable> |
| Captions required? | <yes — sound-off-by-default | no> |

Cite the source of each spec by linking to the channel's official documentation in `paid-research.md`. Do not invent limits.

## 9. Volume target

Generate **<N>** candidates this round.

Justification: target 5-15 candidates per channel per round. Lower than brand-ideation volume (which targets 10-30) because per-channel ad creative is more constrained — the brief locks aspect ratio, length, message hierarchy, and brand alignment, so the search space is narrower. Cite Demand Curve creative-testing cadence (tier: scaffolding) for the volume reasoning. For refinement rounds, target 3-8 — the search space has narrowed further and generation cost has usually gone up (4K statics, longer videos).

## 10. Drop instructions

When you have generated candidates, drop them into:

```
.marketing/candidates/<channel-slug>-<N>/
```

Where `<channel-slug>` matches this brief's channel field exactly (e.g., `meta-static`, `google-search`, `tiktok`, `youtube-skippable`).

Filename pattern:

```
<sequence>-<tool>-<short-description>.<ext>
```

Examples:

```
01-nano-banana-pro-flooded-basement-hero.png
02-veo-5s-emergency-plumber-arrives.mp4
03-higgsfield-orbit-truck-arrival.mp4
04-midjourney-rugged-uniform-reaching-door.png
05-ideogram-headline-slab-charcoal.png
```

Optional: each file may have a `.txt` sidecar with the same base name containing the prompt you used and the tool. Sidecars are not required but presence increases the candidate's "A/B variation potential" sub-score in selection (the rubric rewards reproducible variants the team can iterate on).

## 11. Selection criteria preview

When you run `/marketing:select-creative <channel-slug> <N>`, the creative-ops agent in selection mode will score every candidate 1-5 on six dimensions and write `.marketing/selected/<channel-slug>-<N>.md`. The dimensions, known up front so you can self-filter:

1. **Brand alignment** — does it express the voice and tokens from `.brand/`? Cited against `voice.md` and `tokens.json`.
2. **Channel fit** — does it match the channel's native aesthetic, aspect ratio, length, and viewer attention pattern? Cited against the channel spec table in section 8.
3. **Awareness stage match** — does it speak to the Schwartz awareness level the brief targeted? Cited against `awareness-ladder.md`.
4. **Message hierarchy** — does primary / secondary / proof come through in the right order? Cited against section 3 of this brief.
5. **Creative quality** — composition, balance, typography, legibility, motion craft, audio (where applicable). Visual judgement.
6. **A/B variation potential** — does this candidate offer a meaningfully different testable angle from the other winners, or is it a near-duplicate?

Total 6-30. Minimum acceptable for a winner: 20. Below 15 is a rejection by default.

## 12. Compliance notes

Per channel. Fill in only the rules that apply to this channel.

- **Google Ads policy** — no superlatives without proof, no urgency claims without basis, no health/financial claims without disclaimers. Ad copy must pass the policy preview before push. Source: Google Ads Personalized Advertising Policy and Restricted Content docs. Cite the specific policy section if the brief is in a regulated vertical (medical, financial, dating, alcohol).
- **Meta ad standards** — no before/after imagery in health/wellness, no implied personal attributes targeting, no surrounding-product implication. Source: Meta Advertising Policies.
- **CASL (Canadian Anti-Spam Legislation)** — for any direct-response or lead-capture creative, CTA must comply with CASL consent rules. Cite [knowledge/paid-acquisition/casl-compliance.md] if the project is Canadian.
- **Quebec Bill 96 / Law 25** — for any creative shown to Quebec users, French-language version is required and must be at least as prominent as English. Cite the brand's bilingual policy.
- **PIPEDA** — for any creative that captures personal information (lead forms), consent disclosure required.

If none apply, write "No special compliance constraints for this channel and vertical."
