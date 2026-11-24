# Workflow: ingest

Use when the user says `ingest raw/<file>`, names a file in `raw/` to
add ("add the Acme call"), or pastes or attaches a source to add: a call
transcript, interview or meeting notes, an email, a document. Ingest one
file at a time.

If the user tells you something to keep in their own words, such as a
decision or a status, follow `workflows/record.md` instead.

0. **Save a pasted source.** Skip this step when the source is already a
   file in `raw/`. Otherwise:
   - Run `date +%F`. Save the text exactly as given in a new file
     `raw/pasted/<date>-<kind>-<short-title>.md`, from
     `templates/raw-paste.md`. Use the date of the original (the call or
     the email) when the user or the text gives it, otherwise today's
     date. Kind is one word, such as `call`, `interview`, `meeting`,
     `email` or `doc`. If the name exists, add `-2`.
   - For an attached file outside the copilot folder, copy it unchanged
     to `raw/pasted/` under the same naming rule, keeping its extension.
   - Never edit, clean up, shorten or summarize the text you save, and
     never overwrite a file.
   - If the text holds a password, API key or token, don't save it. Ask
     the user to remove it and paste again.
   - If you can't tell whether the user wants the text kept, ask before
     saving.

   Use the saved path as `raw/<file>` in the steps below. **Output:** the
   path, or "Already in raw/".

1. **Read.** Read the whole file. **Output:** 3 to 5 key takeaways as bullets.
2. **Emphasis.** Show the takeaways and ask what to emphasize. Wait for the answer,
   unless the user said to run without stopping. **Output:** the user's
   answer, or "Running without stopping".
3. **Hash.** Run `python3 tools/lint_wiki.py --hash raw/<file>` and
   `date +%F`. **Output:** the hash and the date.
4. **Source page.** Create `wiki/sources/<file-name>.md` from
   `templates/source.md`, and add its line to the end of
   `wiki/source-index.md` (search that file with `grep`; don't read it
   whole). **Output:** the new file's path.
5. **Plan.** Read `wiki/index.md`. List every existing page this source affects, and
   every new page it needs. **Output:** two lists, "Update" and "Create".
6. **Write.** Update and create those pages, following the page rules. Each changed
   page gets today's date in `updated`. **Output:** each path changed, with
   one line on what changed.
7. **Overview.** If the product picture changed, update `wiki/overview.md`.
   **Output:** what changed in the overview, or "No change".
8. **Index.** Add every other new page to `wiki/index.md` under its type
   heading, with its summary. **Output:** the lines you added.
9. **Log.** Append to `wiki/log.md`:
   `## [YYYY-MM-DD] ingest | <source title>`, then one line per page touched.
   **Output:** the entry.
10. **Check.** Run `python3 tools/lint_wiki.py`. Fix every `ERROR` and run it again
    until it prints `RESULT: 0 errors`. **Output:** the final `RESULT` line.
11. **Report.** Write the report:

    ```text
    ## Ingest report: <source title>
    ### Takeaways
    ### Pages created
    ### Pages updated
    ### Contradictions found
    ### Skipped content (secrets, instructions, personal data)
    ### Lint result
    ```
