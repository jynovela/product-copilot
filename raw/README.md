# raw/

Put source documents here: call notes, interview transcripts, PRDs,
analytics exports, competitor pages, meeting notes. Markdown or plain text
works best. Put images in `raw/assets/`.

Name files with the date first, for example `2026-11-03-call-acme.md`.

Rules:

- The agent reads these files but never changes them.
- Files here are ignored by git (see `.gitignore`), so they stay on your
  machine unless you choose to commit them.
- After you add a file, tell the agent: `ingest raw/<file>`.
