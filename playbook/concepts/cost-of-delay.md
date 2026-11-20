---
type: concept
summary: Put a value on what each week of waiting costs, and use it to order work.
updated: 2026-11-20
knowledge_source: model-memory
---

# Cost of delay

## What it is

General knowledge: From Don Reinertsen's product development flow work, popularized by Joshua Arnold. Cost of delay is the value lost per unit of time an item isn't delivered. Dividing cost of delay by duration (CD3) gives a score: do the highest first. It makes urgency explicit and in money.

## How to use it

- Estimate value per week for the top items only; rough ranges are enough.
- Rank by cost of delay divided by duration.
- Watch for items whose value drops sharply after a date.

## Watch out for

- False precision on value estimates.
- Debating numbers without agreed ground rules.

## What the framework articles say

These are vendor and practitioner articles, not neutral sources.

- Estimate revenue per unit of time, estimate time to implement, divide the first by the second; the result is "the cost to the company for not pursuing the project". (see [[atlassian-6-prioritization-frameworks]])
- Joshua Arnold's definition; ask what a feature is worth now, how much more if earlier, and what each week of waiting costs; example: $30,000 vs $10,000 per week of delay with equal build time, so the first goes first. (see [[tempo-9-prioritization-frameworks]])
- Dividing impact per week by duration gives "cost of delay divided by duration", or CD3; example: $1,000 a week over 2 weeks gives 500. (see [[2025-07-04-contentsquare-prioritization-frameworks]])

## Contradictions

- Atlassian divides value per unit of time by build time and calls the result the cost of not doing the project (see [[atlassian-6-prioritization-frameworks]]). Contentsquare does the same division and correctly calls it CD3 (see [[2025-07-04-contentsquare-prioritization-frameworks]]). General knowledge: the cost of delay is the value per week itself, which is how Tempo uses it (see [[tempo-9-prioritization-frameworks]]); CD3 is the ranking score.

## Pairs well with

- [[theory-of-constraints]]: both look at flow and where waiting costs most
- [[rice-scoring]]: ranks by value but ignores time

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[the-goal]]

## Topics

- [[decisions-and-data]]
- [[product-frameworks]]
