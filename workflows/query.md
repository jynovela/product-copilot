# Workflow: query

Use when the user asks a question about the product, customers or market.

1. Read `wiki/index.md` and pick the pages that may hold the answer. If the
   question is about how to do product work (a method, a decision, a
   negotiation), read only the Guides and Topics sections at the top of
   `playbook/playbook-index.md`, open the matching topic page, and follow
   its links to books and concepts. For a named framework or book, search
   the index with `grep -i "<term>" playbook/playbook-index.md` instead of
   reading it whole. **Output:** the list of pages.
2. Read those pages, and the source pages they cite when a detail matters.
   A question changes nothing: answer from the pages as they stand. If a
   problem page's `As of` is older than the newest own source in
   `wiki/source-index.md`, say so in the answer and offer
   `skills/synthesize-problems`. **Output:** none; go to step 3.
3. Answer. Cite a page for every claim, like `[[slow-invoice-approval]]`.
   Put evidence under `Your evidence:` and playbook advice under
   `The playbook suggests:`. Mark anything neither covers as
   `Not in the wiki:` and say which source would answer it.
   **Output:** the answer.
4. Ask whether to file the answer. If the user says yes, create
   `wiki/analyses/<file-name>.md` from `templates/analysis.md`, link to it
   from at least one related page, add it to `wiki/index.md`, append
   `## [YYYY-MM-DD] query | <question>` to `wiki/log.md`, and run the check.
   **Output:** the new path and the final `RESULT` line, or "Not filed".
