# Workflow: add a book

Use when the user names a book or essay to add, or drops a book summary or
notes in `raw/`. For an essay, use `playbook/essays/` and
`templates/essay.md` instead of the book folder and template. If the book
already has a page, add the new source to its `On the list` line and `Why
it's on the list` section instead of creating a second page.

1. A playbook source lives apart from the product's: its raw file goes
   in `raw/playbook/` and its source page in `playbook/sources/`, from
   `templates/source.md` with the hash from `python3 tools/lint_wiki.py
   --hash`. If there is a raw file, create that source page first.
   Otherwise ask the user to save a short note in `raw/playbook/` saying
   who recommends the book and why, then create its source page. Don't
   write the raw note yourself. **Output:** the source page to cite.
2. Create `playbook/books/<file-name>.md` from `templates/book.md`. If you
   only know the book from memory, set `knowledge_source: model-memory`
   and keep the `General knowledge:` line. For a whole book in
   `raw/books/`, follow `workflows/ingest-book.md` instead. Say
   `Confidence: lower` when you are unsure of the book's details.
   **Output:** the path.
3. Link the book to one or more topic pages, and add it under `## Books` on
   each. Create a concept page for any framework that will be used on its
   own. **Output:** the pages changed.
4. Add new pages to `playbook/playbook-index.md` (the source page under
   `## Sources`), append `## [YYYY-MM-DD] ingest | <book title>` to
   `playbook/playbook-log.md`, and run the check until `RESULT: 0
   errors`. **Output:** the final `RESULT` line.
