---
type: concept
summary: Judge a feature or test by one value metric, explain it with usage metrics, and protect what must not break with guardrails.
updated: 2026-11-24
knowledge_source: ingested
---

# Primary, secondary and guardrail metrics

## What it is

A method for proving that a feature delivered its intended result "while also not wreaking havoc elsewhere in the product" (Avi Siegel, Momentum). Primary metric (value indicator): did it solve the problem it was built for? For a bulk-edit feature that is time saved, not usage. Secondary metrics (usage indicators): adoption, time to first use, return usage. Guardrail metrics: what must not get worse, such as conversion, page load time, support tickets or the cloud bill. The same structure appears in nearly every experimentation source. (see [[2026-11-24-research-digest-metrics]])

## How to use it

- Set a success threshold and a failure threshold for each metric before launch, for example "at least 25% less time to completion" and "conversion down 5% against an expected 0%" (Siegel). (see [[2026-11-24-research-digest-metrics]])
- "Not successful" isn't "failure": less impact than hoped may still be worth keeping; making things worse may mean removing it (Siegel). (see [[2026-11-24-research-digest-metrics]])
- Build tracking, dashboards and a baseline before the feature (Siegel). (see [[2026-11-24-research-digest-metrics]])
- Plan check-ins before launch: daily guardrails in week 1, weekly value and adoption reviews in weeks 2 to 4, monthly in months 2 and 3, a full analysis at quarter end (Siegel; no evidence offered for the schedule). (see [[2026-11-24-research-digest-metrics]])
- Counter-metric examples: conversion vs return rate; support tickets vs CSAT; ad clicks vs retention (Gupta). (see [[2026-11-24-research-digest-metrics]])

## Watch out for

- Adoption alone doesn't prove value (Siegel). (see [[2026-11-24-research-digest-metrics]])
- When several teams ship into the same area, correlation isn't causation (Siegel). (see [[2026-11-24-research-digest-metrics]])

## Contradictions

- Statsig puts guardrails inside its "primary" group; GrowthBook and Contentsquare keep them separate (see [[2026-11-24-research-digest-experiments]]).
- "Secondary" means usage indicators to Siegel but metrics that explain the primary's drivers to The Product Space. (see [[2026-11-24-research-digest-metrics]])

## Pairs well with

- [[north-star-framework]]: the metric feature metrics roll up to
- [[experiment-design-doc]]: where the three kinds get written down

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[measure-what-matters]]
- [[product-analytics-for-dummies]]

## Topics

- [[goals-and-metrics]]
- [[product-experimentation]]
