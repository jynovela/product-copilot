# Expected write-tickets result

Checked against `skills/write-tickets/SKILL.md`. Build the test repo with
`setup.sh --seeded`. Run three prompts, each in a new session.

## Prompt A: approved scope

```text
Write tickets for offline mode.
```

### Must do

- [ ] Step 2 reports "approved by [[approve-offline-mode-scope]]".
- [ ] Gathers the decision, the problem pages under "Problems it
      addresses", and the metric pages in Success metrics. Says no PRD
      exists in `documents/` (the PRD is a raw source, not a document).
- [ ] Slices the First slice first: the first ticket is closing a job
      offline with notes, then sync. Other In items (view jobs, photos,
      parts, signature) follow; Later isn't ticketed.
- [ ] Writes `documents/<date>-tickets-offline-mode.md` with
      `doc_type: tickets` and `status: draft`, one `## T<n>` per ticket,
      every heading present, `- None` where empty, and `## Built from` at
      the end.
- [ ] Every criterion is Given/when/then with something a person can see.
      Details the scope doesn't give (messages, limits, how long a job can
      stay unsynced) end with `(assumption)` and are listed.
- [ ] Each Out item a ticket could drift into appears under that ticket's
      Out of scope: creating jobs offline, editing the schedule offline,
      the Android tablet app.
- [ ] The constraint on the page (Q3 goal said launch by 2026-09-30) shows
      up somewhere, or the report says it no longer applies because the
      feature launched on 2026-10-01.
- [ ] The open question "how long can a job stay unsynced" becomes a Spike
      or an Open questions line, not an invented limit.
- [ ] The report has all six headings and ends with `RESULT: 0 errors`.

### Must not do

- [ ] Name files, endpoints, tables or functions.
- [ ] Use a vague word from the skill's list in a criterion ("works",
      "is saved", "handles", "correctly").
- [ ] Put `[[links]]` in ticket text.
- [ ] Use a real-looking customer name or contact detail in examples.

## Prompt B: no scope decision

```text
Write tickets for multi-day jobs.
```

### Must do

- [ ] Step 2 reports "not approved": the feature page says "Approved by:
      not approved yet".
- [ ] Tells the user and offers to record a scope decision. Stops there,
      or, only if the user then says to go ahead, writes tickets from the
      In list with a title starting "Draft:". The In list is "not set", so
      a draft should say there's nothing to ticket yet or ask for the In
      list.
- [ ] Mentions the evidence is one account (thin), from the problem page.

### Must not do

- [ ] Write normal tickets as if the scope were approved.
- [ ] Invent the In list, a first slice or a decider.
- [ ] Record a scope decision itself, as a person or as `copilot
      (unconfirmed)`, without the user asking. (This prompt isn't a run
      without stopping.)

## Prompt C: work outside the scope

```text
Write a ticket to fix jobs that show up twice after an offline sync.
```

### Must do

- [ ] Finds the offline mode page and sees the fix isn't in its In list.
- [ ] Doesn't put it in a ticket as scope. It lists it under Open
      questions, or offers the record workflow for a new scope decision,
      and says why.
- [ ] Cites the evidence: the beta support ticket of 2026-09-21.

### Must not do

- [ ] Create, change or move a ticket in any tool.

## Scoring

Count the boxes. Any miss under a "Must not do" fails the run.
