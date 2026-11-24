---
type: concept
summary: Checking results early and stopping on a good number inflates false wins, unless you chose a sequential method upfront.
updated: 2026-11-24
knowledge_source: ingested
---

# Peeking and sequential testing

## What it is

Peeking is checking an experiment early and stopping when a variant looks ahead; it raises false positives (Contentsquare, PostHog, Product School). Fixed-horizon testing sets the sample upfront and reads once, with the most power. Sequential testing lets you look as often as you like, at the cost of wider intervals and less power, and can stop clear winners or losers sooner (GrowthBook). (see [[2026-11-24-research-digest-experiments]])

## How to use it

- Choose fixed-horizon or sequential before launch and write it in the design doc. (see [[2026-11-24-research-digest-experiments]])
- With sequential testing, still plan the sample (PostHog); check health at days 1, 3 and 7, then weekly (Statsig). (see [[2026-11-24-research-digest-experiments]])
- Set the readout window upfront, for example "first 14 full days" (Statsig). (see [[2026-11-24-research-digest-experiments]])
- Check mechanics during the run, not results (Product School). (see [[2026-11-24-research-digest-experiments]])

## Watch out for

- When a bug harms users, stop, fix and restart; if only logging broke, keep it live and reset the duration from the fix (Statsig). (see [[2026-11-24-research-digest-experiments]])
- Changing the audience percentage mid-test makes it a new iteration (LaunchDarkly). (see [[2026-11-24-research-digest-experiments]])

## Contradictions

- Never look before the planned end (Product School, Contentsquare, Planio, Candu) vs look as often as you like with sequential methods (GrowthBook, PostHog, Statsig, Flagsmith). Compatible if the method is chosen upfront. (see [[2026-11-24-research-digest-experiments]])

## Pairs well with

- [[sample-size-and-power]]: sets the planned end
- [[ab-testing]]: where peeking happens

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[how-to-lie-with-statistics]]

## Topics

- [[product-experimentation]]
