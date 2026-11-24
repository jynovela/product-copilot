# write-tickets: from a plan

Use this path when the input is a plan, not a feature page: an
architecture doc, an implementation plan, a build order, a roadmap, or a
big idea in a doc or in chat. It also applies when the user asks for
epics. You break the plan into epics, stop for the user's OK, then break
each approved epic into stories.

The stories are for coding agents as well as people. An implementer builds
from them, and a test agent writes a failing test from each criterion
before the code exists. So every criterion must be something you can check
on the running app.

The rules in `SKILL.md` still apply (format, story line, criteria, count,
assumptions, vague words, depends on, data), except where this file says
otherwise.

## What changes from the feature path

- **Source.** The plan and the docs it names as where requirements live,
  in any repo or folder the user points to. Nothing in `wiki/` is needed.
  A plan is intent, not fact: never say something is built unless the
  code shows it.
- **Names.** Criteria may name what the source defines: endpoints,
  pages, commands, tables, error codes, roles. Cite where each comes from
  under Context. Never invent one. If a story needs a name the source
  doesn't give, write the criterion in product terms and mark it
  `(assumption)`.
- **Criteria target the running app.** The "when" is something a person
  does in the product, or a request a client sends. The "then" is what
  anyone can check: text on a page, an HTTP status and a body field, a row
  and its value, a file, an email. Never "given a mock".
- **Task type.** Add **Task** for groundwork with no direct user, like
  setting up the repo or the API layer, when the plan lists it as a step.
  Its criteria are still observable: a command and its output, a request
  and its status. Give it `Type: Task` and no `Story:` line.
- **The target project's rules win.** If the source repo says how stories
  are written (extra headings, title format, where fixed values live,
  "cite the row, don't copy the value"), follow it over this file and say
  so in the report. Add its extra headings after Assumptions.
- **Existing tickets.** If the source says tickets already exist (IDs, a
  tracker project), list them in the epics file and ask whether the new
  set replaces them, adds to them, or is only a comparison. Never write
  over or into the tracker.

## Steps

1. **Find the source.** Read the plan, then each doc it names as a source
   of requirements. Note the repo, branch and commit, or the file dates.
   **Output:** the files read, with commit or dates.
2. **Check what exists.** Look for code and for existing tickets the
   source mentions. **Output:** "no code yet" or what exists, and the
   existing tickets, or "None".
3. **List what the plan commits to.** One line each, with an ID (`P1`,
   `P2`, ...) and where it comes from (file and section). Then read the
   requirement docs for anything the plan skips: list each as a gap with
   an ID (`G1`, ...). List contradictions between docs as conflicts.
   **Output:** plan items, gaps, conflicts.
4. **Group into epics.** An epic is one outcome a user or the owner can
   see when it's done, usually 3 to 8 stories. Order by what each needs
   first. The first epic should give the owner something to try. Mark an
   epic **Blocked** when it needs a decision or an outside step (an
   account, a license, a value marked open) before stories can be built,
   and name what. **Output:** the epic titles in build order.
5. **Write the epics file.** Run `date +%F`. Write
   `documents/<YYYY-MM-DD>-epics-<slug>.md` from `templates/document.md`
   with `doc_type: epics` and `status: draft`, unless the user names
   another place. Use the epic format below. End with "Not covered",
   listing every plan item and gap that no epic covers, with the reason.
   **Output:** the path and the epic count.
6. **Stop for the OK.** Show the user the epic titles, what each covers,
   the gaps you added, the conflicts and blocked epics. Ask them to
   approve, change, merge or drop epics. Write no stories until they
   answer. **Output:** "waiting for OK".
7. **Write the stories.** For the approved epics, in build order, write
   `documents/<YYYY-MM-DD>-tickets-<slug>.md` in the `SKILL.md` format,
   plus an `Epic: E<n>` line under `Type:`. Number tickets across the
   whole file (T1, T2, ...), grouped by epic. Skip Blocked epics unless
   the user asks; their stories carry the blocker as the first line of
   Context. **Output:** the path and tickets per epic.
8. **Check, humanize, lint and report** as in `SKILL.md` steps 6 to 9.
   Add `### Epics` and `### Gaps added` to the report.

## Epic format

```markdown
## E1: Students can register and pay

Outcome: A visitor can create an account, pay with a test card and see the course start page.
Covers: P7, P8, G2
Status: Ready

### In

- Registration with the identity fields in the product doc.
- Stripe Checkout and the webhook that creates the enrollment.

### Out

- Refunds (E7).

### Depends on

- E2

### Stories

- Register with email and identity details
- Pay and land on the course start page
- See the waiting page until payment is confirmed

### Open questions

- The course price is not set yet.
```

`Status` is `Ready` or `Blocked: <what>`. Keep every heading, with `- None`
under any that is empty.

## Rules

- **Coverage.** Every plan item and every gap is in an epic or under "Not
  covered" with a reason. A gap you add is a proposal: say so.
- **One outcome.** No "and" in an epic's Outcome that joins two things a
  user does. Split instead.
- **Stories still slice end to end.** A story that only adds a table or
  an endpoint no one uses is a Task, and only when the plan lists it.
- **Don't decide for the owner.** A value the source marks open or
  undecided (a price, a limit, a policy) becomes an open question, never a
  number in a criterion, not even as an assumption.
- **Don't change the source.** Never edit the plan, the source repo or
  the tracker. Suggested changes to the plan go under Open questions.
