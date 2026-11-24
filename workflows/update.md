# Workflow: update the copilot

Use when the user asks to update the copilot or get its latest version.

A copy owns `wiki/`, `raw/` (except `raw/playbook/`), `documents/`,
`daily/`, `tasks.md`, `.gitignore` and `.copilot-version`. Everything else
is generic and comes from the upstream copilot repository. An update
replaces the generic files and never touches the copy's own.

Don't `git merge` upstream. A copy made with Use this template shares no
history with it, so every file that differs conflicts.

This needs Git. Without it, tell the user to download the new ZIP and copy
the generic paths below over their folder, then run the check.

Generic paths:

```text
AGENTS.md CLAUDE.md README.md .markdownlint-cli2.yaml .claude rules
workflows templates skills tools playbook raw/playbook raw/README.md
documents/README.md examples
```

1. **Check the state.** Run `git status --short`; if it lists anything,
   commit it first or ask. Read `.copilot-version` for the upstream URL
   and the upstream commit this copy last took. **Output:** the URL and
   the commit, or "none".
2. **Fetch.** If `git remote` has no `upstream`, run `git remote add
   upstream <URL>`. Run `git fetch upstream main` and `git rev-parse
   upstream/main`. If that commit is the recorded one, say the copy is up
   to date and stop. **Output:** the new commit.
3. **Show what will change.** Run `git diff --stat HEAD upstream/main --
   <generic paths>`. If a commit is recorded, also run `git diff
   --name-only <recorded commit> HEAD -- <generic paths>`: these are
   generic files this copy changed itself, and the update would overwrite
   them. List them and ask what to keep, unless the user said to run
   without stopping; then take upstream's and list them in the report.
   **Output:** the number of files that change, and the copy's own edits
   with the user's answer for each, or "None".
4. **Replace the generic files.** Run `git checkout upstream/main --
   <generic paths>`. For each file the user chose to keep, run `git
   checkout HEAD -- <file>`. **Output:** "Replaced", and the files kept.
5. **Remove what upstream removed.** If a commit is recorded, run `git
   diff --name-only --diff-filter=D <recorded commit> upstream/main --
   <generic paths>` and `git rm` each listed file that still exists. With
   no recorded commit, skip this and say so. **Output:** the files
   removed, or "Skipped: first update".
6. **Check.** Run `python3 tools/lint_wiki.py`. A playbook page this copy
   added is now missing from `playbook/playbook-index.md` and its topic
   page: add its lines back. A wiki page may fail a rule that changed:
   fix it by `rules/pages.md`, and ask when the fix isn't mechanical. Run
   the check until `RESULT: 0 errors`. **Output:** each fix and the final
   `RESULT` line.
7. **Record and commit.** Write the new commit to `.copilot-version`,
   keeping its `upstream:` line. Commit everything as `Update copilot to
   <first 7 characters of the commit>`. **Output:** the commit message.
8. **Report:**

   ```text
   ## Update report: <old commit> to <new commit>
   ### Files replaced
   ### Files removed
   ### Own edits to generic files (kept or overwritten)
   ### Fixes after the update
   ### Lint result
   ```

## Never

- Change anything in `wiki/`, `documents/` or the copy's own `raw/` files
  during an update, except a fix the check asks for in step 6.
- Merge or rebase onto upstream.
- Push the copy to the upstream repository.
