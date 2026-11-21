---
type: concept
summary: Score ideas by reach x impact x confidence / effort to rank them against one goal.
updated: 2026-11-20
knowledge_source: model-memory
---

# RICE scoring

## What it is

General knowledge: Intercom's prioritization score. Reach is how many people or events are affected in a period. Impact is the effect per person on the goal, on a small scale (for example 0.25 to 3). Confidence is how sure you are, as a percentage. Effort is person-months. Score = reach x impact x confidence / effort.

## How to use it

- Pick the one goal you are scoring against first.
- Score as a group and write down the reason for each number.
- Use the score to start a discussion, not to end it.

## Watch out for

- False precision: the inputs are guesses.
- Ignoring dependencies and strategic bets that score low.

## What the framework articles say

These are vendor and practitioner articles, not neutral sources.

- Confidence scale of 100%, 80% and 50%; effort is time to execute; can be time-consuming and subjective. (see [[atlassian-6-prioritization-frameworks]])
- Started as Intercom's internal system; doesn't account for dependencies; structured estimation, not prediction. (see [[tempo-9-prioritization-frameworks]])
- Developed at Intercom; ranks ideas by a single combined score. (see [[neal-cabage-21-pm-frameworks]])
- Gives each initiative one score from reach, impact, confidence and effort. (see [[productplan-37-pm-frameworks]])
- For ranking features when engineering capacity is tight. (see [[2026-11-20-juan-pm-frameworks-list]])
- Uses impact in dollars of revenue and confidence as a relative factor (1, 1.5, or 2 if twice as sure); compare items relative to each other rather than chasing exact numbers. (see [[2025-07-04-contentsquare-prioritization-frameworks]])

## Contradictions

- Atlassian, following Intercom, scores confidence as a percentage: 100%, 80% or 50% (see [[atlassian-6-prioritization-frameworks]]). Contentsquare uses a relative factor such as 1, 1.5 or 2 and measures impact in revenue dollars (see [[2025-07-04-contentsquare-prioritization-frameworks]]). General knowledge: Intercom's version uses the percentage and an impact scale of 0.25 to 3. Pick one convention and use it for every item, or the scores can't be compared.

## Pairs well with

- [[ice-scoring]]: a faster version without reach
- [[value-vs-effort-matrix]]: a quicker first pass before RICE
- [[okrs]]: gives RICE the goal to score against
- [[cost-of-delay]]: adds the cost of waiting

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[product-roadmaps-relaunched]]
- [[escaping-the-build-trap]]

## Topics

- [[decisions-and-data]]
- [[product-teams-and-operating-model]]
- [[product-frameworks]]
