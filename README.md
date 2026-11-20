# product-copilot

A product-manager copilot built on Andrej Karpathy's LLM Wiki pattern.
You collect sources. An AI agent turns them into a linked wiki about your
product: customers, problems, features, competitors and decisions. The wiki
gets richer with every source you add and every question you ask, so the
agent doesn't start from scratch each time.

It also ships a PM playbook: 67 product management books and 6 essays from
two reading lists (Ken Norton's 2026 list and Ry Sullivan's 2025 list),
classified into 12 topics and 42 core concepts such as jobs to be done,
the opportunity solution tree, choice architecture and OKRs. The agent
uses it to suggest how to approach a problem, kept separate from the
evidence about your product. The book pages are written from the model's
general knowledge, not from the books themselves, and say so on every page.

Works with any agent that reads `AGENTS.md` (Claude Code, Codex, OpenCode,
Hermes and others) and any model you choose.

## How it works

| Layer | Path | Owner |
| ----- | ---- | ----- |
| Raw sources | `raw/` | You. The agent never edits them. |
| Wiki | `wiki/` | The agent. You read it. |
| Playbook | `playbook/` | The agent. General PM knowledge, not evidence. |
| Schema | `AGENTS.md` | You and the agent, together, over time |

## Use it

1. Use this repo as a template, or clone it, and start your agent in the
   repo folder.
2. Drop a source into `raw/`, for example `raw/2026-11-03-call-acme.md`.
3. Tell the agent: `ingest raw/2026-11-03-call-acme.md`.
4. Ask questions: `what are the top problems for small agencies?` Ask the
   agent to file good answers back into the wiki.
5. Ask how-to questions too: `how should I say no to this sales request?`
   The answer separates your evidence from what the playbook suggests.
6. Add a book or essay: `add the book <title>`.
7. Now and then, tell the agent: `lint the wiki`.

Check the wiki yourself at any time:

```sh
python3 tools/lint_wiki.py
```

It needs Python 3.9 or newer and nothing else. It reports broken links,
orphan pages, pages missing from the index, missing frontmatter, pages
that cite no source, playbook pages written from memory without a
`General knowledge:` label, bad log entries, raw files that changed after
ingest, and raw files not ingested yet.

## Privacy

`raw/` is ignored by git, because sources like customer calls are often
confidential. Public sources you want to keep, like a published reading
list, go in `raw/public/`, which is committed. The wiki is committed, so review it before you push it
anywhere public. To commit raw sources too, remove the `raw/` lines from
`.gitignore`.

## Reading the wiki

Open the repo folder as a vault in [Obsidian](https://obsidian.md). Links
use `[[page]]`, so the graph view shows how pages connect. GitHub shows
these links as plain text.
