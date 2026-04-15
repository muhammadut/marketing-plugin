# Marketing Workflow

## Phase diagram

```
      ┌──────────────┐
      │  empty dir   │
      └──────┬───────┘
             │
             │ /marketing:init
             ▼
      ┌──────────────┐
      │   INIT       │──── .marketing/context.md
      │              │──── .marketing/assets/  (user drops references)
      └──────┬───────┘
             │
             │ /marketing:research  (5-way parallel)
             ▼
      ┌──────────────┐
      │  RESEARCH    │──── paid-acquisition-researcher
      │              │──── seo-content-researcher
      │              │──── lifecycle-researcher
      │              │──── positioning-researcher
      │              │──── analytics-experimentation-researcher
      │              │──── .marketing/research/{paid,seo,lifecycle,
      │              │                          positioning,analytics}-research.md
      └──────┬───────┘
             │
             │ /marketing:positioning   (run first; everything reads it)
             ▼
      ┌──────────────┐
      │ POSITIONING  │──── positioning-lead
      │              │──── .marketing/positioning/positioning.md
      │              │──── .marketing/positioning/awareness-ladder.md
      │              │──── .marketing/positioning/messaging-hierarchy.md
      └──────┬───────┘
             │
             │ /marketing:plan
             ▼
      ┌──────────────┐
      │    PLAN      │──── marketing-director
      │              │──── .marketing/plan.md
      │              │──── .marketing/plan-adrs/ADR-*.md
      └──────┬───────┘
             │
             │ /marketing:paid    (default mode — produces brief)
             ▼
      ┌──────────────┐
      │    PAID      │──── paid-acquisition-lead → campaign-structure.md
      │   (brief)    │──── creative-ops (brief mode) → briefs/brief-<channel>.md
      │              │──── paid/keywords/*.csv
      │              │──── paid/ad-copy-briefs.md
      │              │──── paid/bid-strategy.md
      │              │──── paid/budget-plan.md
      └──────┬───────┘
             │
             │ user goes external
             ▼
      ┌──────────────────────────────────────┐
      │  USER GENERATES EXTERNALLY            │
      │  (Nano Banana Pro / Veo 3.1 /         │
      │   Higgsfield / Midjourney /           │
      │   Recraft / Ideogram / Sora 2 / ...)  │
      │  drops files into                     │
      │  .marketing/candidates/<channel>-<round>/
      └──────┬───────────────────────────────┘
             │
             │ /marketing:select-creative <channel> <round>
             ▼
      ┌──────────────┐
      │    SELECT    │──── creative-ops (selection mode)
      │              │──── multimodal read of candidates/
      │              │──── .marketing/selected/<channel>-<round>.md
      └──────┬───────┘
             │
             ├── ACCEPT  → /marketing:paid --accept-creative <channel>-<round>
             │            → .marketing/decisions/<channel>.md written
             │            → winner copied into paid/creative/generated/
             │            → advance to next channel or to ship-campaign
             │
             ├── REFINE BRIEF → /marketing:paid --refine-brief --channel C
             │            → briefs/brief-<channel>.v2.md
             │            → user generates round 2, back to SELECT
             │
             └── REFINE POSITIONING → /marketing:positioning  (re-run)
                          → positioning-lead revises positioning.md
                          → all affected channels reset to round 1
             ▼
      ┌──────────────┐
      │    SHIP      │──── /marketing:ship-campaign --account primary
      │  (paused)    │──── paid-acquisition-lead → Google Ads API
      │              │──── campaign created in PAUSED state
      │              │──── prints entity IDs
      └──────┬───────┘
             │
             │ user reviews in Google Ads UI
             ▼
      ┌──────────────┐
      │  GO LIVE     │──── /marketing:ship-campaign --account primary --enable
      │              │──── flips PAUSED → ENABLED
      │              │──── live calls / clicks start routing
      └──────┬───────┘
             │
             │ /marketing:status (anytime, reentrant)
             ▼
      ┌──────────────┐
      │  STUBBED     │──── /marketing:seo (v0.2 stub)
      │  TRACKS      │──── /marketing:lifecycle (v0.2 stub)
      │              │──── /marketing:analytics (v0.2 stub)
      └──────────────┘
```

