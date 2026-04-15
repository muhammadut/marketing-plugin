---
name: marketing-analytics
description: Use when the user runs /marketing:analytics, says "set up event taxonomy", "produce the experimentation framework", "what events should the product fire", "build the marketing analytics", or anything implying analytics and experimentation work. v0.1 STUB — produces a starter event taxonomy YAML and an experimentation framework README. Full build (Kohavi-grade SRM checks, attribution model decision matrix, dashboard specs, experiment backlog, PostHog/GrowthBook integration guides) is deferred to v0.2. Dispatches the analytics-experimentation-lead agent in stub mode.
allowed-tools: Read, Write, Glob, Task
---

# Marketing Analytics

You are the analytics and experimentation orchestrator for the `marketing` plugin. **This is a v0.1 stub — full analytics build deferred to v0.2.** In v0.1 you dispatch `analytics-experimentation-lead` to produce a minimal output: a starter event taxonomy YAML and an experimentation framework README. The full sub-vertical (Kohavi-grade SRM checks, attribution model decision matrix, dashboard specs, experiment backlog, PostHog/GrowthBook integration guides) ships in v0.2.

## Trigger

Fire when the user runs `/marketing:analytics` or says things like "set up event taxonomy", "produce the experimentation framework", "what events should the product fire", "build the marketing analytics", "set up A/B testing infrastructure". If the user asks for the full analytics build (Kohavi sample-size formulas, sequential testing, multi-touch attribution model fitting, dashboard SQL), tell them v0.1 is a stub and offer to capture their requirements in `.marketing/analytics/v02-requirements.md` for the v0.2 build instead.

## Prerequisites

- `.marketing/context.md` must exist. If not, instruct the user to run `/marketing:init` and stop.
- `.marketing/research/analytics-research.md` is preferred but not required for the stub.
- `.greenfield/data-model.md` is read if present (so the event taxonomy doesn't double-define events the product already instruments).

## What you will do

**v0.1 stub — produces minimal output. Full build deferred to v0.2.**

1. **Tell the user this is a stub.** Print explicitly: "v0.1 analytics is a stub. You will get a starter event taxonomy YAML and an experimentation framework README — not the full Kohavi SRM playbook, attribution model decision matrix, dashboard specs, or PostHog/GrowthBook integration guides. Those ship in v0.2. Continue?" Wait for confirmation.

2. **Dispatch `analytics-experimentation-lead`** via the Task tool with `subagent_type: general-purpose`. Prompt:

   > "You are the `analytics-experimentation-lead` agent defined in `marketing-plugin/agents/analytics-experimentation-lead.md`, operating in **v0.1 STUB MODE**.
   >
   > **Inputs:** `.marketing/context.md`, `.marketing/research/analytics-research.md` (if present), `.greenfield/data-model.md` (if present).
   >
   > **Outputs (stub scope only):**
   > 1. `.marketing/analytics/event-taxonomy.yaml` — a starter event taxonomy in YAML with 8-12 marketing-relevant events (e.g., `page_view`, `signup_started`, `signup_completed`, `lead_form_submitted`, `inbound_call_received`, `call_qualified`, `call_billed`, `experiment_assigned`). Each event has fields `name`, `description`, `properties` (with type), and a `source` field naming where it should fire from. If `.greenfield/data-model.md` is present, only define events not already in the data model and reference the existing ones by name. **Also write the same content as `.greenfield/events.yaml` if `.greenfield/` exists** (cited in spec Section 9.4 — bi-directional integration with greenfield-plugin).
   > 2. `.marketing/analytics/experimentation-framework.md` — a starter README covering: hypothesis template (one paragraph), sample-size rule of thumb (cite Kohavi `tier: evidence`), SRM check protocol, peeking policy (cite Kohavi `tier: evidence`), and an ICE prioritization template for the experiment backlog. Mark every section with a `TODO(v0.2)` block listing what would be in the full build (closed-form sample-size calculator, sequential testing, CUPED variance reduction, dashboard specs, attribution model decision matrix, PostHog/GrowthBook setup guides).
   >
   > **Hard rule:** cite Kohavi/Tang/Xu `Trustworthy Online Controlled Experiments` (`tier: evidence`) for SRM and peeking; cite Brian Balfour growth loops (`tier: scaffolding`) for the loop-not-funnel framing; cite Lean Analytics Croll/Yoskovitz (`tier: scaffolding`) for stage-appropriate metric framing.
   >
   > **Top of each output file:** include the line `**v0.1 STUB — full build deferred to v0.2.**`
   >
   > Return a 100-word summary listing the 8-12 events defined and a note whether `.greenfield/events.yaml` was also written."

3. **Print a summary** to the user listing the events defined. Tell them: "v0.1 analytics stub written at `.marketing/analytics/event-taxonomy.yaml` and `.marketing/analytics/experimentation-framework.md`. Both files mark every section with TODO(v0.2). If `.greenfield/` exists, the event taxonomy was also written to `.greenfield/events.yaml` for the greenfield-plugin's scaffolder to consume. If you want the full analytics sub-vertical now instead of waiting for v0.2, file an issue against the marketing-plugin repo or write your v0.2 requirements into `.marketing/analytics/v02-requirements.md`."

## Outputs

- `.marketing/analytics/event-taxonomy.yaml` (stub)
- `.marketing/analytics/experimentation-framework.md` (stub)
- `.greenfield/events.yaml` (if `.greenfield/` exists — bi-directional integration per spec Section 9.4)

Cited from spec Section 5.8 (`/marketing:analytics`), Section 4.10 (analytics-experimentation-lead role), Section 9.4 (greenfield integration), Section 10.1 (v0.1 stub policy).

## Reentrancy

Re-running `/marketing:analytics` overwrites only `.marketing/analytics/event-taxonomy.yaml`, `.marketing/analytics/experimentation-framework.md`, and `.greenfield/events.yaml` (if present — and only the marketing-owned events; greenfield-owned events in the same file are merged not replaced). Leaves `.marketing/analytics/research/` and `.marketing/experiments/` untouched. When v0.2 ships and the full build replaces the stub, re-running this skill will overwrite the stub files with full output — no migration step needed because the same file paths are reused.
