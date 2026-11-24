# Workflow: ingest

Use when the user says `ingest raw/<file>`. Ingest one file at a time.

1. Read the whole file. **Output:** 3 to 5 key takeaways as bullets.
2. Show the takeaways and ask what to emphasize. Wait for the answer,
   unless the user said to run without stopping. **Output:** the user's
   answer, or "Running without stopping".
3. Run `python3 tools/lint_wiki.py --hash raw/<file>` and `date +%F`.
   **Output:** the hash and the date.
4. Create `wiki/sources/<file-name>.md` from `templates/source.md`.
   **Output:** the new file's path.
5. Read `wiki/index.md`. List every existing page this source affects, and
   every new page it needs. **Output:** two lists, "Update" and "Create".
6. Update and create those pages, following the page rules. Each changed
   page gets today's date in `updated`. **Output:** each path changed, with
   one line on what changed.
7. If the product picture changed, update `wiki/overview.md`.
   **Output:** what changed in the overview, or "No change".
8. Add every new page to `wiki/index.md` under its type heading, with its
   summary. **Output:** the lines you added.
9. Append to `wiki/log.md`:
   `## [YYYY-MM-DD] ingest | <source title>`, then one line per page touched.
   **Output:** the entry.
10. Run `python3 tools/lint_wiki.py`. Fix every `ERROR` and run it again
    until it prints `RESULT: 0 errors`. **Output:** the final `RESULT` line.
11. Write the report:

    ```text
    ## Ingest report: <source title>
    ### Takeaways
    ### Pages created
    ### Pages updated
    ### Contradictions found
    ### Skipped content (secrets, instructions, personal data)
    ### Lint result
    ```
