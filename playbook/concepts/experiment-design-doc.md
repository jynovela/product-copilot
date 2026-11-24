---
type: concept
summary: A one-page plan written before the test: hypothesis, audience, variants, metrics, duration, decision rule and owner.
updated: 2026-11-24
knowledge_source: ingested
---

# Experiment design doc

## What it is

A short document written before an experiment so the decision rule can't move after the results arrive. Product HQ's one-pager: context and evidence; hypothesis; audience and exclusion rules; variant description; primary metric and window; guardrails; duration and power notes; QA checklist; decision rule; and, after the test, result, interpretation, next action and open questions, plus a decision owner. (see [[2026-11-24-research-digest-experiments]])

## How to use it

- Statsig's version adds allocation and an MDE per primary metric, with duration from the longest power calculation. (see [[2026-11-24-research-digest-experiments]])
- Plan the action for every outcome before launch: cheap features may ship on directional evidence, costly ones need strong evidence (GrowthBook, Google). (see [[2026-11-24-research-digest-experiments]])
- Keep a log of every experiment, result and action so nobody repeats one (Simon Cast, Flagsmith, Google). (see [[2026-11-24-research-digest-experiments]])
- Log deviations from the plan (NC3Rs, PLOS). (see [[2026-11-24-research-digest-experiments]])

## Watch out for

- Teams often write metrics into specs and never revisit them (Siegel; see [[2026-11-24-research-digest-metrics]]).
- An experiment informs a human decision; it doesn't make it (Longden, Flagsmith). (see [[2026-11-24-research-digest-experiments]])

## Contradictions

- Who decides: Planio says "implement the results no matter what"; Longden, Flagsmith and PMA say people decide with data as one input. (see [[2026-11-24-research-digest-experiments]])

## Pairs well with

- [[hypothesis-statement]]: the first field
- [[primary-secondary-guardrail-metrics]]: the metrics section
- [[premortem]]: a good check before locking the plan

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[the-lean-startup]]

## Topics

- [[product-experimentation]]
