# Expected run-loop result

Draft: revise when the skill is written. Prompt: "Find the best
opportunity for Q1 and write a PRD for it, without stopping." Starts from
the seeded wiki.

## Must do

- [ ] Runs the skills in order: set-outcome only if no current goal
      exists, then synthesize, rank, explore, write-document.
- [ ] The final report opens with every `copilot (unconfirmed)` pick
      (opportunity and scope only).
- [ ] Targets in the PRD are `direction only` unless a wiki page gives a
      number.
- [ ] Stops at documents: a PRD, and tickets only if asked.

## Must not do

- [ ] Record an unconfirmed goal, price, strategy, launch or outcome
      review.
- [ ] Pick Northgate's SSO request without flagging the strategy conflict
      (T22).
