# Workflow: lint

Use when the user asks to check or clean up the wiki.

1. Run `python3 tools/lint_wiki.py`. **Output:** every line it printed.
2. Fix each `ERROR`. Don't delete pages to fix one; ask first. Run the check
   again until `RESULT: 0 errors`. **Output:** each fix, one line each.
3. Read `wiki/overview.md` and the pages in both index files. Look for:
   claims that contradict each other, claims a newer source replaced, names
   mentioned on two or more pages that have no page, and missing links
   between related pages. **Output:** each finding with the pages involved.
4. Suggest up to 5 questions to investigate and up to 5 sources to look
   for. If the newest `audit` entry in `wiki/log.md` is over a month old,
   or there is none, suggest `workflows/audit.md`. **Output:** the two
   lists, and the audit suggestion or `Audited on <date>`.
5. Append `## [YYYY-MM-DD] lint | <one-line summary>` to `wiki/log.md`.
   **Output:** the entry.
6. Write the report:

    ```text
    ## Lint report: <date>
    ### Check script result
    ### Fixes made
    ### Contradictions and stale claims
    ### Missing pages and links
    ### Not ingested yet
    ### Suggested questions
    ### Suggested sources
    ```
