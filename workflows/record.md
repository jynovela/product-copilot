# Workflow: record

Use when the user tells you something to keep: a decision, a new or
stopped feature, a changed goal, a status, who owns what. For example:
"I decided we'll build bulk export", "we stopped the mobile app", "Ana now
owns billing".

1. Run `date +%F`. Save the user's words in a new file
   `raw/notes/<YYYY-MM-DD>-chat-<short-title>.md`, from
   `templates/raw-note.md`: who said it, the date, "in chat", and their
   words as written. Never edit a note after saving it; a correction is a
   new note. If the name exists, add `-2`. **Output:** the path.
2. Ingest the note (the ingest workflow, steps 3 to 4) so it has a source
   page with `Evidence: own`. **Output:** the source page.
3. List the pages to create, update or archive. Mark each change to a
   locked section or a commitment: it needs a new page (a decision, a goal
   or a strategy version), not an edit. **Output:** three lists, "Create",
   "Update" and "Archive".
4. List the required fields the note doesn't give, such as Decided by,
   Why, or Options not chosen for a decision. Ask for them in one message,
   unless the user said to run without stopping; then write `unknown` and
   list them in the report. Never fill them in yourself. **Output:** the
   answers, or "Running without stopping".
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
