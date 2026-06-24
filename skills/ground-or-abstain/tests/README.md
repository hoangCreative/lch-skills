# Tests for ground-or-abstain

Three layers, from cheapest to most honest.

## Files
- `fixtures/` : structured cases as data. `good-*` describe correct behavior; `bad-*` describe a cheap compliant-looking failure with its `leak_class`, the round it was found in, and a `pass_if` / `fail_if` for a judge.
- `cases.json` : the original 12 read-level cases, frozen as a regression bank. A verdict that regresses on an unchanged case here is a real regression.
- `results.md` : the full write-up of all three test rounds (read-level, behavioral, controlled blind A/B), including where the skill lost.

## How to re-run (behavioral)
1. Give an agent the current `SKILL.md` plus one fixture's `scenario`.
2. Have it actually handle the case with real web/shell tools.
3. Have a second, adversarial agent judge the transcript against the fixture's `pass_if` / `fail_if`, re-fetching any cited URL to confirm it exists and states what was claimed.
4. Take the strictest verdict.

## How to re-run (read-level, cheap)
Give an agent the `SKILL.md` text plus a `bad-*` fixture and ask for the cheapest compliant-looking way to fail. If it finds one the skill does not already block, that is a new leak.

## The four bad fixtures map to the four surviving leak classes
- `bad-1-memory-assertion` : the root failure the whole skill exists to stop.
- `bad-2-citation-nonsupporting` : a real source that does not state the claim (closed in v2.2).
- `bad-3-over-abstention` : hiding a grounded answer in to-verify (closed in prose in v2.2.1, but it is a reward-shaping gap).
- `bad-4-verbatim-integrity` : trusting a self-reported verbatim label (a runtime ceiling; see `../HARNESS.md`).

The last two are the prose ceiling. Fixtures document them honestly rather than pretending a sentence closed them.
