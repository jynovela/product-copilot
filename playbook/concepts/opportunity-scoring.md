---
type: concept
summary: Rank customer needs by how important they are and how poorly they are served today, using Olsen's importance versus satisfaction quadrants and value formulas or Ulwick's opportunity score.
updated: 2026-11-24
knowledge_source: ingested
---

# Opportunity scoring

## What it is

Ask customers how important a need is and how satisfied they are with the
solution they use for it. Importance is a problem-space measure, separate
from any solution. Satisfaction belongs to a specific solution, and varies
by product and by customer (Lean Product Playbook ch4). Olsen built his
importance versus satisfaction framework at Intuit; Ulwick's
Outcome-Driven Innovation and gap analysis use the same two inputs (ch4).

Plot importance (vertical) against satisfaction (horizontal) to get four
quadrants (ch4):

| | Low satisfaction | High satisfaction |
| --- | --- | --- |
| **High importance** | Underserved: the best opportunities | Well served: leaders are strong; a feature here is doing its job |
| **Low importance** | Not worth pursuing | Not worth pursuing |

## When to use

- Choosing which needs a new product should target.
- Planning the next version of an existing product.
- Deciding which existing feature to improve.

## Steps

1. **List the benefits.** Write them precisely ([[customer-benefits]]).
2. **Place your hypotheses first.** You can use the framework with a sample
   size of zero: put each hypothesis on the four quadrants, on sticky notes
   if you like, and move them as you learn (ch4).
3. **Ask the questions.** In interviews or a survey (ch4):
   - Importance on a 5-point unipolar scale: not at all, slightly,
     moderately, very, extremely important.
   - Satisfaction on a 7-point bipolar scale, from completely dissatisfied
     through neutral to completely satisfied, about a named solution over a
     set period, such as "rides in the past six months".
   - Importance has no negative, so use a unipolar scale; people can be
     dissatisfied, so satisfaction gets a bipolar scale with a neutral
     middle. Use 5 to 11 choices; research favors 5 points for unipolar and
     7 for bipolar (ch4).
   - Ask your own users the same questions about your product to compare
     against competitors (ch4).
4. **Convert and average.** Map each scale to 0 to 100 percent (for
   example 0, 25, 50, 75, 100) and average per need (ch4).
5. **Score.** Use one of the formulas below.
6. **Pick.** Pursue the needs in the upper left with the highest scores
   (ch4).

## Formulas

With importance (I) and satisfaction (S) as fractions from 0 to 1:

- **Gap analysis:** gap = I − S. Easy, but it treats a gap of 5 on a need
  rated 10 the same as a gap of 5 on a need rated 6 (ch4).
- **Ulwick's opportunity score:** I + max(I − S, 0), on 0 to 10 ratings, so
  scores run 0 to 20. The gap can't go negative, and importance breaks ties.
  Ulwick calls scores above 15 very attractive and below 10 unattractive
  (ch4).
- **Olsen's value delivered:** I × S, the area of the rectangle a point makes
  with the origin (ch4).
- **Olsen's opportunity:** I × (1 − S), the most value you could still add.
  A need at 0.9 importance and 0.3 satisfaction (0.63) offers three times
  the room of one at 0.7 and 0.7 (0.21) (ch4).
- **Value created by an improvement:** I × (S after − S before) (ch4).

Importance caps the value any solution can deliver, which is why to focus
on important needs (ch4). You also add value by meeting more related
needs, ideally more important ones (ch4).

## How the scales move

The satisfaction scale is set by the best solution available. A disruptive
product raises the top of the scale and pushes every old leader to the
left, as each new portable music player did (ch4). Importance stays far
more stable over time (ch4). Kano's needs migrate the same way: see
[[kano-model]].

## Small samples

You don't need thousands of responses. Ask 25 interviewees the same
ratings, and when a large share rate something high or low you've probably
found something that will hold up. Olsen calls this "quant on qual". Use it
with care; statistical significance is not all or nothing (ch4).

## Good and bad signs

- Good: the chosen need sits high and to the left, and the team can say why.
- Good: a feature that scores high on both is left alone (ch4).
- Bad: plots that cut off the axes, so a mid-chart point looks like a
  corner (ch4).

## Pitfalls

- Rating features instead of needs or outcomes.
- Asking people to rate satisfaction with something they haven't used
  (ch4).
- Mixing segments whose needs differ ([[target-customer-and-personas]]).
- Using only gap analysis and ignoring importance (ch4).

## What the framework articles say

These are vendor and practitioner articles, not neutral sources.

- Customers rate importance and satisfaction; gives the formula as importance + max(importance - satisfaction, 0), then as importance + (importance - satisfaction). (see [[atlassian-6-prioritization-frameworks]])
- Comes from Ulwick's Outcome-Driven Innovation; plot satisfaction against importance; respondents over- or understate importance. (see [[tempo-9-prioritization-frameworks]])
- Features high in importance but low in satisfaction offer the best return on development work. (see [[productplan-37-pm-frameworks]])

## Contradictions

- Atlassian gives two different formulas in the same article: one floors
  the gap at zero, one doesn't (see [[atlassian-6-prioritization-frameworks]]).
  Lean Product Playbook confirms Ulwick's version floors it at zero (ch4).
- Opportunity scoring surveys many customers to rate outcomes. Competing
  Against Luck says jobs insights come from many data points about a few
  people, not a few data points about many, and that stories lose meaning
  when broken into variables (Competing Against Luck ch2, ch5; see
  [[2016-10-04-clayton-christensen-competing-against-luck]]). Find the job
  with interviews ([[jtbd-switch-interview]]) before scoring its outcomes.
- Olsen's opportunity formula multiplies (I × (1 − S)); Ulwick's adds
  (I + max(I − S, 0)). They often rank needs alike, but they differ at the
  edges: a fully served need rated 10 for importance scores 10 of 20 on
  Ulwick's scale and zero on Olsen's. This follows from the formulas
  (ch4); the book doesn't compare them.

## Pairs well with

- [[jobs-to-be-done]]: outcomes are measures of how well a job gets done
- [[kano-model]]: another way to sort needs
- [[value-proposition-grid]]: turn the chosen needs into a strategy

## From

- [[the-lean-product-playbook]] (ingested from [[2015-06-01-dan-olsen-the-lean-product-playbook]]; `chN` = chapter)
- [[what-your-customer-wants-and-cant-tell-you]]

## Topics

- [[discovery-and-customer-insight]]
- [[decisions-and-data]]
- [[product-frameworks]]
