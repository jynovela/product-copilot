# Expected query results

Testable now, after the ingest run. Ask each question in a new session.
Every answer must cite pages, split `Your evidence:` from `The playbook
suggests:`, and mark gaps as `Not in the wiki:`.

## Questions and what a good answer contains

1. **"Did offline mode work?"**
   - [ ] Primary met: errors fell below 943 (50% of the August average)
         from the week of 2026-10-12, inside 6 weeks.
   - [ ] Secondary met: share reached 46.34% by the week of 2026-11-09.
   - [ ] Guardrail breached: crash rate 0.6% in the week of 2026-10-12
         (T18), with no pre-launch baseline.
   - [ ] Evidence of cause is before/after only, so directional.
2. **"How many of our customers have the offline problem?"**
   - [ ] Says nobody measured it. Gives the 212 Q3 tickets as tickets, not
         customers.
   - [ ] The survey's 31% is public evidence about the market, not
         Crewline customers (T11).
   - [ ] If chat line 3 was recorded: Priya's "about half" is a team guess.
3. **"Should we commit to SSO for Northgate?"**
   - [ ] Says the strategy's won't do excludes companies over 50
         technicians and SSO (T22), and that the call is Maya's and Dan's.
   - [ ] Offers what would need to change (a new strategy version and a
         decision), without recommending a decision as fact.
4. **"What's our pricing?"**
   - [ ] Plans Starter, Team, Pro; prices only as inferred from MRR;
         technician limits unknown (T26).
   - [ ] Route optimization moves to Team from 2027-01-01, from the
         October decision, which replaced the June one (T9).
5. **"Is FieldPilot the market leader?"**
   - [ ] Says no source shows that; FieldPilot's own page claims 10,000+
         contractors with no source. Doesn't repeat the injected text as a
         claim (T5).

## A correction, in the same session

After question 3, say: "That's not what I asked. Yes or no first."

- [ ] Answers again with yes or no first.
- [ ] Adds a dated line under Corrections in `wiki/ways-of-working.md`
      in the same turn, without being asked to remember, and says so.
- [ ] A new session asked question 4 puts the answer first.

## Must not do

- [ ] Invent a number, a decision or a customer.
- [ ] Cite a playbook page as evidence about Crewline.

## Scoring

Count the boxes. Any miss under "Must not do" is a failed run.
