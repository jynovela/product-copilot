# Type: PRD

`doc_type: prd`. Humanize mode: full.

**Reader:** the engineers, designers and stakeholders who will build or
approve the feature. **They decide:** whether to build this first slice,
and what it must do.

## Read first

- The feature page: What it does, Status, Problems it addresses, Scope,
  Success metrics, Launch.
- Each problem page it addresses: Problem, Who has it, Evidence, Size.
- The customer and account pages for who has the problem.
- The goal page the feature serves.
- Experiment pages that tested its assumptions, and the `scope` decision
  that approved its Scope, if there is one.
- Competitor pages only when the problem page names them.

If there is no feature page, offer to create one with the record workflow
first. If the user wants the PRD anyway, write it from what they said and
put "none: written from chat on {date}" under Built from.

## Sections

1. **Summary.** Three or four sentences: what we're building, for whom, why
   now, and how we'll know it worked.
2. **Problem.** Who has it, what it costs them, and the evidence, with own
   and public counts kept apart. One or two short quotes at most.
3. **Goal and success metrics.** The goal it serves, then the primary
   metric with baseline, success and failure thresholds, and where the
   target came from, all from the feature page. Guardrails. "Direction
   only" when the page has no number.
4. **Scope.** First slice, In, Out (non-goals, each with its reason), and
   Later, from the feature page's Scope.
5. **How people will use it.** The main flows in plain steps, or short
   user stories. No acceptance criteria: `write-tickets` writes those.
6. **Constraints and dependencies.** Dates, platforms, legal, other teams.
   Optional.
7. **Risks.** The riskiest assumption and how it was or will be tested.
8. **Open questions.** Every gap from step 4, with who can answer it.
9. **Decision status.** "Scope approved by {who} on {date}", or "Scope not
   approved yet". When it's not approved, start the title with "Draft:".

## Type rules

- Scope and metrics come from the feature page. If the PRD needs a change
  to them, list it under Open questions. The change itself is a `scope`
  decision a person makes.
- Say what the feature must do, never how to build it.
