---
name: write-tickets
description: Turn a feature's approved scope, or a whole plan or architecture doc, into epics and user stories with exact, observable acceptance criteria, as Markdown ready to paste into Linear or Jira. Use when the user asks for tickets, stories, epics, a backlog or acceptance criteria.
---

# write-tickets

You turn one feature into tickets an engineering team can pick up, as
Markdown the user pastes into their tracker. You never create, change or
move tickets in a tool.

Tickets say what a user can do or see when the work is done, never how to
build it. Engineers choose the build. You don't read the codebase, so you
never name files, endpoints, tables or functions.

## Which path

- **A feature** with a page in `wiki/features/`: follow the steps below.
- **A plan**: an architecture doc, an implementation plan, a build order,
  a big idea, or any ask for epics. Follow `from-a-plan.md`. It writes
  epics, stops for the user's OK, then writes stories for coding agents,
  and it may name what the plan defines.

**Output:** the path and why.

## Steps

1. **Find the feature.** Open its page in `wiki/features/`. If there is no
   page, offer the record workflow first and stop. **Output:** the page
   and its `updated` date.
2. **Check the scope.** Read the feature's Scope section.
   - Approved by a `scope` decision (any `Decided by`, including
     `copilot (unconfirmed)`): go on.
   - Not approved: tell the user, and offer to record a scope decision.
     If they want tickets anyway, write them from the In list and start
     the file's title with "Draft:".
   **Output:** "approved by [[decision]]" or "not approved".
3. **Gather.** Read what the tickets rest on: the decision pages the Scope
   cites, the problem pages under "Problems it addresses", the newest PRD
   or demo spec in `documents/` for this feature, and the metric pages in
   Success metrics. Open only those. **Output:** the pages and documents
   read, with dates.
4. **Slice.** Break the First slice into stories first, then Later only if
   the user asks. Each story is one thing a user can do, working end to
   end. Order them so the first one can ship and be tried alone.
   **Output:** the ticket titles in build order.
5. **Write the tickets.** Run `date +%F`. Create
   `documents/<YYYY-MM-DD>-tickets-<feature slug>.md` from
   `templates/document.md` with `doc_type: tickets` and `status: draft`.
   Write one `## T<n>` section a ticket, in the format below.
   **Output:** the path and the number of tickets by type.
6. **Check each ticket against the rules below.** Fix what fails.
   **Output:** each fix, or "None".
7. **Humanize.** Run `skills/humanize-check` in `--mode light` on the
   file and fix what it finds outside criteria lines. **Output:** its
   one-line report.
8. **Check.** Run `python3 tools/lint_wiki.py` and fix every `ERROR` on
   the file. **Output:** the final `RESULT` line.
9. **Report:**

    ```text
    ## Tickets report: <feature>
    ### File
    ### Scope status
    ### Tickets
    ### Assumptions
    ### Open questions
    ### Lint result
    ```

## Ticket types

- **Story:** something a user can do or see. Most tickets are stories.
- **Measure:** the data a success metric needs, when the metric page says
  there is no way to count it yet. The criteria say what number someone
  can read and where, never how to log it.
- **Spike:** a question that must be answered before a story can be
  written, with a timebox of 3 days or less. It ends in a written answer.

Leave technical tasks (migrations, refactors, new services) to engineering.
If a story clearly needs one, say so under the story's Open questions.

## Format

````markdown
## T1: Export this month's orders to a spreadsheet

Type: Story
Story: As an ops lead, I want to download this month's orders as a CSV file, so that I can reconcile them in my spreadsheet.

### Context

Ops leads copy orders out by hand every week (2026-11-03 call with Acme).
Part of the first slice approved on 2026-11-20.

### Acceptance criteria

- C1: Given a shop with orders this month, when the ops lead clicks
  "Export" on the Orders page, then a file named `orders-2026-11.csv`
  downloads with one row per order shown on the page.
- C2: Given the file from C1, when it's opened in a spreadsheet, then the
  columns are, in order: order number, date, customer name, total.
  (assumption)
- C3: Given a shop with no orders this month, when the ops lead clicks
  "Export", then the page shows "No orders to export this month" and
  nothing downloads. (assumption)

### Out of scope

- Exports for a custom date range (Later in the scope).

### Depends on

- None

### Assumptions

- C2: the column order isn't in the scope or PRD.
- C3: the exact message is mine.

### Open questions

- Should refunded orders appear in the file?
````

A Measure ticket has `Type: Measure` and a `Metric:` line naming the
metric page instead of the `Story:` line. A Spike has `Type: Spike`, then
`Question:` and `Timebox:` lines, and `### Expected answer` instead of
`### Acceptance criteria`. Keep every heading in every ticket, with
`- None` under any that is empty. Context may cite wiki pages in words and
dates, as above, but never with `[[links]]`: the text gets pasted into a
tracker. List the pages under `## Built from` at the end of the file.

## Rules

- **Story line.** In the user's words, with no product jargon. One goal:
  no "and" in the "I want" part. If you need "and", split the story.
- **Who.** A role from the customer or account pages, never "user" when
  the pages name who it is.
- **Criteria.** Given, when, then. The "when" is something a person does
  in the product. The "then" is what they can see or check: exact text on
  screen, a file and its contents, a number, an email they receive. Put
  exact text in quotes and values in backticks.
- **Count.** Give a Story or Measure 1 to 5 criteria, numbered C1, C2, ...
  More than 5 means the story is too big: split it.
- **Assumptions.** Any detail the scope, PRD, demo spec or decisions
  don't give (a message, a limit, an order, a format) ends with
  `(assumption)` and is listed under Assumptions.
- **Vague words.** Never in a criterion: fast, easy, simple, intuitive,
  user-friendly, seamless, properly, correctly, appropriate, should, works,
  handles, as expected, "an error", "is saved", "is updated", "succeeds".
  Name what the person sees instead. A speed goal becomes a number marked
  `(assumption)`, like "the file downloads within `5` seconds for `1000`
  orders".
- **Scope.** Ticket only the In list (or Later, if asked). Each Out item a
  ticket might drift into goes under that ticket's Out of scope. Ideas the
  scope doesn't mention go under Open questions, never into a ticket.
- **Constraints.** Each constraint on the feature page shows up as a
  criterion or an Out of scope line in at least one ticket.
- **Depends on.** Only tickets this one can't be built or tried without.
  "Comes after" is not a dependency.
- **Data.** No real customer data or contact details in examples. Use
  made-up names and values.
- Tickets record nothing. If writing them surfaces a decision or a new
  fact, offer the record workflow.
- A new version is a new file with a new date. Set `status: final` only
  when the user says the tickets are ready.
