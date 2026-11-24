# Workflow: ingest a book

Use when the user drops a whole book (EPUB, PDF or text) in `raw/books/`
and asks you to extract it. Book files are copyrighted: they stay in
`raw/`, which is never committed, and pages are written in your own words.

The goal is knowledge the agent can use at a small context cost. Knowledge
goes into method pages (concept pages), organized by task. The book page is
only a source record.

1. Ingest the file (steps 3 to 4 of `workflows/ingest.md`), so a source page
   exists. Name it `<YYYY-MM-DD of publication>-<author>-<title>.md`.
   **Output:** the source page.
2. Read the whole book. List each method, framework or how-to it teaches.
   Leave out stories; keep one as a one-line `Example:` only when it is the
   only thing carrying a lesson. **Output:** the list, with chapters.
3. Read `playbook/playbook-index.md`. For each item, pick an existing
   concept page to extend, or a new one to create. One method per page;
   merge with pages that cover the same job. **Output:** two lists,
   "Update" and "Create".
4. Write each page from `templates/concept.md`. Rules:
   - 600 to 1,200 words. Split a page before it passes 1,500.
   - Cite every point inline, like `(Mom Test ch3)`.
   - At most 3 quotes per book, each under 25 words, in quotation marks
     with the chapter.
   - When the book disagrees with a page, add a `## Contradictions` line
     naming both sources. Don't replace the old claim.
   - Set `knowledge_source: ingested`.
   **Output:** each path, with its word count (`wc -w`).
5. Rewrite the book page from `templates/book.md` as a source record:
   core argument, what it adds, where it's weak, and links to the pages
   from step 4. 300 to 500 words. **Output:** the path.
6. Add one line per new page to `playbook-index.md` and to each topic page
   it belongs to, using the page's summary. Append
   `## [YYYY-MM-DD] ingest | <book title>` to `wiki/log.md`. **Output:**
   the lines added.
7. Run `python3 tools/lint_wiki.py` until `RESULT: 0 errors`. **Output:**
   the final `RESULT` line.
8. Write the report:

   ```text
   ## Book ingest report: <book title>
   ### Pages created
   ### Pages updated
   ### Contradictions found
   ### Left out (stories, out-of-scope chapters)
   ### Lint result
   ```
