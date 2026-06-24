# Regression tests for the what-for-and-how engine

This directory is the engine's mechanical safety net. It exists because of a finding,
not a hunch: an adversarial stress-test (v3.2 to v3.3) showed that prose guards in the
SKILL file do not enforce themselves. The engine, run by a language model, performs the
de-biasing ritual and reports itself compliant while still breaking the rule. Only CODE
that reads the engine's output and re-derives the verdict catches that. So the rules that
can be checked mechanically are checked here, not trusted.

## What is here

- `regression-cases.json`: the 28 inputs that broke earlier versions, frozen from the
  v3.2 stress-test (workflow run that produced them is named in the file's `origin`).
  Each case carries its attack dimension, the mechanism it targets, and `review_assertions`
  for the human/lens-reviewable parts.
- `fixtures/`: tiny hand-written cascade outputs, one clean and one per hard check, each
  carrying an `_expect_fail` marker. The checker's `--selftest` runs these so CI can prove
  the checker itself works without a live model.
- `../scripts/check_cascade.py`: the checker. Its header documents the cascade-output
  JSON contract and the checks.

## The two-step regression (engine is a model, checker is code)

The checker cannot run the engine for you; the engine is a language model. The loop is:

1. Run the engine over `regression-cases.json`, having it emit the cascade-output JSON
   shape (the Format B fields plus per-floor `grounding`, `l6_survived`, a discrete
   `l6_falsify`, and `no_pack`). Save each output as a `.json` file.
2. Run the checker over those outputs:

   ```
   python3 scripts/check_cascade.py --dir path/to/outputs
   ```

   It exits non-zero if any hard check (C1 to C5) fails. Compare the failure rate to the
   last release: regression means a previously-passing case now cheats again.

## What the checker enforces (hard, exit non-zero)

- **C1** a fired brake (permissibility propriety-limit, or a clinical/propriety terminus)
  emits no scored floors and no selection_audit.
- **C2** a one-winner `resolves_when` cannot wear a `held_conjunctive` or `single` label
  (it is an ASK); a `held_disjunctive` carries a blocked_resolution from the closed list.
- **C3** a floor with `l6_survived: false` is never seated in a held set.
- **C4** no floor is `grounding: high` while `no_pack` is true.
- **C5** a discrete `l6_falsify` field exists and L6 content is not duplicated into floor
  evidence.

Advisory (warn only): **C6** fabricated speaker gender/role, **C7** a bare
`banned_tiebreaker_used: none`, **C8** a coined or fused terminus type.

## CI

`.github/workflows/validate-pack.yml` runs `check_cascade.py --selftest`, which proves the
checker catches each cheat on the fixtures. The full two-step regression against
`regression-cases.json` needs a model and is run by hand before a release.

## The honest limit

This is a release and test tool, not a runtime shield. It checks outputs you have captured;
it does not run inside someone else's chat when they invoke the published skill. Real
runtime enforcement would need a harness wrapping the skill, which is a larger thing than a
markdown file. See the engine's honesty notes and METHODOLOGY.md.
