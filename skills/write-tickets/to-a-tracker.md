# write-tickets: create them in the tracker

Use this file only when the user asks you to put the tickets into their
tracker (Linear, Jira, GitHub Issues or another). Their ask is the
approval. Without it, the tickets stay in the Markdown file.

You only create. You never edit, close, move, relabel or comment on a
ticket that already exists, including ones you created in an earlier run.

## Before you start

- **A finished file.** The tickets file the user has seen, with every
  check in `SKILL.md` passed. For the plan path, the epics file too.
- **A connected tool.** An MCP server or CLI for the tracker that can
  create issues. Without one, say so and stop. The user pastes the file.
- **The exact place.** The team or project, by its exact name. Take it
  from the user's ask or from `wiki/ways-of-working.md`. If neither names
  one, ask. Never guess, and never use another team.

## Steps

1. **Find the place.** Look up the team or project. Find its first
   state for new work: Backlog, Triage, To Do in Jira's default flow, or
   no state for GitHub Issues. If none fits, ask. **Output:** the team and
   the state.
2. **Find the label.** Look for a `copilot` label. Create it only if it's
   missing. It marks your tickets so people can review or bulk-delete
   them. **Output:** "label found" or "label created".
3. **Find duplicates.** List the open issues in that team with the
   `copilot` label. A ticket or epic whose title matches one exactly is a
   duplicate: don't create it, and use the existing ID where other tickets
   point to it. **Output:** the duplicates, or "None".
4. **Create the epics** (plan path only), in build order. Use the
   tracker's epic type if it has one (a Jira Epic), otherwise a parent
   issue (Linear, GitHub). Title: the epic's title. Description: the
   epic's section, from `Outcome:` to the end of the section.
   **Output:** each `E<n> -> <ID> <url>`.
5. **Create the tickets** in file order, so a ticket exists before the
   ones that depend on it. For each:
   - Title: the heading text after `T<n>:` and its space.
   - Description: the ticket's section from the `Type:` line to the end,
     copied from the file, not retyped. Replace each `T<n>` and `E<n>`
     with the ID it was created as.
   - The team, the state from step 1 and the `copilot` label.
   - The epic as parent, when there is one.
   - Each Depends on ticket as a "blocked by" relation, when the tool
     has one. The line stays in the description either way.
   **Output:** each `T<n> -> <ID> <url>`, or `T<n> -> exists: <ID>`.
6. **Record the IDs.** Add a `## Created` section to the end of the
   tickets file (and the epics file) with the lines from steps 4 and 5,
   and the date. **Output:** the count created and skipped.

## Rules

- Never put a ticket in a state past the first one (no To-do, In
  Progress or Done). Moving work forward is the team's call.
- Never pass an existing issue's ID to an update call. If the user wants
  old tickets replaced, create the new ones and list the old ones in the
  report for them to close.
- Never add estimates, assignees, priorities, cycles or sprints the file
  doesn't give. If the plan sets a build order, list it in the report.
- If a call fails, stop, report which tickets were created and which
  weren't, and don't retry with changed content.
- Add `### Created` to the report with the step 6 lines.
