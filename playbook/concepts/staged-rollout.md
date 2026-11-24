---
type: concept
summary: Release to 1 to 5% first, watch errors and key events, then ramp up or roll back; feature flags separate deploy from release.
updated: 2026-11-24
knowledge_source: ingested
---

# Staged rollout and feature flags

## What it is

A canary, incremental or staged rollout starts with about 1 to 5% of traffic, watches errors, latency and key events, then ramps up or rolls back (Product School, Flagsmith). Feature flags decouple deploying code from releasing it, target segments, and give a kill switch (Wingify, Flagsmith, LaunchDarkly). (see [[2026-11-24-research-digest-experiments]])

## How to use it

- Ramp risky tests from about 10% to 50/50 (Product School). (see [[2026-11-24-research-digest-experiments]])
- Use flags so rollback is easy (Siegel; see [[2026-11-24-research-digest-metrics]]).
- Remove experiment flags and losing variant code after the test (LaunchDarkly, PostHog). (see [[2026-11-24-research-digest-experiments]])
- Check that infrastructure can isolate concurrent experiments before scaling (Flagsmith's "blast radius"). (see [[2026-11-24-research-digest-experiments]])

## Watch out for

- A before/after comparison per slice is not a controlled experiment: Planio says it's usually not recommended, Google calls it directional only, and a GrowthBook customer dropped it because of seasonality. (see [[2026-11-24-research-digest-experiments]])

## Pairs well with

- [[rollout-waves]]: the go-to-market version: alpha, beta, limited release, general availability
- [[ab-testing]]: measures impact; a rollout manages risk

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[designing-with-data]]

## Topics

- [[product-experimentation]]
- [[positioning-and-go-to-market]]
