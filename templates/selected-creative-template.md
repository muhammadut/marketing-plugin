# Selection — channel: <channel-slug>, round <N>

Generated-by: creative-ops (selection mode)
Generated: <ISO-8601 timestamp>
Depends-on: .marketing/briefs/brief-<channel-slug>.md, .marketing/positioning/positioning.md, .marketing/positioning/awareness-ladder.md, .brand/voice.md, .brand/tokens.json, .marketing/candidates/<channel-slug>-<N>/
Sources-cited: <comma-separated files cited across the rationales below>
Candidates reviewed: <integer count of files under candidates/<channel-slug>-<N>/ that creative-ops actually read>

## Summary

<2-3 sentences: the overall state of this round. Did the brief land? Did the tool mix produce diverse candidates or did they collapse to one aesthetic? Is there a clear winner or is the whole round mid? If the channel has video and static mixed, note whether one format outperformed the other.>

## Winners (top 3)

### Winner 1: <filename>
Score: <total>/30

- **Brand alignment: <1-5>/5** — <one sentence naming the voice principles expressed and citing `.brand/voice.md` by section. E.g., "expresses the 'plain-spoken expertise' voice principle through the 'no jargon' headline; passes the forbidden words list; reads as the target tone (matter-of-fact, respectful, serious) on three of the four NN/g axes.">
- **Channel fit: <1-5>/5** — <one sentence on the channel-native characteristics. E.g., "1:1 framing reads cleanly in Meta feed; thumb-stop image is the wet basement at 0:00, well within the 1.5s native attention window; CTA card lands at 0:04 with brand mark visible.">
- **Awareness stage match: <1-5>/5** — <one sentence naming the Schwartz stage and how the candidate hits it. Cite `awareness-ladder.md` by section. E.g., "lands the Problem-Aware → Solution-Aware transition by naming 'flooded basement' (problem language) and 'Hamilton plumber in 30 min' (solution category) without yet selling the brand name; matches awareness-ladder.md §2.">
- **Message hierarchy: <1-5>/5** — <one sentence on whether primary/secondary/proof landed in order. E.g., "primary (urgency) hits in the first frame; secondary (geographic specificity) reads in the lower third; proof (30-minute response) is the largest text element. Order correct.">
- **Creative quality: <1-5>/5** — <one sentence of visual judgement — composition, balance, typography, legibility at thumbnail, motion craft if video, audio sync if audio. Cite the observed quality, not just the adjective.>
- **A/B variation potential: <1-5>/5** — <one sentence on whether this candidate offers a testable angle different from the other winners. Cite the sidecar `.txt` presence explicitly because the rubric rewards reproducibility. E.g., "sidecar prompt present; the 'arrival shot' angle is meaningfully different from Winner 2's 'damaged scene' angle and Winner 3's 'before/after' angle, giving three testable creative hypotheses.">

### Winner 2: <filename>
Score: <total>/30

- **Brand alignment: <1-5>/5** — <cited rationale>
- **Channel fit: <1-5>/5** — <cited rationale>
- **Awareness stage match: <1-5>/5** — <cited rationale>
- **Message hierarchy: <1-5>/5** — <cited rationale>
- **Creative quality: <1-5>/5** — <cited rationale>
- **A/B variation potential: <1-5>/5** — <cited rationale>

### Winner 3: <filename>
Score: <total>/30

- **Brand alignment: <1-5>/5** — <cited rationale>
- **Channel fit: <1-5>/5** — <cited rationale>
- **Awareness stage match: <1-5>/5** — <cited rationale>
- **Message hierarchy: <1-5>/5** — <cited rationale>
- **Creative quality: <1-5>/5** — <cited rationale>
- **A/B variation potential: <1-5>/5** — <cited rationale>

## Rejected (top 5 with reasons)

Include the 5 highest-scoring rejections, not the 5 lowest — surface what almost made it and why it didn't. The remaining candidates are listed by total score in the appendix at the bottom.

### Rejected: <filename>
Score: <total>/30

- <dimension and score that killed it, with one-sentence citation. E.g., "Brand alignment 1/5 — uses the forbidden word 'cheap' which voice.md §3 explicitly bans for this brand; also reads as the wrong tone on three of four NN/g axes (too casual, too funny, too irreverent for a plumber emergency context).">
- <second-worst dimension and score, also with citation>

### Rejected: <filename>
Score: <total>/30

- <fatal dimension, cited>
- <secondary issue, cited>

### Rejected: <filename>
Score: <total>/30

- <cited>
- <cited>

### Rejected: <filename>
Score: <total>/30

- <cited>
- <cited>

### Rejected: <filename>
Score: <total>/30

- <cited>
- <cited>

## Recommendation

<1-3 sentences. Name the action explicitly: "Proceed with Winner 1 to the ship-campaign phase as the primary creative; hold Winners 2 and 3 as A/B test variants." OR "None of the winners cross the 20-point threshold; do not proceed — refine the brief (see iteration suggestion below)." OR "Winner 1 is strong enough to lock; advance to `/marketing:paid --accept-creative <channel-slug>-<N> --winner <filename>`."

State explicitly which rejected directions should NOT be pursued in a next round, with the reason cited from the rubric. E.g., "Do not pursue 'cartoon plumber' aesthetic in next round — five of seven cartoon-style candidates rejected on Brand alignment; voice.md §2 forbids cartoon for this vertical.">

## Iteration suggestion

If none of the winners feel right at gut-check level, this section tells the user where the fix probably lives. Three possibilities — pick the one the evidence supports, do not present all three as equally likely:

1. **Refine the brief** — if the Brand alignment and Channel fit scores are good but Creative quality or Message hierarchy scores are weak, the brief's visual direction or tool choice is the bottleneck. Run `/marketing:paid --refine-brief --channel <channel-slug>` with notes on what to shift.
2. **Refine the awareness ladder / messaging hierarchy** — if Awareness stage match scores are uniformly low, the brief targeted the wrong Schwartz stage for this channel and audience. Edit `.marketing/positioning/awareness-ladder.md` and re-run `/marketing:paid` for this channel.
3. **Refine the positioning** — if Brand alignment and Awareness stage match are both low across all candidates, the upstream positioning is mismatched to what the visual creative can actually express. Re-run `/marketing:positioning` to revise `positioning.md`, then restart this channel from round 1.

<Pick the option the evidence supports, and explain in 2-3 sentences why. Cite specific scores above. Do not present all three as equally likely when the evidence points one direction.>

## Appendix: full scoring table (all candidates)

| Filename | Brand | Channel | Awareness | Hierarchy | Quality | A/B | Total | Status |
|---|---|---|---|---|---|---|---|---|
| 01-nano-banana-pro-... | 5 | 5 | 4 | 5 | 4 | 4 | 27 | Winner 1 |
| 02-veo-5s-emergency-... | 4 | 5 | 5 | 4 | 5 | 4 | 27 | Winner 2 |
| 03-... | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Winner 3 |
| 04-... | 3 | 3 | 3 | 3 | 3 | 3 | 18 | Rejected (top 5) |
| ... | | | | | | | | |

(Every candidate the creative-ops agent read is listed here with its six-dimension scores. The "winners" and "rejected (top 5)" sections above quote the rationale for the highlighted ones; this appendix is the auditable full record.)
