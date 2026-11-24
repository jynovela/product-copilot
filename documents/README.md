# Documents

Documents the copilot writes for people to read or share outside the
repo: PRDs, weekly updates, demo specs, interview guides and summaries,
tickets, and others. Wiki pages are the copilot's records; documents are
what it hands to people.

## Rules

- One file per document, named `<YYYY-MM-DD>-<doc type>-<short-title>.md`,
  for example `2026-11-24-prd-bulk-export.md`. The date is the day it was
  written. A new version is a new file with a new date; old versions stay.
- Follow `skills/write-document/SKILL.md`. It starts from
  `templates/document.md` and has one file per document type.
- Write the body for people: plain prose, no `[[links]]`. Put the wiki
  pages the document was built from under `## Built from`, with the
  `updated` date each page had. A reader can then see how old the facts
  are, and the check script flags a link whose page no longer exists.
- Documents are not evidence. Never cite one on a wiki page. To use a
  document as evidence, the user saves it in `raw/` and ingests it.
- Run `skills/humanize-check` on every document before you hand it over.
- Set `status: final` only when the user says the document is done.

Git tracks this folder. If your documents are confidential and you push
this repo somewhere public, add `documents/*` and `!documents/README.md`
to `.gitignore`.