`/marketing:status` is reentrant and can be run at any point. It prints which sub-verticals are complete, which files exist, which campaigns are live, which experiments are running, and which blocking inputs are missing.

## Time budget

| Phase | Command | Actor | Wall time (plugin-side) | Wall time (user-side) |
|---|---|---|---|---|
| Init | `/marketing:init` | user interview | 0 | 10-20 min |
| Assets drop | (no command) | user | 0 | 5-30 min |
| Research | `/marketing:research` | 5 researchers in parallel | 5-10 min | 0 |
| Positioning | `/marketing:positioning` | `positioning-lead` | 3-8 min | 0 |
| Plan | `/marketing:plan` | `marketing-director` | 2-5 min | 0 |
| Paid (brief) | `/marketing:paid` | `paid-acquisition-lead` + `creative-ops` brief mode | 5-10 min | 0 |
| Generate externally | (user's tools) | user | 0 | **30-120 min per channel per round** |
| Select | `/marketing:select-creative C R` | `creative-ops` selection mode | 2-4 min | 0 |
| Decide | (user) | user reviews `selected/` | 0 | 5-15 min |
| Accept/refine | `/marketing:paid --accept-creative` or `--refine-brief` | orchestrator or `creative-ops` | <1 min or 3-5 min | 0 |
| Ship (paused) | `/marketing:ship-campaign` | `paid-acquisition-lead` (API push) | 2-5 min | 30 min review |
| Go live | `/marketing:ship-campaign --enable` | API flip | <1 min | 0 |
| **Plugin-side total (paid only)** | | | **~30-60 min** | |
| **User-side total** | | | | **variable — an afternoon to several weeks** |

Plugin-side time is deterministic and bounded. User-side time is dominated by the external creative generation phase — how many channels the user is briefing, how many rounds each one takes, and whether the user is batching across a week or sitting down for a sprint. The plugin imposes no schedule; it imposes only a discipline. See spec §11 for the full elocal_clone Month 1 walkthrough (60 plugin minutes plus 40 review minutes from empty repo to live campaign).

## State directory tree

All state lives in `.marketing/` inside the **target project**, never inside the plugin.

```
<target-project>/
└── .marketing/
    ├── context.md                          # /marketing:init output
    ├── plan.md                             # /marketing:plan output
    ├── open-questions.md                   # unresolved items
    ├── plan-adrs/                          # marketing-director ADRs
    │   ├── ADR-0001-paid-channel-priority.md
    │   └── ADR-0002-attribution-model.md
    ├── assets/                             # USER drops references
    │   ├── README.md                       # instructions from /marketing:init
    │   └── <user files>                    # screenshots, PDFs, brand refs
    ├── research/                           # /marketing:research outputs (5 parallel)
    │   ├── paid-research.md
    │   ├── seo-research.md
    │   ├── lifecycle-research.md
    │   ├── positioning-research.md
    │   └── analytics-research.md
    ├── paid/                               # /marketing:paid outputs (lead)
    │   ├── campaign-structure.md
    │   ├── keywords/
    │   │   ├── ca-on-hamilton-plumbing-emergency.csv
    │   │   ├── ca-on-mississauga-plumbing.csv
    │   │   └── negatives-master.csv
    │   ├── ad-copy-briefs.md
    │   ├── bid-strategy.md
    │   ├── budget-plan.md
    │   ├── google-ads-api-wiring.md
    │   ├── offline-conversion-spec.md
    │   ├── scripts/
    │   │   └── upload-offline-conversions.py   # generated for the user
    │   └── creative/
    │       ├── copy-variants/{campaign}/{adgroup}.md
    │       └── generated/{campaign}/{variant}.{png,mp4}   # post-accept copies
    ├── seo/                                # v0.2 stub outputs
    │   ├── keyword-research.md
    │   ├── content-calendar.md
    │   └── (others stubbed)
    ├── lifecycle/                          # v0.2 stub outputs
    │   ├── onboarding-flow.md
    │   └── (others stubbed)
    ├── positioning/                        # /marketing:positioning outputs
    │   ├── positioning.md                  # THE canonical one-pager
    │   ├── messaging-hierarchy.md
    │   ├── competitive-alternatives.md
    │   ├── awareness-ladder.md
    │   └── strategic-narrative.md
    ├── analytics/                          # v0.2 stub outputs
    │   ├── event-taxonomy.yaml
    │   └── (others stubbed)
    ├── briefs/                             # /marketing:paid output (creative-ops brief mode)
    │   ├── brief-google-search.md
    │   ├── brief-google-pmax.md
    │   ├── brief-meta-static.md
    │   ├── brief-meta-reels.md
    │   ├── brief-tiktok.md
    │   └── brief-youtube.md
    ├── candidates/                         # USER drops externally generated assets
    │   ├── google-search-1/                # round 1
    │   │   ├── 01-nano-banana-pro-flooded-basement.png
    │   │   └── (5-15 files typical)
    │   ├── meta-static-1/
    │   ├── meta-reels-1/
    │   │   └── 01-veo-5s-emergency-plumber.mp4
    │   └── google-search-2/                # round 2 after refinement
    ├── selected/                           # /marketing:select-creative outputs
    │   ├── google-search-1.md              # winners + rejected + rationale
    │   ├── meta-static-1.md
    │   └── meta-reels-1.md
    ├── decisions/                          # locked picks per channel
    │   ├── google-search.md
    │   ├── meta-static.md
    │   └── meta-reels.md
    ├── campaigns/                          # /marketing:ship-campaign outputs
    │   ├── live/
    │   │   └── {campaign-id}.yaml          # snapshot of live state
    │   └── archived/
    ├── experiments/                        # A/B test registry
    │   └── {experiment-id}/
    │       ├── hypothesis.md
    │       ├── srm-check.md
    │       └── results.md
    ├── leads/                              # → sales-plugin handoff
    │   └── inbound-{date}.csv
    ├── attribution/                        # ← sales-plugin feedback
    │   └── closed-loop-{date}.csv
    └── .secrets/                           # gitignored
        └── google-ads.yaml                 # OAuth credentials
```

Every markdown file has a fixed header: `Generated-by:`, `Depends-on:`, `Sources-cited:`. The `marketing-status` skill validates these on every run.

## The brief-and-judge loop for ad creative

The visual creative phases for paid channels are not one-shot. Each runs as a `brief → generate externally → drop → select → decide` cycle, repeated until the user accepts a winner. The plugin's job is to make every loop iteration cheap and well-rationalized. There are exactly three exits from a selection.

```
            ┌────────────────────┐
            │  /marketing:paid   │
            │  (brief mode)      │
            │  creative-ops      │
            └─────────┬──────────┘
                      │
                      │ writes briefs/brief-<channel>.md
                      ▼
            ┌────────────────────┐
            │  USER takes brief  │
            │  to external tools │
            │  (Nano Banana Pro, │
            │   Veo, Higgsfield, │
            │   MJ, Recraft...)  │
            │  generates 5-15    │
            │  candidates        │
            └─────────┬──────────┘
                      │
                      │ drops to candidates/<channel>-<round>/
                      ▼
            ┌────────────────────────────┐
            │  /marketing:select-creative│
            │  <channel> <round>         │
            │  creative-ops (selection)  │
            │  multimodal scoring        │
            │  six-dimension rubric      │
            └─────────┬──────────────────┘
                      │
                      │ writes selected/<channel>-<round>.md
                      ▼
            ┌────────────────────┐
            │  USER reviews      │
            │  selected/<...>.md │
            └────────┬───────────┘
                     │
        ┌────────────┼────────────────────┐
        │            │                    │
        ▼            ▼                    ▼
  ┌──────────┐ ┌────────────┐  ┌─────────────────────┐
  │  ACCEPT  │ │  REFINE    │  │  REFINE POSITIONING │
  │ creative │ │   BRIEF    │  │  (upstream fix)     │
  └──────────┘ └────────────┘  └─────────────────────┘
       │              │                    │
       │              │                    │
       ▼              ▼                    ▼
  decisions/    briefs/brief-           positioning/
  <channel>.md  <channel>.v2.md         positioning.md
       │              │                  (revised)
       │              │                    │
       │              ▼                    ▼
       │       round N+1                 reset all
       │       in candidates/            affected
       │                                  channels to
       │                                  round 1
       │
       ▼
  /marketing:ship-campaign
```

1. **Accept.** User is satisfied with one of the winners. Runs `/marketing:paid --accept-creative <channel>-<round> --winner <filename>`. The winning file is copied from `candidates/<channel>-<round>/` into `paid/creative/generated/{campaign}/`, a `.meta.md` sidecar is written linking back to the selection rationale, and `decisions/<channel>.md` is written capturing the locked decision with citations. The channel pointer advances and the user is ready to ship.

2. **Refine brief.** Winners are close but not right. User runs `/marketing:paid --refine-brief --channel <channel>` with notes. The `creative-ops` agent rewrites the brief — usually adjusting visual direction, tool mix, per-tool prompts, or the awareness-stage targeting — and writes `briefs/brief-<channel>.v2.md`. Round number bumps. User generates round 2, drops into `candidates/<channel>-2/`, runs `/marketing:select-creative <channel> 2`, decides again.

3. **Refine positioning.** The selection rationale shows the misalignment is upstream of creative — the awareness-stage targeting is wrong, or the message hierarchy is inverted, or the ICP is mis-scoped. User re-runs `/marketing:positioning` to revise `positioning.md` and `awareness-ladder.md`, then re-runs `/marketing:paid` against the revised positioning. All candidates from the old rounds are preserved for audit; round counters reset to 1.

There is no upper bound on rounds. Creative is inherently iterative. The plugin tracks rounds in `decisions/` and never auto-progresses without explicit user intent.

## The Google Ads API push flow

The Google Ads API push is the second iteration loop in the plugin and the one with dollar consequences. Hard safeguards at every step.

```
┌──────────────────────┐
│ paid/                │
│   campaign-structure │
│   .md                │
│   keywords/*.csv     │
│   ad-copy-briefs.md  │
│   bid-strategy.md    │
│   budget-plan.md     │
└──────────┬───────────┘
           │
           │ /marketing:ship-campaign --account primary
           ▼
┌──────────────────────────────────┐
│  PRE-FLIGHT VALIDATION           │
│  - parse all paid artifacts      │
│  - sum(daily_budgets) ≤ monthly  │
│    budget / 30                   │
│  - no single campaign > 40% of   │
│    total daily spend             │
│  - account is not SUSPENDED      │
│  - OAuth refresh token valid     │
│  - developer token approved      │
│  → BLOCK on any failure          │
└──────────┬───────────────────────┘
           │
           │ all checks pass
           ▼
┌──────────────────────────────────┐
│  DRY-RUN PRINT                   │
│  - prints full intended state    │
│    change (campaigns, ad groups, │
│    keywords, ads, budgets)       │
│  - prompts user for "push"       │
│    confirmation                  │
└──────────┬───────────────────────┘
           │
           │ user types "push"
           ▼
┌──────────────────────────────────┐
│  GOOGLE ADS API PUSH (PAUSED)    │
│  - MutateOperation batches       │
│  - all entities created in       │
│    PAUSED state                  │
│  - prints created entity IDs     │
│  - writes campaigns/live/        │
│    {campaign-id}.yaml snapshot   │
└──────────┬───────────────────────┘
           │
           │ user logs into Google Ads UI
           ▼
┌──────────────────────────────────┐
│  HUMAN VISUAL REVIEW             │
│  - confirms structure, copy,     │
│    keywords, budget, geo,        │
│    schedule all look right       │
└──────────┬───────────────────────┘
           │
           │ /marketing:ship-campaign --account primary --enable
           ▼
┌──────────────────────────────────┐
│  GO-LIVE FLIP                    │
│  - re-validates account is not   │
│    SUSPENDED                     │
│  - flips PAUSED → ENABLED        │
│  - prints confirmation           │
│  - logs to campaigns/live/       │
└──────────────────────────────────┘
```

Every step is an explicit gate. There is no `--yes-skip-prompts` flag in v0.1. Even non-interactive automation has to invoke the two commands separately and confirm both. This is by design and not a config knob.

## Reentrancy contract

Every skill is idempotent on its inputs. Re-running a skill overwrites only its own outputs and leaves unrelated files untouched. Concretely:

- `/marketing:research` overwrites `research/*-research.md` and nothing else.
- `/marketing:positioning` overwrites `positioning/*.md` and nothing else.
- `/marketing:paid` (default) overwrites `paid/campaign-structure.md`, `paid/keywords/*.csv`, `paid/ad-copy-briefs.md`, `paid/bid-strategy.md`, `paid/budget-plan.md`, `paid/google-ads-api-wiring.md`, `paid/offline-conversion-spec.md`, and `briefs/brief-<channel>.md` for each in-scope channel. It does NOT touch `candidates/`, `selected/`, `decisions/`, `paid/creative/generated/`, or any other sub-vertical.
- `/marketing:paid --refine-brief --channel C` overwrites only `briefs/brief-C.v<next>.md` — never an existing round's brief, never any candidate file, never any locked decision.
- `/marketing:paid --accept-creative <channel>-<round> --winner <filename>` writes `paid/creative/generated/`, `decisions/<channel>.md`, and the `.meta.md` sidecar — and nothing else.
- `/marketing:select-creative C R` writes `selected/C-R.md` and nothing else.
- `/marketing:plan` overwrites `plan.md`, `plan-adrs/ADR-*.md` (only newly added), and `open-questions.md`.
- `/marketing:ship-campaign` writes only `campaigns/live/{campaign-id}.yaml` and Google Ads API state. Local files mutate only on the snapshot.
- `/marketing:seo`, `/marketing:lifecycle`, `/marketing:analytics` (v0.1 stubs) overwrite their respective sub-vertical directories only.

Verify by running `git diff` after a re-run. Any unexpected file touch is a bug.

The user can exit and resume at any phase. `/marketing:status` shows where they are.

## Three unhappy paths

**Unhappy path 1 — Google Ads API push fails.** `/marketing:ship-campaign` validates and prints intended state, the user confirms, the plugin makes the API call, and Google returns an error. Possible causes: developer token not approved for the customer account, OAuth refresh token expired, daily quota exceeded, account suspended, ad copy rejected by policy preview, geo target invalid for the account. The plugin catches each of these and prints a structured error: which check failed, which fix to try, and which file to re-edit. No partial state is committed — the plugin uses the Google Ads API's atomic mutation batches, so either the entire campaign creates or none of it does. The user fixes the underlying issue (often a re-OAuth or a policy-friendly ad-copy rewrite), re-runs `/marketing:ship-campaign`, and tries again. The reentrancy contract guarantees this is safe.

**Unhappy path 2 — creative-ops selection rejects all candidates.** User generates 12 candidates for `meta-static-1`, drops them, runs `/marketing:select-creative meta-static 1`, and the selected file says "no winner crosses the minimum threshold; all 12 candidates score below 18/30." The recommendation will point the user at one of the three exits (accept, refine brief, refine positioning) based on which dimensions failed. If brand alignment scores are uniformly low, the brief was probably weak on the voice quote — refine the brief. If awareness-stage match scores are low across the board, the positioning's awareness-ladder is the problem — refine positioning. If craft scores are low but everything else passed, the tool mix was wrong — refine the brief and switch tools. The plugin tracks the rejection rationale in `selected/meta-static-1.md` so the next round's brief can explicitly avoid the failure modes. Three rounds is normal for a new channel; five rounds is not pathological for a fast-moving creative team.

**Unhappy path 3 — campaigns underperform after going live.** User runs the campaign for two weeks, the cost-per-billable-call is 3x the target, and the user backtracks. The plugin's job at this point is not to "auto-optimize" — it is to surface what to revisit. `/marketing:status` prints a campaign-health report showing actual CPC, CTR, conversion rate, and cost-per-conversion against the bid-strategy stage's expected ranges (per Wordstream benchmarks cited in `research/paid-research.md`). If the CTR is fine but the conversion rate is low, the landing page is the problem (out of plugin scope — fix in greenfield). If the CTR is low, the ad copy or creative is the problem — refine the brief and run a new creative round. If both are fine but the cost is too high, the bid strategy is too aggressive for the conversion volume — drop a stage on the Brad Geddes ladder. If the awareness ladder is mismatched (e.g., the ad targets problem-aware but the keyword set is solution-aware), back up to `/marketing:positioning` and revise. The plugin makes the diagnosis explicit; the user picks the fix and re-runs the affected commands. The reentrancy contract means this never corrupts state.

All three unhappy paths are supported and expected. The plugin tolerates the user's real workflow rather than forcing a happy-path-only contract.
