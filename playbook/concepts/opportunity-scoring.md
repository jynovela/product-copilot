---
type: concept
summary: Rank customer outcomes by how important they are and how poorly they are served today.
updated: 2026-11-24
knowledge_source: model-memory
---

# Opportunity scoring

## What it is

General knowledge: From Anthony Ulwick's Outcome-Driven Innovation. Customers rate how important each desired outcome is and how satisfied they are with current solutions. Outcomes that are important and poorly served are the best opportunities. Ulwick's formula is importance + max(importance - satisfaction, 0).

## How to use it

- Write outcomes as measurable results the customer wants, not as features.
- Survey enough customers in one segment.
- Plot importance against satisfaction and look at the important, unsatisfied corner.

## Watch out for

- Rating features instead of outcomes.
- Mixing segments whose needs differ.

## What the framework articles say

These are vendor and practitioner articles, not neutral sources.

- Customers rate importance and satisfaction; gives the formula as importance + max(importance - satisfaction, 0), then as importance + (importance - satisfaction). (see [[atlassian-6-prioritization-frameworks]])
- Comes from Ulwick's Outcome-Driven Innovation; plot satisfaction against importance; respondents over- or understate importance. (see [[tempo-9-prioritization-frameworks]])
- Features high in importance but low in satisfaction offer the best return on development work. (see [[productplan-37-pm-frameworks]])

## Contradictions

- Atlassian gives two different formulas in the same article: one floors the gap at zero, one doesn't (see [[atlassian-6-prioritization-frameworks]]). General knowledge: Ulwick's version floors it at zero, so an over-served outcome doesn't get a negative score.

- Opportunity scoring surveys many customers to rate outcomes. Competing Against Luck says jobs insights come from many data points about a few people, not a few data points about many, and that stories lose meaning when broken into variables (Competing Against Luck ch2, ch5; see [[2016-10-04-clayton-christensen-competing-against-luck]]). Find the job with interviews ([[jtbd-switch-interview]]) before scoring its outcomes.

## Pairs well with

- [[jobs-to-be-done]]: outcomes are measures of how well a job gets done
- [[kano-model]]: another survey-based way to sort needs
- [[value-proposition-canvas]]: pains and gains to score

## From

- [[what-your-customer-wants-and-cant-tell-you]]
- [[the-lean-product-playbook]]

## Topics

- [[discovery-and-customer-insight]]
- [[decisions-and-data]]
- [[product-frameworks]]
