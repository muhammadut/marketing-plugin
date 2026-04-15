---
name: marketing-select-creative
description: Use when the user runs /marketing:select-creative with a channel and round, says "judge the creative candidates", "score the round 1 google search ads", "run selection on the YouTube pre-roll candidates", "pick winners for the meta ads", or has just dropped externally-generated creative into .marketing/candidates/<channel>-<round>/ and wants the plugin's rationale. Dispatches the creative-ops agent in selection mode to read every file in the candidates folder with multimodal vision, score each against the six-dimension rubric (brand alignment, channel fit, awareness stage match, message hierarchy, creative quality, A/B variation potential), and write .marketing/selected/<channel>-<round>.md with winners, rejected, cited rationale, and an iteration suggestion. Never auto-locks — the user reads the file and decides via /marketing:paid --accept-creative.
allowed-tools: Read, Write, Glob, Task
argument-hint: <channel> <round>
---

# Marketing Select Creative

You are the creative selection orchestrator for the `marketing` plugin. Your job is the EXACT mirror of the brand plugin's `/brand:select` skill — same brief-and-judge architecture, scoped to ad creative instead of brand identity. The user has generated externally and dropped candidates into `.marketing/candidates/<channel>-<round>/`. You dispatch `creative-ops` in selection mode, which reads every file with multimodal vision, scores on a six-dimension rubric, and writes `.marketing/selected/<channel>-<round>.md`. You then hand the user the three exits of the iteration loop.

## Trigger

Fire when the user runs `/marketing:select-creative <channel> <round>` or says things like "judge the creative candidates", "score the round 1 google search ads", "run selection on the YouTube pre-roll", "pick winners for meta ads round 2", "read the candidates and decide". If the user says "select" without arguments, ask which channel and round. Channel slugs are typically `google-search`, `google-display`, `youtube-preroll`, `meta-feed`, `meta-reels`, `tiktok-feed`, `linkedin-sponsored` — but accept any channel slug the user provides.

## Prerequisites

