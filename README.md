# product-copilot

A product-manager copilot built on Andrej Karpathy's LLM Wiki pattern.
You collect sources. An AI agent turns them into a linked wiki about your
product: customers, problems, features, competitors and decisions. The wiki
gets richer with every source you add and every question you ask, so the
agent doesn't start from scratch each time.

It also ships a PM playbook: 145 product management books and 10 essays
from nine reading lists (including Ken Norton's and Ry Sullivan's),
classified into 16 topics and 105 core concepts such as jobs to be done,
the opportunity solution tree, the kernel of good strategy and OKRs. The
agent uses it to suggest how to approach a problem, kept separate from the
evidence about your product. The book pages are written from the model's
general knowledge, not from the books themselves, and say so on every page.
Books the model can't summarize reliably are short stubs marked as
unverified. `playbook/reading-paths.md` suggests what to read for a given
question, `playbook/newsletters-and-podcasts.md` lists ongoing reading,
`playbook/topics/product-frameworks.md` says which framework fits which job,
and `playbook/topics/types-of-product-managers.md` maps the kinds of PM
roles.

Works with any agent that reads `AGENTS.md` (Claude Code, Codex, OpenCode,
Hermes and others) and any model you choose.

## How it works

| Layer | Path | Owner |
| ----- | ---- | ----- |
| Raw sources | `raw/` | You. The agent never edits them; its research skills may add public pages to `raw/public/`, it saves what you tell it in chat to `raw/notes/`, and sync saves tool snapshots to `raw/sync/`. |
| Wiki | `wiki/` | The agent. You read it. |
| Playbook | `playbook/` | The agent. General PM knowledge, not evidence. |
| Documents | `documents/` | The agent, when you ask for one: PRDs, reports, updates and demo specs to share. Not evidence. |
| Schema | `AGENTS.md` (short, read every session), `rules/` and `workflows/` (read only when a task needs them) | You and the agent, together, over time |

## Use it

1. Use this repo as a template, or clone it, and start your agent in the
   repo folder.
2. Drop a source into `raw/`, for example `raw/2026-11-03-call-acme.md`.
3. Tell the agent: `ingest raw/2026-11-03-call-acme.md`.
4. Ask questions: `what are the top problems for small agencies?` Ask the
   agent to file good answers back into the wiki.
5. Ask how-to questions too: `how should I say no to this sales request?`
   The answer separates your evidence from what the playbook suggests.
6. Tell it what changed, in plain words: `I decided we'll build bulk
   export` or `we stopped the mobile app`. It saves your words as a note,
   then updates, creates or archives the pages they affect.
7. Add a book or essay: `add the book <title>`.
8. Fill in `wiki/ways-of-working.md` (how you decide and how to write for
   you) and `wiki/now.md` (this month's focus). The agent reads both first.
9. Ask for a document (`write a weekly update`) or paste a draft and say
   `humanize this`. The humanize check flags chatbot habits with a script
   and fixes them, and it learns your voice from your corrections.
10. Now and then, tell the agent: `lint the wiki`.
11. New fork? Say `set up the copilot for my company`. It ingests what's in
    `raw/`, asks a few short rounds of questions, and writes the answers
    into the wiki, leaving `AGENTS.md` generic so you can pull updates.
12. Say `sync accounts from the CRM` (or tickets from Jira) to save a dated
    snapshot to `raw/sync/` and move status lines forward. With no
    connector, hand it an export file.
13. Ask `what do I need to do today?` for a brief: what the wiki says is
    due, plus meetings, replies and tasks when email, calendar or a task
    app is connected. Briefs go to `daily/`, which git ignores.

Check the wiki yourself at any time:

```sh
python3 tools/lint_wiki.py
```

It needs Python 3.9 or newer and nothing else. It reports broken links,
orphan pages, pages missing from the index, missing frontmatter, pages
that cite no source, bad values in page frontmatter (goal level,
strategy status, decision kind and others), more than one active strategy,
a replacing decision with no reason, pages whose facts are past their
type's freshness window, archived pages with no reason, a past month in
`wiki/now.md`, changes waiting too long in `wiki/review-queue.md`, decisions the copilot made that
no person has confirmed yet, documents with a bad name or header or links
to pages that are gone, `AGENTS.md` growing past its size budget, playbook pages written from memory without a
`General knowledge:` label, bad log entries, raw files that changed after
ingest, and raw files not ingested yet.

## Privacy

`raw/` is ignored by git, because sources like customer calls are often
confidential. Public sources you want to keep, like a published reading
list, go in `raw/public/`, which is committed. The wiki is committed, so review it before you push it
anywhere public. To commit raw sources too, remove the `raw/` lines from
`.gitignore`. Chat notes in `raw/notes/` stay ignored the same way.
`daily/` and `tasks.md` are ignored too, because daily briefs and tasks
can hold email content.

## Reading the wiki

Open the repo folder as a vault in [Obsidian](https://obsidian.md). Links
use `[[page]]`, so the graph view shows how pages connect. GitHub shows
these links as plain text.
