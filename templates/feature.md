---
type: feature
summary: {one line: what it does}
updated: {YYYY-MM-DD}
---

# {Feature name}

## What it does

{Description.} (see [[{source}]])

## Status

{idea | planned | building | in beta | launched | removed} (see [[{source}]])

- Plan: {plan name | add-on at {price} | all plans} (see [[{source}]] or [[{decision}]])

## Problems it addresses

- [[{problem}]]

## Scope

Locked once a `scope` decision approves it. A later change is a new
`scope` decision (action `re-scope`), not an edit.

- Approved by: [[{decision}]] | not approved yet
- First slice: {the smallest version that tests the riskiest assumption} (see [[{source}]])
- In: {what this version does} (see [[{source}]])
- Out (non-goals): {what it deliberately won't do, and why} (see [[{source}]])
- Later: {what may come after the first slice} | none
- Constraints: {deadlines, platforms, legal, dependencies} (see [[{source}]]) | none known
- Open questions: {what is still unknown} | none

## Success metrics

Set before build. Locked at launch: after that, add dated Deviations lines
and judge results against the original thresholds.

- Goal it serves: [[{goal}]]
- Why this should move the goal: {one line}
- Owner: {name or role}
- Primary (value; one decides): [[{metric}]], baseline {n} (see [[{source}]]), normal variance {n}, {leading | lagging}
  - Success if: {threshold}
  - Failure if: {threshold}
  - Target from: {baseline + expected lift | funnel sizing [[{analysis}]] | past launch or period [[{page}]] | benchmark [[{source}]] (external) | set by leadership ({who}) | team guess ({who}) | direction only}
- Adoption (secondary): share of {audience} using it at {7 | 14 | 30} days; success if {threshold}
- Guardrails: [[{metric}]] must stay within {range}
- Segments to check: {segments}
- Evidence of cause: {A/B [[{experiment}]] | staged rollout | before/after (directional)}
- Check dates: guardrails {YYYY-MM-DD}; adoption {YYYY-MM-DD}; value {YYYY-MM-DD}; final review {YYYY-MM-DD}

## Launch

- Tier: {1 (announced widely) | 2 (told to affected customers) | 3 (release note only) | silent}
- Audience: [[{customer}]], regions {regions} | everyone
- Rollout (dated, added as it happens):
  - {YYYY-MM-DD}: {internal | invite-only beta with {who, how many} (see [[{experiment}]]) | open to {segment} | {n}% of {audience} | general availability}
- Launched: {YYYY-MM-DD}, the first day the target segment could use it without an invitation
- Announced: {channels} on {YYYY-MM-DD} (see [[{source}]]) | not announced
- Message: {one line} (pillar: {which messaging pillar, if any})
- Teams briefed: {support | sales | docs | success} on {YYYY-MM-DD} | not needed
- Launch decision: [[{decision}]] | none (tier 2 or 3, no test)
- Launched with: [[{feature}]] | none (in a bundled launch, the lead feature holds this section)

## Deviations

None.

## Results at check dates

- {YYYY-MM-DD}: [[{metric}]] {value} vs success {n} / failure {n} (see [[{source}]])
  - Segments: {values} (see [[{source}]])
  - Other changes in that window: {launches, price changes, campaigns} (see [[{page}]])
  - What people did or said: {summary} (see [[{source}]])
- Verdict at final review: {succeeded | not successful | failed | inconclusive}
- Next: [[{decision}]]

## Feedback

- {qualitative feedback} (see [[{source}]])

## Contradictions

None.
