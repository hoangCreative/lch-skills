# The runtime harness (where prose stops)

This document is the part of ground-or-abstain that is honest about its own ceiling.

Three rounds of adversarial testing (see `tests/results.md`) showed that prose raises the floor a great deal and then stops. Two failure classes survived every wording fix, because they are not wording problems:

- **Over-abstention** is a reward-shaping gap. The skill is rewarded only for "ground or abstain", so hiding a grounded answer in TO VERIFY is always safe and never penalized. A sentence cannot fix an incentive.
- **Verbatim integrity** is a runtime-state gap. The skill trusts a self-reported "verbatim" label, and a process log can be reconstructed to fake it.

Closing these needs a checking mechanism at runtime, not a v-next of the prose. This is the spec for that mechanism. It is not built; it is named so the skill does not pretend to be complete.

## Point 1: Cite-time byte snapshot
Capture what each tool returns at the moment it returns it. Every SETTLED quote must string-match a snapshot captured at or after the moment of its claim. A quote that matches no snapshot is not settled, regardless of any "verbatim" label. This closes `tests/fixtures/bad-4-verbatim-integrity.json`.

## Point 2: Forced-choice abstention cost
When a committed call is mandated and grounded evidence is sufficient, parking the answer in TO VERIFY incurs a penalty. Make over-abstention cost something so it stops being the free safe move. This closes `tests/fixtures/bad-3-over-abstention.json`.

## Point 3: Number reconciliation
Flag any final number that differs from a this-turn fetched source for the same entity. If the answer says 200k and a page fetched this turn for the same thing says 30k, the discrepancy is surfaced, not silently propagated.

## Status
Specced, not built. Building it is system work beyond a markdown file (note 141 territory in the author's vault). Until it exists, the two ceiling fixtures are documented failures, not closed ones. A skill that names its ceiling and points at the fix is worth more than one that claims none.
