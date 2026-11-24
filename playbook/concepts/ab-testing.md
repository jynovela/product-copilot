---
type: concept
summary: Randomly split users between a control and one or more variants and compare a pre-chosen metric; the workhorse of online experiments.
updated: 2026-11-24
knowledge_source: ingested
---

# A/B testing

## What it is

A randomized controlled experiment: split users at random between a control and one or more variants, change one thing, and compare a metric chosen beforehand. Called the "workhorse" of product experimentation (Product School, Flagsmith, Userpilot). A multivariate test changes several elements in combination to find interactions and needs much more traffic. (see [[2026-11-24-research-digest-experiments]])

## How to use it

- Write the hypothesis, primary metric, guardrails, sample size and duration before launch. (see [[2026-11-24-research-digest-experiments]])
- Randomize as close to the experience as possible, keep assignment across sessions, and include only users the change can affect (GrowthBook, PostHog). (see [[2026-11-24-research-digest-experiments]])
- Run an A/A test or a small 5% rollout first to check the setup; a broken launch can't be cleanly rerun (GrowthBook, PostHog). (see [[2026-11-24-research-digest-experiments]])
- Cover at least a full weekly cycle and avoid unusual periods (Product School, Contentsquare, Simon Cast). (see [[2026-11-24-research-digest-experiments]])
- Check sample ratio mismatch before reading results; if the split is off, fix and rerun (Contentsquare). (see [[2026-11-24-research-digest-experiments]])
- Segment the results (device, new vs returning, traffic source), but treat segment wins as new hypotheses. (see [[2026-11-24-research-digest-experiments]])

## Watch out for

- Needs traffic; underpowered tests give false results. On low traffic, use fake doors, concierge tests or staged rollouts instead (Product HQ). (see [[2026-11-24-research-digest-experiments]])
- Small tweaks tend to give 1 to 2% gains and can trap you at a local maximum (Department of Product, Simon Cast, Murray). (see [[2026-11-24-research-digest-experiments]])
- Running overlapping tests on the same users contaminates both (Planio). (see [[2026-11-24-research-digest-experiments]])
- "No evidence of impact" is not "proof of no impact" (Product HQ). (see [[2026-11-24-research-digest-experiments]])

## Contradictions

- Multivariate tests: Userpilot says they usually give more insight than A/B; Simon Cast, Mind the Product and GrowthBook say they need far more traffic and suit only optimizing near a known peak. (see [[2026-11-24-research-digest-experiments]])

## Pairs well with

- [[sample-size-and-power]]: how long it must run
- [[peeking-and-sequential-testing]]: when you may look
- [[staged-rollout]]: the release-safety cousin

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[designing-with-data]]
- [[the-lean-startup]]

## Topics

- [[product-experimentation]]
