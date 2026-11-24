---
type: concept
summary: When a measure becomes a target it stops being a good measure; design metrics expecting people to game them.
updated: 2026-11-24
knowledge_source: ingested
---

# Goodhart's law and metric gaming

## What it is

Goodhart's and Campbell's laws, as paraphrased by Hoskin: "every measure which becomes a target becomes a bad measure". David Manheim's peer-reviewed paper gives four causes of metric failure: task-appropriate data is hard to find; correlation is imperfect and collapses at the extremes; non-causal correlates used as incentives create perverse effects; and the goal itself is unknown, incoherent or conflicting. Strategy surrogation is forgetting that a measure is a proxy and treating it as the goal. (see [[2026-11-24-research-digest-metrics]])

## How to use it

- Pre-game the metric: imagine how it will be gamed, like a premortem, and design against it (Manheim). (see [[2026-11-24-research-digest-metrics]])
- Diversify: several measures triangulate a goal (Manheim). (see [[2026-11-24-research-digest-metrics]])
- Pair every growth metric with a guardrail (Gupta; and the LedgerPulse example in [[2026-11-24-research-digest-goals]]). (see [[2026-11-24-research-digest-metrics]])
- Set checkpoints, because metrics drift: overzealous sales show up later as lower repeat sales (Manheim). (see [[2026-11-24-research-digest-metrics]])
- Consider measuring for diagnosis rather than reward when perverse effects outweigh the benefit (Manheim). (see [[2026-11-24-research-digest-metrics]])
- Manheim's design process: understand the system, identify goals, pick which desiderata matter, brainstorm measures, plan how they become metrics, plan revisits. (see [[2026-11-24-research-digest-metrics]])

## Watch out for

- Wells Fargo: aggressive cross-sell targets led to about 3.5 million unauthorized accounts (LSA). (see [[2026-11-24-research-digest-metrics]])
- A limit tends to become the target too, as with flight duty times (Manheim). (see [[2026-11-24-research-digest-metrics]])

## Contradictions

- Tie targets to rewards? NetSuite and 12 Characteristics say yes; Rego, LSA and Manheim warn it distorts behaviour and discourages honest reporting. (see [[2026-11-24-research-digest-metrics]])

## Pairs well with

- [[primary-secondary-guardrail-metrics]]: guardrails as the standard defense
- [[premortem]]: the same move applied to metrics

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[how-to-lie-with-statistics]]
- [[measure-what-matters]]

## Topics

- [[goals-and-metrics]]
- [[decisions-and-data]]
