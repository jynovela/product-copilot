---
type: concept
summary: Goals describe a change in user or business behaviour, not the feature you will ship; keep the work separate from the measure.
updated: 2026-11-24
knowledge_source: ingested
---

# Outcomes over outputs

## What it is

An outcome is a change in human behaviour that creates impact; an output is an artefact such as a feature or report; impact is the business or mission effect of outcomes (Herbig, after Josh Seiden's *Outcomes Over Output*). Nearly every goal source says goals and key results should be outcomes, and the work that should move them (initiatives) should be listed separately. (see [[2026-11-24-research-digest-goals]])

## How to use it

- airfocus's test: if a key result can be satisfied by doing a task regardless of impact, it is a work plan; if only evidence that the outcome happened satisfies it, it is an OKR. (see [[2026-11-24-research-digest-goals]])
- Rewrite in four steps: what user behaviour changes a month after launch, why it is stuck today, which metric measures that bottleneck, and which guardrail must hold (interview-prep site). (see [[2026-11-24-research-digest-goals]])
- Example rewrite: "Ship 5-step onboarding wizard by May 15" becomes "cut p80 time-to-first-published-project from 6 days to 1.5 days by June 30", guardrail "Day-30 retention of activated teams ≥ 78%". (see [[2026-11-24-research-digest-goals]])
- Rephrase a key result as "How might we…?" to catch premature feature talk (Herbig). (see [[2026-11-24-research-digest-goals]])
- Write the roadmap after the goals, so it answers which work is most likely to create the outcome (airfocus). (see [[2026-11-24-research-digest-goals]])

## Watch out for

- Most vendor example OKRs break their own outcome rule ("Hire 5 salespeople", "Launch 12 new features"); don't copy them. (see [[2026-11-24-research-digest-goals]])
- Use percentiles where slow tails cause churn: an average of 4 days hid a 13-day 80th percentile in the LedgerPulse example. (see [[2026-11-24-research-digest-goals]])

## What Escaping the Build Trap adds

Source note: from secondary summaries of the book, not the book text. Chapter numbers are the book's.

- Feature launches, specs, backlogs and smooth execution are outputs.
  They don't create value by themselves (Build Trap ch1).
- Features shipped and story points are productivity metrics, not product
  metrics, because they can't tie development back to the business (ch16).
- A feature is done when it reaches its goal, not when it ships (ch19).
- Reward people for outcomes, learning about users and finding good
  opportunities (ch21). Leaders who still count features shipped undo the
  change (ch20).
- Goals should be outcome-oriented, actionable and clearly communicated
  throughout the company (Build Trap appendix). See [[build-trap]].

## Contradictions

- Strict: key results must be outcomes (Google's rules, Perdoo, airfocus, WorkBoard). Pragmatic: launch or output key results are fine sometimes, such as with no baseline or when starting out (Herbig, Digit's "ship KRs" with counter-metrics, Productboard citing Doerr, Murphy's milestone key results). Google's own re:Work page lists "ship feature Y" as a good endpoint. (see [[2026-11-24-research-digest-goals]])

## Pairs well with

- [[build-trap]]: the failure mode it guards against
- [[okrs]]: where the rule is most often applied
- [[primary-secondary-guardrail-metrics]]: the guardrail half

## From

Inference: these books cover the same job; the framework itself may not appear in them.

- [[radical-focus]]

Ingested:

- [[escaping-the-build-trap]] (from secondary summaries
  [[2020-11-17-swamy-seetharaman-escaping-the-build-trap-summary]] and
  [[bookey-escaping-the-build-trap-summary]]; `chN` = book chapter)

## Topics

- [[goals-and-metrics]]