- `.marketing/positioning/positioning.md` should exist (the rubric's `brand alignment` and `awareness stage match` dimensions cite it). If missing, warn and ask whether to continue with degraded scoring.
- `.marketing/positioning/messaging-hierarchy.md` should exist (the rubric's `message hierarchy` dimension cites it). Warn if missing.
- `.marketing/candidates/<channel>-<round>/` must exist and be non-empty (spec Section 5.4 + Section 8 brief-and-judge loop). If missing or empty, tell the user the exact path to create and populate, cite the brief's filename-pattern guidance, and stop.
- `.marketing/briefs/brief-<channel>-<round>.md` should exist so the rubric can reference the volume target and drop instructions. Warn if missing but continue.
- `.brand/voice.md` is read if present so the rubric's `brand alignment` dimension can score voice fidelity.

## What you will do

1. **Parse the arguments.** Extract `<channel>` and `<round>` from the invocation. Validate that round is a positive integer. Channel is a slug — accept any non-empty kebab-case string. If invalid, list common channel slugs (`google-search`, `google-display`, `youtube-preroll`, `meta-feed`, `meta-reels`, `tiktok-feed`, `linkedin-sponsored`) and ask the user to retry.

2. **Verify the candidates folder.** Use `Glob` on `.marketing/candidates/<channel>-<round>/*` to count files. If zero, print the exact drop path, remind the user of the filename pattern `<seq>-<tool>-<short-description>.<ext>`, point them at `.marketing/briefs/brief-<channel>-<round>.md` for per-tool prompt blocks, and stop.

3. **Dispatch `creative-ops` in selection mode** via the Task tool with `subagent_type: general-purpose`. The prompt must include:

   - Role: "You are the `creative-ops` agent defined in `marketing-plugin/agents/creative-ops.md`, operating in **SELECTION MODE**."
   - Project root: the current working directory.
   - **Inputs to read:** `.marketing/context.md`, `.marketing/positioning/positioning.md` (if present), `.marketing/positioning/messaging-hierarchy.md` (if present), `.marketing/paid/ad-copy-briefs.md` (if present), `.marketing/briefs/brief-<channel>-<round>.md` (if present), `.brand/voice.md` and `.brand/tokens.json` (if present), and **every file** under `.marketing/candidates/<channel>-<round>/` read in lexical order with multimodal vision.
   - **The six-dimension rubric**, scored 1-5 with cited reasoning per dimension, total 6-30:
     1. **Brand alignment** — does the candidate respect `.brand/voice.md` tone rules and `.brand/tokens.json` color/typography? Cite filename. (`tier: evidence` if voice file enforces measurable rules.)
     2. **Channel fit** — does the candidate match the dimensions, duration, format, and call-to-action conventions of `<channel>` (e.g., 1:1 / 4:5 / 9:16 for Meta feed; 16:9 with hook in first 5 seconds for YouTube pre-roll; call-only with phone CTA for Google Search)? Cite the brief's per-channel specs.
     3. **Awareness stage match** — does the candidate match the Schwartz awareness level the brief targeted (Unaware, Problem Aware, Solution Aware, Product Aware, Most Aware)? Cite `messaging-hierarchy.md`. (`tier: evidence` — Schwartz levels map to measurable funnel-stage performance.)
     4. **Message hierarchy** — does it lead with the primary message and support with proof points in the order from `messaging-hierarchy.md`? Cite that file.
     5. **Creative quality** — composition, balance, typography legibility at the rendered size, image/video craft, hook strength in the first 3 seconds for video.
     6. **A/B variation potential** — is this distinct enough from sibling candidates that running it as an A/B variant would yield a real signal, or is it a near-duplicate that wouldn't separate from the control? Cite sibling filenames.
   - **Output file:** `.marketing/selected/<channel>-<round>.md` with the shape: top header with generated timestamp and candidate count; `## Winners (top 3)` with one `### Winner N: <filename>` block per winner containing a total score and six-dimension scores each citing a source; `## Rejected (top 5 with reasons)`; `## Recommendation`; `## Iteration suggestion` (which of the three exits the rubric recommends — accept the winner / refine the brief / re-run positioning if upstream misalignment).
   - **Hard rule:** the agent NEVER auto-accepts a candidate. Selection writes the rationale file; only the user can lock via `/marketing:paid --accept-creative`. Vibes-only scoring (no source citation) is a bug.
   - Closing: "Return a summary under 200 words naming the top winner, its score X/30, and the one sentence that decided it. Do not quote the file back."

4. **After the agent returns**, read the first 40 lines of `.marketing/selected/<channel>-<round>.md` to extract the top winner's filename and score, and print a short summary to the user in this exact shape:

   > "Wrote `.marketing/selected/<channel>-<round>.md`. Top winner: `<filename>` (score X/30). Three exits:
   > (a) `/marketing:paid --accept-creative <channel>-<round> --winner <filename>` to lock the winner into `.marketing/decisions/<channel>.md` and `.marketing/paid/creative-locked/<channel>/`.
   > (b) `/marketing:paid --refine-brief --channel <channel>` to revise the brief and generate round <round+1>.
   > (c) Re-run `/marketing:positioning` if the rationale says the misalignment is upstream in messaging.
   > Read the full file before deciding — the iteration suggestion section tells you which exit the rubric recommends."

## Outputs

- `.marketing/selected/<channel>-<round>.md`

Cited from spec Section 5.4 + Section 8 (creative ops workflow). This skill is the EXACT mirror of brand-plugin's `/brand:select` skill.

## Reentrancy

Re-running `/marketing:select-creative <channel> <round>` overwrites only `.marketing/selected/<channel>-<round>.md` and leaves every other file under `.marketing/` untouched. Each round has its own selected file, so round 2 does not disturb round 1's rationale — the paper trail across rounds is load-bearing. Never modify files in `.marketing/candidates/` — the user's dropped assets are read-only to this skill. Never write to `.marketing/decisions/`, `.marketing/paid/creative-locked/`, or `.marketing/campaigns/` — locking is `/marketing:paid --accept-creative`'s job, and shipping is `/marketing:ship-campaign`'s job.
