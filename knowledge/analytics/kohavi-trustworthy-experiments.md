---
title: "Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing"
author: Ron Kohavi, Diane Tang, Ya Xu
year: 2020
type: book
tier: evidence
url: https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59
sub-vertical: analytics
cited-by-agents: [analytics-experimentation-lead, analytics-experimentation-researcher, marketing-director]
---

# Kohavi, Tang, Xu — Trustworthy Online Controlled Experiments

## One-line summary
Cambridge University Press, three principal authors who built and ran the experimentation platforms at Microsoft (Bing), Google, and LinkedIn — this is the closest thing the field has to a definitive textbook on running A/B tests that don't lie, and the math in it is engineering math, not opinion.

## Why this tier
Evidence — and the highest-confidence evidence in this entire knowledge bundle. Three authors with combined decades running production experimentation platforms at the largest scale on the internet. The book documents specific quantitative pitfalls (peeking, sample ratio mismatch, Simpson's paradox, novelty effects, primacy effects, twins, twyman's law) with worked examples drawn from real experiments they ran. Every claim is checkable; every pitfall is reproducible; every recommendation is grounded in measured experience. If a tier above `evidence` existed for "this is engineering math you can build a system on," this book would be in it. The only caveat is that the book assumes a reader who can run hundreds of experiments per year — for a $1k/mo bootstrap account that runs maybe one experiment a month, the statistical apparatus is more aspirational than operational, but the failure modes are universal even at small scale.

## Key concepts
- **Twyman's Law.** "Any figure that looks interesting or different is usually wrong." If an experiment result looks too good to be true, it almost certainly is — and the first action should be to look for instrumentation bugs, not to celebrate.
- **Sample Ratio Mismatch (SRM).** If your A/B test was supposed to send 50/50 traffic to control and treatment but you observe 50.4/49.6, your experiment is **broken**. SRM almost always indicates a bug (selection bias, telemetry loss, redirect issues), not a real difference. Kohavi: SRM checks should run on every experiment automatically; results should be discarded when SRM fires.
- **Peeking.** Looking at experiment results before they reach the pre-declared sample size and stopping early when significance appears. Inflates false positive rate dramatically (from 5% nominal to 20-30% in practice). Either pre-commit to a sample size and don't peek, or use sequential testing methods (mSPRT, alpha-spending) that adjust for the peeking.
- **Simpson's Paradox.** A treatment that wins overall can lose in every subgroup, or vice versa, depending on subgroup mix. Always check segment-level results in addition to the overall ATE; segment-level reversals are common and load-bearing.
- **Novelty effects and primacy effects.** Users may react to a change because it is new (positive or negative), not because of the change itself. The first week of an experiment is usually noisy in this direction; the third or fourth week is more representative.
- **Heterogeneous treatment effects (HTE).** The treatment may help one segment dramatically and hurt another segment moderately, with a small positive ATE that hides both. Reading only the average is reading wrong.
- **OEC — Overall Evaluation Criterion.** Pre-commit to a single metric (or a thoughtful linear combination) that decides the experiment, before the experiment runs. Without an OEC, every experiment turns into a metric-shopping exercise after the fact.
- **Power and sample size.** You need to know in advance how much sample you need to detect a given effect size with a given confidence. For most consumer products the realistic minimum-detectable-effect at the volume a startup operates at is uncomfortably large; the right move is often to run fewer, bigger experiments rather than many small ones.

## Direct quotes (fair use, attributed)

1. "The first principle is that you must not fool yourself — and you are the easiest person to fool. We borrow this from Richard Feynman because it captures the experimentation mindset exactly." — Kohavi, Tang, Xu, *Trustworthy Online Controlled Experiments*, Chapter 1, paraphrased.

2. "If you observe a sample ratio mismatch, your experiment is invalid. Do not interpret the result. Find the bug, fix it, and re-run." — paraphrase of Chapter 21 (Sample Ratio Mismatch) framing.

3. "Peeking inflates the false positive rate. The textbook nominal 5% becomes 20-30% in practice when an analyst checks the experiment daily and stops at the first significant result." — paraphrase of Chapter 17 (Online Experimentation Pitfalls) discussion.

*(All three quotes are paraphrases of book content rather than verbatim; the analytics-experimentation-researcher should pull exact citations from the published Cambridge edition before using in formal documents.)*

## When to cite
Cited by `analytics-experimentation-lead` in every `experiment-spec.md` (the OEC, the sample-size calculation, the pre-committed analysis plan). Cited by the lead when reviewing proposed experiments from other sub-verticals — the lead's job is to flag SRM checks, peeking risk, and HTE concerns before the experiment runs, not after. Cited by `marketing-director` when sub-vertical leads claim experiment results that don't match expected effect sizes.

## Anti-citation guidance
Do not cite Kohavi as a license to run hundreds of small experiments at low traffic — the book is explicit that under-powered experiments are usually a waste of effort. Do not cite Kohavi to overrule a clearly working bootstrapper heuristic on statistical grounds when the bootstrapper doesn't have the volume for proper experiments anyway. Do not assume the patterns in the book translate cleanly to single-digit users per day; they do not. The book is for organizations that can run an experiment to power; smaller organizations should rely on judgment plus the book's *failure-mode* lessons (don't peek, check for SRM, watch for novelty) without pretending to a rigor they cannot afford.
