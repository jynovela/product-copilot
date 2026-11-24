# Type: demo spec

`doc_type: demo-spec`. Humanize mode: light.

**Reader:** an AI builder (Claude Design, Claude Code or similar) and the
PM who hands it over. **They decide:** nothing. The builder must be able
to build the demo without asking a follow-up question.

## Read first

- The feature page and its PRD in `documents/`, if one exists.
- The problem page, for the moment the demo must show being fixed.
- The customer page, for the persona.
- Competitor pages for documented flows, as reference only.
- "Formats I prefer" in ways-of-working.md for look and feel.

## Sections

1. **Goal of the demo.** One sentence: what it must convince whom of.
2. **Audience and setting.** Who watches, live or self-serve, how long.
3. **Persona.** Who the user in the demo is, from the customer page, with
   a made-up name.
4. **Critical user flows.** Numbered steps. Each step: what the user
   does, then what the screen shows.
5. **Screens and states.** For each screen in the flows: its purpose,
   the main elements, and its states (empty, loading, error, success).
6. **Sample data.** Realistic, clearly fake, and the same across screens:
   names, numbers, dates. Never real customers or anything from `raw/`.
7. **Faked and real.** What can be hard-coded and what must actually work.
8. **Look and feel.** Platform, screen size, density, brand colors or "plain
   and neutral". Mark any choice the user didn't give as an assumption.
9. **Out of scope.** What the demo must not include.
10. **The demo works if.** A checklist of things a person can see happen,
    like "after step 4, the approval shows as done on the dashboard".

## Type rules

- Every screen named in a flow appears under Screens and states, and
  every screen there appears in a flow.
- Don't copy a competitor's interface. Describe the job a screen does.
- Precision beats style: exact labels, exact numbers, exact order.
