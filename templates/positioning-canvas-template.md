# Positioning Canvas — <project-name>

Generated-by: positioning-lead
Depends-on: .marketing/context.md, .marketing/research/positioning-research.md, .brand/voice.md
Sources-cited: knowledge/positioning/dunford-10-step.md, knowledge/positioning/schwartz-awareness-levels.md, knowledge/positioning/raskin-strategic-narrative.md

A Dunford-style 10-step positioning canvas. Each step has a single deliverable. Cite April Dunford "Obviously Awesome" (tier: scaffolding) for the methodology and the order. The canvas is the input to `messaging-hierarchy.md`, `awareness-ladder.md`, `competitive-alternatives.md`, and `strategic-narrative.md`. Every other agent in the marketing plugin reads `positioning.md`, which is the human-facing one-pager *derived* from this canvas — but the canvas is the auditable working file.

## Step 1. Understand the customers who love your product

> Dunford step 1: identify the segment of customers who already buy and love what you have. These are your "best-fit" customers, not your aspirational customers.

**Best-fit customer profile (today, not aspirational):**

- **Role / function:** <e.g., "Hamilton-area homeowner with a flooded basement at 11pm on a Saturday">
- **Trigger event:** <what just happened that makes them search? e.g., "burst pipe, sewage backup, no hot water in winter">
- **Constraints they live under:** <budget, urgency, technical literacy, language>
- **What they currently use to solve the problem:** <e.g., "Google search 'plumber near me', call 4-5 numbers, take whoever answers first">
- **Why they choose us over alternatives (in their words):** <one or two real customer quotes if available, or the closest synthesized version>

If no real customer data exists yet (cold-start), write `[hypothesis]` next to each line and cite the source of the hypothesis in `.marketing/research/positioning-research.md`.

## Step 2. Form a positioning team

> Dunford step 2: positioning is a cross-functional decision. List the stakeholders.

**Stakeholders for this positioning decision:**

- <person 1: role, decision authority>
- <person 2: role, decision authority>
- <person 3: role, decision authority>

For solo founders: write "founder (sole authority); will validate against best-fit customer interviews in `<calendar quarter>`."

## Step 3. Align your positioning vocabulary

> Dunford step 3: the team needs shared definitions before debate. Otherwise you argue about the wrong thing.

**Vocabulary glossary:**

