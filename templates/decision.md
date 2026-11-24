---
type: decision
summary: {one line: what was decided}
updated: {YYYY-MM-DD}
kind: {opportunity | scope | launch | outcome-review | pricing | strategy | goal | other}
---

# {Decision}

- Date decided: {YYYY-MM-DD}
- Decided by: {name or role}
- How decided (optional): {decider after discussion | consent | majority | unanimity | decider alone | delegated to {who}}
- Input from (optional): {names or roles}
- Reversible: {easily | at a cost | no}
- Recorded: {at the time | reconstructed on {YYYY-MM-DD} from [[{source}]]}
- Status: {active | replaced by [[{decision}]] | reversed on {YYYY-MM-DD} (see [[{decision}]])}
- Replaces: [[{decision}]] | none
- Reopened because (required when it replaces a decision): {new information} (see [[{source}]])

## Decision

{What was decided.} (see [[{source}]])

## Why

- {reason} (see [[{source}]])

## Known at decision

Locked. When the decision is reconstructed, list only what the source shows
was known then.

- Evidence: [[{problem, analysis, experiment or customer}]]
- Biggest unknown: {what we didn't know}
- {the kind block below}

## Options not chosen

- Do nothing: {why not} (or "not possible: {why}")
- {option}: {why not}

## Expected result

- Expect: [[{metric}]] from {baseline} to {target} by {YYYY-MM-DD} | direction only | no metric: {why}
  - Target from: {baseline + expected lift | funnel sizing [[{analysis}]] | past launch or period [[{page}]] | benchmark [[{source}]] (external) | set by leadership ({who}) | team guess ({who}) | direction only}
- Confidence (optional): {low | medium | high}
- Watch: [[{metric}]], check on {YYYY-MM-DD}

## Revisit when

- If {observable signal} (by {YYYY-MM-DD}), then {review | kill | scale back | other action}

## Affects

- [[{feature, problem, customer, goal or strategy}]]

## Reviews

- {YYYY-MM-DD}: result {as expected | better | worse | unclear}; decision given what was known {sound | flawed: why} (see [[{source}]])

## Contradictions

None.

<!--
Kind blocks. Put the one that matches `kind` under "Known at decision".

opportunity:
- Size at decision: {copy of the problem's Size section, with its As of date}
- Goal served: [[{goal}]]

scope:
- Feature: [[{feature}]] (its Success metrics hold the expected result)

launch:
- Experiment: [[{experiment}]], result by its rule: {succeeded | not successful | failed | inconclusive} | none
- Followed the rule: {yes | overridden because {reason}}
- Go: {on {YYYY-MM-DD} | delayed to {YYYY-MM-DD} because {reason} | killed}
- Tier and audience at decision: {tier}, [[{customer}]]

outcome-review:
- Reviews: [[{decision}]] for [[{feature}]]
- Verdict: {iterate | scale | kill}

pricing:
- Existing customers: {grandfathered | migrated on {YYYY-MM-DD} | moved at renewal | not affected}
- Cost to serve (optional): {from a source only}

strategy:
- From [[{strategy}]] to [[{strategy}]]; choice that changed: {which}

goal:
- Goal: [[{goal}]], replaced by [[{goal}]] | committed goal missed
- What changed or why it was missed: {reason}

other: no block.
-->
