---
type: concept
summary: A button, menu item or page for something that doesn't exist yet, to measure interest before building.
updated: 2026-11-24
knowledge_source: ingested
---

# Fake door test

## What it is

Show a button, menu item or page for a feature or product that doesn't exist yet and measure how many people try it. Also called painted door, smoke test or mock sale. Show "coming soon" or a waitlist; apologize or offer something if someone pays (Huryn, Product School, Flagsmith, Userpilot, LaunchDarkly). (see [[2026-11-24-research-digest-experiments]])

## How to use it

- Use it to tell must-have sales requests from nice-to-haves (LaunchDarkly, Valerie Kroll). (see [[2026-11-24-research-digest-experiments]])
- It answers in about a week whether people notice and want a feature, where a multivariate test would take a month (Flagsmith). (see [[2026-11-24-research-digest-experiments]])
- Start from the hypothesis, not from "I want to run a fake door test" (Mind the Product). (see [[2026-11-24-research-digest-experiments]])

## Watch out for

- A landing page is not necessarily a fake door unless it implies the product exists (Huryn). (see [[2026-11-24-research-digest-experiments]])
- Clicks show interest, not willingness to pay or retention. (see [[2026-11-24-research-digest-experiments]])
- Run it only until you reach the sample size you need, then take it down, so customers don't get annoyed (Lean Product Playbook ch7).

## What Lean Product Playbook adds

- A fake door is a quantitative product test on a live product: add the link or button and measure the share of users who click (ch7).
- The click can lead to a thank-you page that explains the feature isn't built and asks why they'd value it. The cheapest version sends clicks to the generic 404 page (ch7).

## Contradictions

- The research digest lists "smoke test" as another name for a fake door (see [[2026-11-24-research-digest-experiments]]). Olsen separates them: a smoke test is a landing page for a product that doesn't exist (a marketing test), while a fake door sits inside a live product (a product test) (Lean Product Playbook ch7). See [[mvp-test-matrix]].

## Pairs well with

- [[pretotyping]]: the family it belongs to
- [[hypothesis-statement]]: write the click-rate threshold first
- [[mvp-test-matrix]]: where it sits among other MVP tests

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[the-lean-startup]]

Ingested:

- [[the-lean-product-playbook]] (ingested from [[2015-06-01-dan-olsen-the-lean-product-playbook]]; `chN` = chapter)

## Topics

- [[product-experimentation]]