| Term | Definition (this project's working definition) |
|---|---|
| ICP | <one sentence — who exactly we serve> |
| Category | <the market category the customer mentally puts us in> |
| Alternative | <what the customer would do *instead of* us — including "do nothing" and "use a spreadsheet"> |
| Differentiator | <a feature or capability we have that alternatives don't> |
| Value | <what the differentiator enables the customer to do that they couldn't before> |
| <add others as needed> | |

## Step 4. List your true competitive alternatives

> Dunford step 4: the alternatives the customer would consider if you didn't exist. NOT a feature comparison grid. Often the biggest alternative is "do nothing" or "use a spreadsheet."

**True alternatives (what customers would do without us):**

1. **<Alternative 1>** — <2-3 sentences. What is it, why customers consider it, where it fails them.>
2. **<Alternative 2>** — <2-3 sentences>
3. **<Alternative 3>** — <2-3 sentences>
4. **Do nothing** — <2-3 sentences. What does the customer's life look like if they keep ignoring the problem? This option must always be listed unless the problem is genuinely binary.>

For elocal_clone Hamilton plumbing: alternatives include (1) calling random plumbers from Google search, (2) HomeStars listings, (3) a neighbor's recommendation via Nextdoor, (4) DIY YouTube fix, (5) waiting until business hours.

## Step 5. Isolate your unique attributes / features

> Dunford step 5: the things you have that the alternatives don't. Capabilities, not value (yet).

**Unique attributes:**

- <Attribute 1 — concrete, observable, falsifiable. Not "best in class." E.g., "Dispatch within 8 minutes guaranteed via the routing engine.">
- <Attribute 2>
- <Attribute 3>
- <Attribute 4>

Each attribute must pass two tests: (1) is it true today, not aspirational? (2) do the alternatives in step 4 NOT have it?

## Step 6. Map the attributes to value

> Dunford step 6: translate "we have X" into "you can do Y you couldn't before." Value is what the customer cares about, not what you built.

| Attribute (from step 5) | Enables this value (for the customer) |
|---|---|
| <Attribute 1> | <Value 1 — what does the customer experience differently? E.g., "You speak to a real plumber within 8 minutes instead of leaving voicemails for 4 different shops."> |
| <Attribute 2> | <Value 2> |
| <Attribute 3> | <Value 3> |
| <Attribute 4> | <Value 4> |

## Step 7. Determine who cares a lot

> Dunford step 7: the value matters most to a specific segment. Not "everyone." Not "small businesses." Specific.

**Best-fit segment (people who care most about the value in step 6):**

- **Demographic / firmographic:** <e.g., "Hamilton homeowners, ages 35-65, single-family residence, household income $60-150k">
- **Psychographic:** <e.g., "Risk-averse, values immediate response over price, low DIY confidence">
- **Why they care more than other segments:** <one to two sentences>
- **Estimated size:** <number, even if rough — Hamilton CMA has ~580k people, ~210k households, of which ~70% are owner-occupied = ~150k addressable households>

## Step 8. Find a market frame of reference

> Dunford step 8: positioning needs a category. The customer needs to know what kind of thing you are before they understand why you're different. Pick the frame deliberately — sometimes the obvious frame is the wrong frame.

**Market category (the frame we're choosing):** <e.g., "Pay-per-call home services marketplace" — NOT "Home services directory" because directories are perceived as passive listings, not active dispatch>

**Why this frame and not the alternatives:**

- **Alternative frame 1:** "<frame>" — rejected because <reason>
- **Alternative frame 2:** "<frame>" — rejected because <reason>

The frame must be a category the customer already understands OR a category we are willing to invest in *creating* (Crossing the Chasm, Geoffrey Moore, tier: scaffolding — category creation is expensive and slow).

## Step 9. Layer on a trend (optional)

> Dunford step 9: if a relevant macro trend is moving in your direction, naming it makes the positioning feel inevitable rather than novel. Optional — do not force one if it's weak.

**Trend (if any):** <e.g., "Decline of trust in random Google search results post-AI-generated SEO spam; consumers increasingly want curated, vetted, accountable services.">

**Source:** <citation — preferably an evidence-tier source from `.marketing/research/positioning-research.md`>

If no defensible trend, write "No trend layered for this positioning. The value stands on its own." Do not invent a trend.

## Step 10. Capture your positioning in a one-pager

> Dunford step 10: synthesize everything above into a single page that the team can read in 60 seconds and that every downstream decision (sales, marketing, product) can reference.

**The positioning one-pager** (this is what gets written to `.marketing/positioning/positioning.md`):

```
For:        <best-fit segment, from step 7>
Who:        <are tired of / struggling with / underserved by — what?>
Our product:  <name and category, from step 8>
Provides:   <unique value, from step 6 — pick the top 2-3>
Unlike:     <true competitive alternatives, from step 4>
We:         <unique attributes that enable the value, from step 5>
```

**Onliness statement (Marty Neumeier, tier: vocabulary-only):**

> Our <category, step 8> is the only <descriptor> that <unique value, step 6> for <segment, step 7>.

## Awareness ladder (Schwartz overlay)

> Eugene Schwartz, *Breakthrough Advertising* (1966), tier: evidence. The five awareness levels of the customer at the moment of contact. Every ad, email, and landing page is written for one level. Mismatched copy is the most common reason for low conversion at otherwise reasonable CPC.

| Stage | Customer mental state | Hook for this project |
|---|---|---|
| **Unaware** | Doesn't know the problem exists | <hook — typically a story or surprising fact, not a sales pitch> |
| **Problem-Aware** | Knows the problem, doesn't know solutions exist | <hook — name the problem in their language; do not yet name the brand> |
| **Solution-Aware** | Knows solutions exist, doesn't know yours | <hook — name the solution category, contrast with alternatives> |
| **Product-Aware** | Knows you exist, hasn't bought | <hook — proof, urgency, removed friction> |
| **Most-Aware** | Has bought before / is a current customer | <hook — upgrade, expansion, retention> |

For paid acquisition, which Schwartz stage you target depends on the channel: Google Search keyword intent typically signals Problem-Aware → Solution-Aware; Meta and TikTok feeds typically reach Unaware → Problem-Aware; retargeting reaches Solution-Aware → Product-Aware. Cite this overlay in `awareness-ladder.md`.

## Strategic narrative (Andy Raskin overlay — optional)

> Andy Raskin, "The Greatest Sales Pitch I've Seen All Year," tier: scaffolding. Five elements of the top-of-funnel narrative. Use this when the positioning needs a story arc, not just a one-pager — typically for content marketing, sales decks, and brand campaigns. Skip for direct-response ads.

1. **Name the big change in the world** — <what just shifted that makes the old way obsolete?>
2. **Name the enemy / the obstacle** — <what stands between the customer and the promised land?>
3. **Tease the promised land** — <what does life look like on the other side?>
4. **Position our capabilities as magic gifts** — <how do we uniquely help the customer cross over?>
5. **Present the best evidence** — <what proof do we have that this works?>

If the project is direct-response only (paid acquisition for pay-per-call), this overlay is optional. Write "Strategic narrative deferred — direct-response only" and skip.

## Validation checklist

Before locking the canvas:

- [ ] Every step has content, not placeholder
- [ ] Best-fit customer is specific (not "small businesses")
- [ ] Alternatives in step 4 include "do nothing" or "current workaround"
- [ ] Unique attributes in step 5 are falsifiable, not "best in class"
- [ ] Value in step 6 is what the customer experiences, not what we built
- [ ] Frame in step 8 has alternatives-rejected reasoning
- [ ] One-pager in step 10 fits on one page
- [ ] Schwartz awareness ladder is populated at all 5 levels (or a documented subset for direct-response only)
- [ ] All citations have tier annotations
- [ ] Canvas reviewed by at least one stakeholder from step 2 (or marked solo-founder)
