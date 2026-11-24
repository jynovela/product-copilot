---
type: experiment
summary: {one line: what we tested and what happened}
updated: {YYYY-MM-DD}
status: {planned | running | done | stopped}
---

# {Experiment name}

## Context

- Why now: {reason} (see [[{source}]])
- Owner: {name or role}
- Evidence bar: {directional is enough | strong evidence needed} (because {reason})

## Hypothesis

If {who} gets {change}, then [[{metric}]] will {rise | fall} by {amount},
because {reason}.

- Would be proven wrong by: {result}

## What it tests

- Assumption: {assumption}
- Risk: {value | usability | feasibility | viability}
- Solution: [[{feature}]]
- Problem: [[{problem}]]

## Method

- Type: {interview | usability test | fake door | landing page | concierge or Wizard of Oz | prototype | A/B | multivariate | staged rollout | pre/post (directional only)}
- Why this type: {reason}
- Audience: [[{customer}]], {how many, how chosen}
- Unit and control (A/B only): {user | account | session}, {control}
- Change tested: {what differs}
- Overlapping tests: {none | [[{experiment}]]}
- Setup check: {A/A test | pilot | tracking check | none}
- Planned length: {days or sample size, whichever takes longer}

## Metrics and decision rule

Set before the start. Never edited once status is running; to change it,
stop this experiment and start a new page.

- Primary (one decides): [[{metric}]], baseline {n} (see [[{source}]]), normal variance {n}, {leading | lagging}
- Secondary (explain why): [[{metric}]]
- Guardrails: [[{metric}]] must stay within {range}
- A/B only: significance level {n}, minimum detectable effect {n}, {fixed length | sequential testing}
- Stop early only if: {condition}
- Decision: {result} -> ship; {result} -> iterate; {result} -> re-scope; {result} -> kill
- Target from: {baseline + expected lift | funnel sizing [[{analysis}]] | past launch or period [[{page}]] | benchmark [[{source}]] (external) | set by leadership ({who}) | team guess ({who}) | direction only}

## Deviations

None.

## Result

- Primary: {value} (see [[{source}]])
- Secondary and guardrails: {values} (see [[{source}]])
- Segments: {values} (see [[{source}]])
- Setup checks: {passed | failed: what}
- What people did or said: {summary} (see [[{source}]])
- Outcome: {succeeded | not successful | failed | inconclusive}

## Learning and next step

- Inference: {what we learned}
- Next: [[{decision}]] or [[{experiment}]]

## Contradictions

None.
