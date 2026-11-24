# raw/

Put source documents here: call notes, interview transcripts, PRDs,
analytics exports, competitor pages, meeting notes. Markdown or plain text
works best. Put images in `raw/assets/`.

Name files with the date first, for example `2026-11-03-call-acme.md`.

Rules:

- The agent reads these files but never changes them.
- The agent's research skills may add new public pages to `raw/public/`,
  as paraphrased extracts with their URL and fetch date. They never edit
  or overwrite a file.
- Files here are ignored by git (see `.gitignore`), so they stay on your
  machine unless you choose to commit them.
- You can also paste a call, notes or an email into the chat and ask the
  agent to add it. It saves the text unchanged in `raw/pasted/` first,
  then reads it.
- After you add a file, tell the agent what it is, for example "add the
  Acme call", or `ingest raw/<file>`.
