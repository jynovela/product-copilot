# Page rules

Read this before you create or change a wiki page.

## Page types

| Folder | `type` | One page per | Example file name |
| ------ | ------ | ------------ | ----------------- |
| `wiki/sources/` | `source` | file in `raw/` about the product | `2026-11-03-call-acme.md` |
| `wiki/customers/` | `customer` | customer segment or persona | `small-agency-owner.md` |
| `wiki/accounts/` | `account` | customer company: plan, status, open issues | `acme-corp.md` |
| `wiki/problems/` | `problem` | customer need, pain or opportunity | `slow-invoice-approval.md` |
| `wiki/features/` | `feature` | feature or product area | `bulk-export.md` |
| `wiki/people/` | `person` | person at the company: role and what they own | `ana-ortiz.md` |
| `wiki/competitors/` | `competitor` | competing product or alternative | `spreadsheets.md` |
| `wiki/decisions/` | `decision` | product decision that was made | `drop-free-tier.md` |
| `wiki/experiments/` | `experiment` | test of an assumption, from interviews to A/B tests | `csv-import-fake-door.md` |
| `wiki/metrics/` | `metric` | metric, defined once | `weekly-active-teams.md` |
| `wiki/goals/` | `goal` | business or product goal for one period | `cut-approval-time-2027-q1.md` |
| `wiki/strategies/` | `strategy` | version of the product strategy | `strategy-2027.md` |
| `wiki/analyses/` | `analysis` | answer to a question worth keeping | `churn-drivers-q4.md` |
| `playbook/sources/` | `source` | file in `raw/playbook/` or `raw/books/` | `2026-01-07-ken-norton-best-pm-books.md` |
| `playbook/books/` | `book` | book | `high-output-management.md` |
| `playbook/topics/` | `topic` | area of PM craft that groups books | `decisions-and-data.md` |
| `playbook/concepts/` | `concept` | framework or idea from the books | `jobs-to-be-done.md` |
| `playbook/essays/` | `essay` | blog post or essay | `invisible-asymptotes.md` |

Every page starts from its template in `templates/<type>.md`.

## Rules for every page

1. **File names** are lowercase words joined by dashes, ending in `.md`. A
   file name must be unique across `wiki/` and `playbook/` together.
2. **Frontmatter.** Every page in a type folder starts with:

   ```text
   ---
   type: <type from the table>
   summary: <one line, same text as in index.md>
   updated: <YYYY-MM-DD, from date +%F>
   ---
   ```

   Source pages also have `raw: raw/<file>` and `raw_sha256: <hash>`.
   Experiment pages also have `status`; goal pages `level`, `commitment`,
   `status` and `period`; strategy pages `status` and `horizon`; decision
   pages `kind`. Their allowed values are in the templates, and the check
   script enforces them. A goal is `ended` when its period is over and no
   source gives its result.
   Book, essay, topic and concept pages also have `knowledge_source:`, either
   `model-memory` (you wrote it from what you already know) or `ingested`
   (it comes from a source in `raw/`).
3. **Links** are `[[file-name]]` without `.md` and without folders. Only
   link to pages that exist. If a page should exist, create it. Links may
   cross layers, e.g. a problem page can link to `[[jobs-to-be-done]]`.
4. **Citations.** Every claim on a customer, account, problem, feature, competitor or
   decision page ends with the source page it came from, like
   `(see [[2026-11-03-call-acme]])`, a page in `wiki/sources/`. Book and
   essay pages cite the page in `playbook/sources/` that put them on a
   list. A source in the other layer never counts. Topic and concept pages link the books or
   essays they draw on.
5. **Your own reasoning** is marked `Inference:`. Knowledge that comes from
   no source is marked `General knowledge:`. Never present either as
   something a source said. A page with `knowledge_source: model-memory`
   must contain `General knowledge:`; the check script enforces it.
6. **Keep the layers apart.** Playbook pages are advice, not evidence.
   Never cite a playbook page as proof of something about the user's
   product or customers.
7. **Contradictions.** When a new source disagrees with a page, keep the old
   claim, add the new one, and add a line under `## Contradictions` on that
   page that names both sources. Don't silently replace old claims.

8. **Own and public evidence.** A source is `own` (from the team or its
   customers) or `public` (from the web). Web content is `public` even when
   a teammate copied or forwarded it, such as a competitor's pricing page
   or release notes. Notes the teammate added to it, such as deals lost,
   are `own`: say so on the source page. Public sources can show what a
   market says, never how many of the user's customers have a problem, so
   problem pages count the two apart.
9. **You record; people decide.** Never set a goal, a target, a price, a
   strategy or a decision. Write what a person or a source decided, and
   name who. You may count what the wiki holds, and do arithmetic on
   sourced numbers, marked `Inference:`. You may prepare options on an
   analysis page. You never guess a number.
   One exception: in a run the user asked to do without stopping, you may
   record your own pick of an opportunity or a scope with `Decided by:
   copilot (unconfirmed)`, and list each one first in the run's report. A
   person confirms it by putting their name in Decided by and adding a
   dated Reviews line. Never use it for a goal, price, strategy, launch or
   outcome review.
