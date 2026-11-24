---
type: concept
summary: Decide before launch how big an effect you need to detect, with what confidence and power, and so how many users and days.
updated: 2026-11-24
knowledge_source: ingested
---

# Sample size, power and minimum detectable effect

## What it is

Before an experiment, set the significance level (often 95%), power (usually 80 to 90%), the minimum detectable effect (MDE: the smallest change worth detecting or shipping) and the baseline rate and variance; together they give the sample size and duration. At 95%, about 1 in 20 metrics with no real effect will look significant (Statsig, Conversion.com). (see [[2026-11-24-research-digest-experiments]])

## How to use it

- Write down the baseline rate, MDE, weekly traffic and stop rules before launch (Product HQ). (see [[2026-11-24-research-digest-experiments]])
- For guardrails, the MDE is the largest regression you are willing to miss (Statsig). (see [[2026-11-24-research-digest-experiments]])
- Run the calculation under several assumptions and take the largest (PLOS). (see [[2026-11-24-research-digest-experiments]])
- If runtime is too long: test a bolder change, cut variants, choose a more sensitive metric, narrow to a high-intent audience, raise allocation, or use a non-experiment method (Product HQ, GrowthBook, Statsig). (see [[2026-11-24-research-digest-experiments]])
- Raise the bar above 95% for high-risk tests such as pricing (Conversion.com). (see [[2026-11-24-research-digest-experiments]])

## Watch out for

- Small studies that do find an effect tend to overestimate it (PLOS). (see [[2026-11-24-research-digest-experiments]])
- Separate practical from statistical significance: is the lift big enough to pay for its maintenance? (Product HQ) (see [[2026-11-24-research-digest-experiments]])
- No source gives a worked calculation; all point to calculators (digest section 6). (see [[2026-11-24-research-digest-experiments]])

## Contradictions

- Significance as a gate: 95% by convention, raised for high risk (Conversion.com, Contentsquare), vs report exact p-values, don't split at 0.05, and use p < 0.005 for novel claims (PLOS). (see [[2026-11-24-research-digest-experiments]])

## Pairs well with

- [[ab-testing]]: what it sizes
- [[statistical-traps]]: the wider list of ways numbers mislead

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[how-to-lie-with-statistics]]
- [[designing-with-data]]

## Topics

- [[product-experimentation]]
