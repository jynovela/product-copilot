---
name: morning-brief
description: Answer "what do I need to do today?" from the wiki first, then from email, calendar and the task app when they are connected. Use when the user asks for their brief, their day, their priorities or their to-dos, or says done, add or drop for a task.
---

# morning-brief

A short daily brief for the person running the copilot. The wiki comes
first, because it knows what is due: check dates, revisits, goal
check-ins, stale pages. Email, calendar and tasks add today's meetings
and replies when they are connected. The brief is notes, not fact.

## Rules

- Read-only on email, calendar and every other connector. Never send,
  accept, decline, move, label or delete anything.
- If a source isn't connected or fails, say so in one line and carry on
  with the rest.
- Never invent a meeting, email, task, date or person. An attendee the
  wiki doesn't know gets `(guess)` after the role you think they have.
- Nothing from the brief goes onto wiki pages. Anything worth keeping
  becomes one line in `wiki/review-queue.md`, with no quotes from email
  and no contact details.
- The brief saves to `daily/<YYYY-MM-DD>.md`, settings to
  `daily/settings.md`, tasks to `tasks.md`. All three are git-ignored
  because they can hold email content. Never commit them, and never copy
  email text anywhere else.

## First run: setup

Run this when `daily/settings.md` doesn't exist.

1. Read `wiki/ways-of-working.md`, `wiki/now.md` and `wiki/index.md`.
   Check which connectors you can reach (email, calendar, a task app).
   **Output:** one line per connector: connected or not.
2. Ask only what you can't work out, at most four multiple-choice
   questions in one message, recommended answer first: which email
   accounts and calendars to read; where tasks live (a task app, or
   `tasks.md`, recommended when none is connected); email drafts, yes or
   no (recommend no); any extra section. **Output:** the answers.
3. Show the plan in three lines and wait for a yes. Then write
   `daily/settings.md` with the answers. **Output:** the settings file.

## Each run

1. **Date and focus.** Run `date +%F` and note the weekday. Read
   `wiki/ways-of-working.md`, `wiki/now.md` and `daily/settings.md`.
   **Output:** the date, the weekday, and this week's goals from now.md,
   or "now.md is empty".
2. **Due in the wiki.** Run `python3 skills/morning-brief/due.py`. Open
   each line it prints and drop the ones the page shows are done (a
   result is already recorded, a review already happened). Keep the
   rest, newest due date last. **Output:** the kept items with their
   pages, and how many you dropped.
3. **Today's meetings.** From the calendar: time, title, who. For each
   meeting with a customer, account or teammate the wiki knows, add up to
   three prep lines from the wiki: the account's status and open issues,
   the last decision that touches them, what they asked for. No prep for
   events with more than ten people. **Output:** the meetings, or "Calendar
   not connected".
4. **Needs a reply.** From email, the last 24 hours (72 on a Monday):
   messages from real people that ask a question, need a decision or tie
   to a deadline. Skip newsletters, notifications and receipts. Rank by
   deadline, then by whether the sender is in the wiki. One line each:
   who (role and company, no address), what they need, by when.
   **Output:** the list, or "Email not connected".
5. **Tasks.** Due today or overdue, from the task app or `tasks.md`.
   **Output:** the list, or "No task list yet".
6. **Top 3.** Pick three priorities for today from steps 2 to 5, each
   tied to one of this week's goals in now.md. If now.md is empty or its
   week is over, say so and propose three goals for the week, each linked
   to a goal page, and wait for an OK before you write them to now.md. On
   Mondays, always propose the week's three goals. **Output:** the three,
   each with the goal it serves.
7. **Watch and question.** Name one customer, feature or experiment that
   needs attention this week and why. Name one gap in the wiki to fill
   today, such as a missing Decided by or a stale page with no owner.
   **Output:** one line each.
8. **Queue.** For each thing worth keeping (a status an email reports, a
   date a meeting moved), add one line to `wiki/review-queue.md`:
   `- [date] <change> | from: <email from role at company, date> or
   <calendar, date> | confirm: <who>`. Then run
   `python3 tools/lint_wiki.py`. **Output:** the lines added, or "None".
9. **Drafts (only if settings say yes).** Up to five reply drafts for
   step 4, in the voice from "How to write for me" in
   `wiki/ways-of-working.md`, shown in the brief for the person to copy.
   Don't put them in the mail app. **Output:** the drafts, or "Off".
10. **Write the brief** to `daily/<YYYY-MM-DD>.md` and show it:

    ```text
    # Brief for <weekday> <YYYY-MM-DD>
    ## Top 3
    ## Today
    ## Needs a reply
    ## Tasks
    ## Due in the wiki
    ## Watch
    ## Question
    ## Drafts
    ## Sources not connected
    ## Added to the review queue
    ```

    Keep it to one screen: one line per item, no paragraphs. Write
    `None` under an empty heading.

## Task commands

When the person says `done: <task>`, `add: <task> [by <date>]` or
`drop: <task>`, change the task app, or `tasks.md` when none is
connected, and confirm in one line. `tasks.md` holds one line per task:
`- [ ] <task> (due <YYYY-MM-DD>)`, ticked with `[x]` when done. Never add
a task the person didn't ask for; suggest it in the brief instead.

## Never

- Write facts from email, calendar or the brief onto wiki pages.
- Change `wiki/now.md` without the person's OK.
- Put email text, addresses or phone numbers in the wiki, the review
  queue or any committed file.
- Count a meeting or email as evidence about customers. If a customer
  email holds evidence, suggest saving it to `raw/` and ingesting it.
