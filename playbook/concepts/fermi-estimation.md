---
type: concept
summary: Break an unknowable number into guessable parts and multiply, for an order-of-magnitude answer in minutes.
updated: 2026-11-24
knowledge_source: ingested
---

# Fermi estimation

## What it is

Break a number you can't look up into smaller parts you can guess, and multiply them (noirbook). It gives an order of magnitude quickly, for sizing or for sanity-checking a detailed analysis. noirbook's illustration: about 30M US businesses × 40% B2B × 60% using SaaS × 15% with 10 to 500 staff × 20% with the problem × 10% paying $200+ a month gives 21,600 companies, about $52M a year. (see [[2026-11-24-research-digest-problem-size]])

## How to use it

- Write each input down with its basis and confidence (noirbook rates confidence per line). (see [[2026-11-24-research-digest-problem-size]])
- A solo PM can write a problem statement plus a Fermi estimate in 30 minutes, not 3 days (noirbook). (see [[2026-11-24-research-digest-problem-size]])
- Estimate within one order of magnitude, use buckets instead of false precision, and triangulate against one smaller and one larger known item (Mike Cohn, Mountain Goat Software). (see [[2026-11-24-research-digest-problem-size]])

## Watch out for

- noirbook claims errors "tend to cancel out". Inference: they cancel only when independent and unbiased; teams that like an idea push every input the same way. (see [[2026-11-24-research-digest-problem-size]])
- noirbook's own unsourced claim: teams over-promise impact by 2 to 3x. (see [[2026-11-24-research-digest-problem-size]])

## Pairs well with

- [[tam-sam-som]]: what Fermi estimates often feed
- [[statistical-traps]]: ways the numbers mislead

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[the-art-of-doing-science-and-engineering]]
- [[how-to-lie-with-statistics]]

## Topics

- [[discovery-and-customer-insight]]
