# Workflow: record

Use when the user tells you something to keep: a decision, a new or
stopped feature, a changed goal, a status, who owns what. For example:
"I decided we'll build bulk export", "we stopped the mobile app", "Ana now
owns billing".

1. **Save the note.** Run `date +%F`. Save the user's words in a new file
   `raw/notes/<YYYY-MM-DD>-chat-<short-title>.md`, from
   `templates/raw-note.md`: who said it, the date, "in chat", and their
   words as written. Add nothing of your own to the note, not even a
   line of context. Never edit a note after saving it. When the user
   says a saved note or any other raw source is wrong, save the
   correction as a new note that names the wrong file, and add a
   `- Corrected by: [[<new source page>]]` line to the wrong source's
   page in `wiki/sources/`. If the name exists, add `-2`.
   **Output:** the path.
2. **Source page.** Give the note a source page with `Evidence: own`,
   following the Hash and Source page steps of `workflows/ingest.md`.
   **Output:** the source page.
3. List the pages to create, update or archive. Mark each change to a
   locked section or a commitment: it needs a new page (a decision, a goal
   or a strategy version), not an edit. **Output:** three lists, "Create",
   "Update" and "Archive".
4. List the required fields the note doesn't give, such as Decided by,
   Why, or Options not chosen for a decision. Ask for at most three of
   them, in one message: the ones that most change what the page says,
   such as who decided and why. Write `unknown` for the rest and list
   them in the report. If the user said to run without stopping, ask nothing and
   write `unknown` for all of them. Never fill them in yourself.
   **Output:** the answers, or "Running without stopping".
5. Show the lists from steps 3 and 4 and wait for a yes, unless the user
   said to run without stopping. **Output:** the user's answer.
6. Make the changes, following the page rules. Archive a page by setting
   `state: archived` and adding the `- Archived:` line; never delete it.
   Every changed page gets today's date in `updated` and, where the note
   confirms its facts, in `as_of`. Move archived pages to `## Archived`
   in `wiki/index.md`. **Output:** each path changed, one line each.
7. Append `## [YYYY-MM-DD] record | <one-line summary>` to `wiki/log.md`,
   one line per page touched. Run `python3 tools/lint_wiki.py` until
   `RESULT: 0 errors`. **Output:** the entry and the final `RESULT` line.
8. Write the report:

    ```text
    ## Record report: <one-line summary>
    ### Note saved
    ### Pages created
    ### Pages updated
    ### Pages archived
    ### Fields left unknown
    ### Lint result
    ```