10. **Shared lists.** Use these words exactly, wherever the field appears:
    - Target from: `baseline + expected lift`, `funnel sizing [[analysis]]`,
      `past launch or period [[page]]`, `benchmark [[source]] (external)`,
      `set by leadership (<who>)`, `team guess (<who>)`, `direction only`.
    - Basis (for sizes and counts): `measured`, `stated by source`,
      `team guess (<who>)`, `inference`. `unknown` is a valid value.
    - Verdict (experiments and features): `succeeded`, `not successful`,
      `failed`, `inconclusive`.
    - Actions: `ship`, `scale`, `iterate`, `re-scope`, `delay`, `kill`.
    - Guardrails: `must stay within <range>`.
    - Product stage: `pre-fit`, `growth`, `mature`, `decline`.
    - Say "metric" and "target", never "KPI".
11. **Locked sections.** Some sections lock (each template says when).
    Fixing wording or a typo is always allowed; a factual error gets a
    dated correction line, never a silent edit. Beyond that:
    - Records of a run (experiment, a feature's Success metrics and
      Launch): keep the original text, add a dated line under
      Deviations, and judge results against the original thresholds.
    - Commitments (goal, strategy, decision): write a new page that
      replaces the old one, and link both ways.
12. **Current and archived.** Customer, account, problem, feature,
    competitor, metric, person and analysis pages have `state: current | archived` and
    `as_of` (the last day their facts were checked). Archived means no
    longer true or no longer done: add `- Archived: <YYYY-MM-DD>, <why>
    (see [[page]])`, never delete. Skip archived pages unless asked. Never
    mark a page outdated; the check script flags pages past their type's
    freshness window. Facts no person confirmed go to
    `wiki/review-queue.md`, not onto pages.

## Page type rules

- **Source.** Each quote is one line, `- "the words"`, word for word from
  the raw file. Mark a cut inside a quote with `...`. The check script
  compares every quote with the raw file. On other pages, each line under
  `## Evidence` names its source.
- **Experiment.** Results come from an ingested source, never from you.
  The Metrics and decision rule section can't change once status is
  `running`. The Outcome follows the rule, not judgment.
- **Feature.** "Launched" is the first day the target segment can use it
  without an invitation; invite-only betas are rollout steps before it.
  Success metrics, Tier, Audience and Launched lock that day. Scope locks
  earlier, once a `scope` decision approves it. The verdict follows the
  thresholds. The Plan line is the only place plans are named.
  No launch task lists: those live in the team's project tool.
- **Account.** One page per customer company; its segment is a `customer`
  page. Keep `status` in the frontmatter and the Status line the same.
  Open issues are dated snapshots from the ticket tool, never edited to
  look current: add a new line when the status changes.
- **Metric.** Define each metric once, here. Other pages link it and never
  restate the formula.
- **Problem.** Count Evidence strength yourself. Each Magnitude line needs
  a Basis. Urgency is the highest step a source shows people taking; when
  sources disagree, use the lower step and add a Contradictions line.
  Ranges are fine. Never multiply reach and frequency into one score, and
  put no RICE, ICE or market size here.
- **Goal.** Features point at goals; goals don't list features. A business
  goal's Parent is the active strategy; a product goal's is a business
  goal. Flag an output written as an outcome ("launch X"), more than one
  active product goal per team, and more than five business goals. Read a
  verdict by commitment: an aspirational goal near 70% is not a failure.
- **Strategy.** At most one page is `active`. Changing a choice in
  Challenge, Where to play, How to win, Focus areas, Bets or Won't do makes
  a new version and a decision page. No strategy page until a person or
  source gives at least a challenge and where to play; until then the
  overview says "No strategy recorded". Ask for a review when the newest
  Reviews line is over three months old. Frameworks such as SWOT go on
  analysis pages.
- **Decision.** A page is required for: choosing an opportunity, approving
  scope, a launch that is tier 1 or followed an experiment, overriding an
  experiment's rule, iterate/scale/kill reviews, any price or packaging
  change, adopting or changing a strategy, a go-to-market category, motion
  or main channel change, and replacing or missing a committed goal.
  Otherwise only when a person asks or a source records one. Everything
  above Reviews is locked except Status. A decision that replaces another
  fills in "Reopened because". Flag a missing decider, "do nothing" as the
  only option, an irreversible call on thin evidence, and no Revisit when
  or Watch line.
- **Overview.** Target customers and Competitive position describe today,
  from evidence; the strategy page holds the choices. Flag when the two
  drift apart. Pricing and Go-to-market are current pictures; each change
  to them is a decision page.
