---
type: concept
summary: Put a value on what each week of waiting costs, and use it to order work.
updated: 2026-11-24
knowledge_source: ingested
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

## What Escaping the Build Trap adds

Source note: from secondary summaries of the book, not the book text. Chapter numbers are the book's.

- Perri's preferred prioritization method once the strategic outcomes are
  clear (Build Trap ch19).
- For a first release, treat scope as an optimization: cut scope enough to
  capture the most value soon, but not so far that a poor release loses
  early adopters, who are hard to win back (ch19). Over-scoping costs
  revenue and lets a competitor in (ch19).
- Perri also uses Joshua Arnold's business value model when setting
  strategic intents (ch13). See [[strategy-deployment]].

## Contradictions

- Atlassian divides value per unit of time by build time and calls the result the cost of not doing the project (see [[atlassian-6-prioritization-frameworks]]). Contentsquare does the same division and correctly calls it CD3 (see [[2025-07-04-contentsquare-prioritization-frameworks]]). General knowledge: the cost of delay is the value per week itself, which is how Tempo uses it (see [[tempo-9-prioritization-frameworks]]); CD3 is the ranking score.

## Pairs well with

- [[theory-of-constraints]]: both look at flow and where waiting costs most
- [[rice-scoring]]: ranks by value but ignores time

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[the-goal]]

Ingested:

- [[escaping-the-build-trap]] (from secondary summaries
  [[2020-11-17-swamy-seetharaman-escaping-the-build-trap-summary]] and
  [[bookey-escaping-the-build-trap-summary]]; `chN` = book chapter)

## Topics

- [[decisions-and-data]]
- [[product-frameworks]]
