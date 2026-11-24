---
name: setup-copilot
description: Onboard a new company or a fresh fork of the copilot. Ingests the files already in raw/, then interviews the person in short rounds and writes their answers into the wiki, never into AGENTS.md. Use when the user says set up the copilot, onboard, or start fresh for their company.
---

# setup-copilot

Turns an empty fork into a copilot that knows one company. The company's
facts go into `wiki/` and `raw/` only. `AGENTS.md`, `rules/`,
`workflows/`, `templates/`, `skills/` and `tools/` stay generic, so the
fork can pull later copilot updates without merge conflicts.

## How to ask

- At most three questions per message, one topic each.
- Each question comes with a recommended answer or a draft first, built
  from what the wiki already holds: "I'd put: Crewline, scheduling for
  field service firms. Right?" The person can say yes, fix it, or skip.
- "I don't know" and "skip" are fine answers. Write `unknown` and move
  on. Never fill a field with your own guess.
- Ask only for what the raw files and the wiki don't already say.

## Steps

1. **Look first.** Run `date +%F` and `python3 tools/lint_wiki.py`. Count
   the files in `raw/` the check script lists as not ingested, the pages
   in `wiki/`, and whether `README.md` has a `## Set up for` section.
   In a Git repository, also run `git rev-parse HEAD` and keep the commit
   for step 8. **Output:** one line each. If the README section exists,
   say setup ran before, and offer to fill only the gaps.
2. **Where sources live.** Say this once, before reading any file:
   sources in `raw/` are committed with the wiki, so the repository must
   be private, and the person can say "keep sources local" instead. Don't
   wait for an answer. If they say it, add `raw/*`, `!raw/README.md` and
   `!raw/public/` to `.gitignore`, and tell them cloud sessions and other
   computers won't see the sources. **Output:** "Sources committed" or
   "Sources kept local".
3. **Ingest what's there.** If `raw/` has files not yet ingested, list
   them and offer to ingest them all, oldest first, before any interview,
   because they answer questions you would otherwise ask. On a yes,
   follow `workflows/ingest.md` for each, without stopping. If `raw/` is
   empty, ask for the first files: strategy or planning docs, interview
   notes, a metrics export, a CRM or ticket export. **Output:** the files
   ingested, or the person's answer.
4. **Find the gaps.** Read `wiki/overview.md` and `wiki/index.md`. Check
   each topic below and mark it known, partly known or empty.
   **Output:** the table of topics with their state.

   | Topic | Where the answer goes |
   | ----- | --------------------- |
   | You: name, role, team, what you own | a `person` page, and `wiki/ways-of-working.md` |
   | Company and products | `wiki/overview.md` Product, Product stage |
   | Customers and segments | `customer` pages; overview Target customers |
   | Key accounts | `account` pages |
   | Current goals | `goal` pages; overview Current goals |
   | Strategy | a `strategy` page, only with at least a challenge and where to play; otherwise the overview says "No strategy recorded" |
   | Pricing and plans | overview Pricing table |
   | Competitors | `competitor` pages |
   | Team: who owns what | `person` pages (role, team, areas owned; no contact details or opinions about performance) |
   | Tools the team uses | the connectors list in step 9 |
   | How you work | `wiki/ways-of-working.md` |
   | This month's focus | `wiki/now.md` |

5. **Interview in rounds.** Take the empty and partly known topics in the
   table's order, three questions per message at most, as in "How to
   ask". After each round, save the person's words with
   `workflows/record.md`: one note in `raw/notes/`, then the pages, so
   every chat answer cites a note. Show the pages you'll change and wait
   for a yes before writing, unless the person said to run without
   stopping. **Output:** after each round, the note path and the pages
   changed.
6. **Ways of working and now.** Draft `wiki/ways-of-working.md` (how you
   decide, how to write for you, formats you prefer) and `wiki/now.md`
   (this month's focus and this week's three goals, each linked to a goal
   page) from the answers. Show both and write them after a yes.
   **Output:** both files, or "Skipped".
7. **README block.** Add or update one section in `README.md`, right
   after the first paragraph, and nothing else in the file:

   ```text
   ## Set up for

   - Company: <name>. Product: <name>.
   - Set up: <YYYY-MM-DD> by <name or role>.
   - Company facts live in wiki/ and raw/; AGENTS.md stays generic.
   ```

   **Output:** the block.
8. **Check.** Run `python3 tools/lint_wiki.py` until `RESULT: 0 errors`.
   In a Git repository, run `git diff --stat <commit from step 1> --
   AGENTS.md CLAUDE.md rules workflows templates skills tools`; it must
   print nothing. If it lists a file, undo your change to it. Without
   Git, say the generic files couldn't be compared. **Output:** both
   results.
9. **Connectors.** List the connectors worth adding for the tools the
   person named, and what each feeds. Don't install or configure any.
   **Output:** the table:

   | Tool kind | Feeds | Used by |
   | --------- | ----- | ------- |
   | CRM | account status, plan, owner | sync |
   | Ticket tool (Jira, Linear) | open issues on accounts; feature delivery | sync |
   | Support desk | ticket themes and counts as raw sources | ingest, sync |
   | Product analytics | metric baselines and check-date values | sync |
   | Email and calendar | today's meetings and replies, read-only | morning-brief |
   | Docs and drive | strategy docs, PRDs, notes to put in `raw/` | ingest |

10. **Report:**

    ```text
    ## Setup report: <company>
    ### Files ingested
    ### Notes saved
    ### Pages created
    ### Pages updated
    ### Left unknown
    ### Generic files untouched
    ### Connectors to add
    ### Next steps
    ### Lint result
    ```

    Under Next steps, say how to keep the fork current: add the upstream
    copilot repo as a remote and pull its updates; only the README's
    `## Set up for` section should ever conflict.

## Never

- Write company facts into `AGENTS.md`, `CLAUDE.md`, `rules/`,
  `workflows/`, `templates/`, `skills/` or `tools/`.
- Set a goal, target, price or strategy yourself. Record what the person
  says, with their name as the source.
- Ask for something a raw file or wiki page already answers.
- Copy contact details, passwords or keys into the wiki, even when the
  person types them.
