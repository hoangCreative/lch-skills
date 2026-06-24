# Changelog

All notable changes to this skill. Format loosely follows Keep a Changelog. Versions are semantic.

## [2.3.0] - 2026-06-24

Publish-grade hardening. The first application of the `skill-upgrade` process. No engine prose changed: v2.2.1 already reached the prose ceiling. This release is scaffolding and honesty, not new rules.

### Added
- Structured test fixtures (`tests/fixtures/`, good and bad cases mapping to the four surviving leak classes) plus `tests/README.md`, turning the narrative results into a reproducible apparatus.
- `CONTRIBUTING.md` with a contribution rubric that is itself a ground-or-abstain check (sourced gap, grounded claims, included test, self-check), so the standard holds without a human gatekeeper.
- `scripts/validate_skill.py` and a CI workflow enforcing the mechanical rules (no em-dash, frontmatter present, version consistency across SKILL, CITATION, and CHANGELOG, fixture completeness). The validator caught and fixed a real version-detection bug in itself.
- `HARNESS.md`: a named spec for the runtime harness (cite-time byte snapshot, forced-choice abstention cost, number reconciliation) that closes the two failures prose cannot, so the skill names its own ceiling instead of pretending completeness.

## [2.2.1] - 2026-06-23

Last prose fix, driven by a controlled A/B round.

### Tested
- Round 3: a controlled A/B behavioral test. 10 cases, each run by an assistant carrying the skill (treatment) and a plain assistant (control), blind judges. Targeted the four Round-2 gaps plus v2.2 regression.
- Result: treatment 9 HOLDS / 1 PARTIAL / 0 GAMEABLE; control 5 HOLDS / 3 PARTIAL / 2 GAMEABLE. The skill measurably removes the assert-from-memory and trust-the-premise failure modes under pressure; its lift is invisible on easy cases and decisive on attacks.
- v2.2 regression held (offload and citation-must-support both clean). Of the four gaps: poisoned-community and TOCTOU are now handled; fabricated-citation and non-converging-chain are not, and they fail in the two ways the critic predicted: over-abstention and unverifiable verbatim.

### Changed
- Banned over-claiming: assert only what you ran or fetched this turn; reconcile or drop a number that conflicts with a fetched source.
- Banned over-abstaining: when a decision is forced and a grounded answer is in hand, commit with the risk named rather than parking everything in to-verify.

### Noted
- Declared the prose ceiling. The two surviving failure classes (over-abstention as reward-shaping, verbatim integrity as runtime state) are not wording problems. Honest-limits now specifies the runtime harness that closes them (cite-time byte snapshot, forced-choice cost scorer, number-reconciliation). No v2.3 of guards is planned; the next investment is the harness, not more prose.

## [2.2.0] - 2026-06-23

Second hardening release, driven by a behavioral test.

### Tested
- A behavioral round: 16 cases (the 12 read-level cases plus 4 new edge cases), real assistants with the v2.1 skill running real tools, two adversarial judges per transcript who re-fetched cited URLs.
- Result on v2.1: 12 HOLDS, 3 PARTIAL, 1 GAMEABLE. Regression on the 12 inherited cases moved from 1/6/5 (read-level v2.0) to 8/3/1 (behavioral v2.1). Real execution beat the read-level prediction, but exposed leaks the text-only round could not.

### Changed
- A cited source must actually STATE the claim; an adjacent source (symptom not cause, failure not fix) does not settle it. Closes the "memory fact wearing a real but non-supporting citation" leak (seen in 3 cases).
- A clarifying question or a promise to verify later does not satisfy the no-offload rule when the tools are in hand. Closes the one downward regression (case 10).
- A substantive memory fact may not be parked under TO-VERIFY as a hedge when a tool to check it is available.
- A security-changing community fix is never settled by consensus, however upvoted.

### Noted
- Honest-limits now records the behavioral result and names four classes prose still cannot close (fabricated-unfetched citation, poisoned community consensus, verify/act state drift, non-converging source chain), left for a future round and a harness.

## [2.1.0] - 2026-06-23

Hardening release, driven by an adversarial test.

### Tested
- Designed a 12-case adversarial stress test (the same method used for the sibling skill `what-for-and-how`). Four adversarial agents read the actual skill text and, per case, found the cheapest way to look compliant while skipping the work.
- Result on v2.0: 1 of 12 held cleanly, 6 partial, 5 gameable. Confirms, again, that a prose skill cannot fully enforce itself against a model that games it.

### Changed (turned narration into checkable output requirements)
- A specific number, version, or fact may not appear in the answer, even hedged under "to verify", unless a source was consulted this turn.
- Every SETTLED claim must carry its source inline (what, where, when or which version), or it auto-downgrades to TO-VERIFY.
- Added an explicit empty-community branch: silence is data, not permission to backfill from memory or to read it as "no problem".
- Reasoning may operate only on settled or explicitly assumed facts; a user-supplied "given" premise is still a claim subject to the chain.
- Each self-check pass must reach a new external source; re-reading the same artifact is not a pass.
- A sub-agent's report is a claim, not a source: re-derive the state. Positively locate before deleting (a no-result grep is a failure to locate, not proof of non-use). An urgent command is not the explicit confirmation an irreversible removal requires.
- Official sources are now used to TEST the community claim, including for evidence it is wrong, not only to confirm.

### Noted
- Honest-limits section now records the test result and states that the ceiling (full enforcement) needs a harness, not more prose.

## [2.0.0] - 2026-06-23

First public release, for a global audience, under the name `ground-or-abstain`.

### Added
- Rewrote the discipline in English as a portable, host-agnostic skill.
- Three load-bearing clarifications made explicit: community-first is for freshness not correctness; the ban is on the model's information not its intelligence; the output shows its seams (settled / assumed / to-verify).
- Adopted intelligence-tradecraft's three-way split (settled / assumed / to-verify), SIFT's "Stop" reflex, and Chain-of-Verification's independence in the self-check loop.
- A METHODOLOGY.md anchoring every part of the discipline in its prior art (lateral reading, the Admiralty code, ICD 203/206, SIFT, CRAAP, Sagan, CoVe, ReAct, RAG, knowledge-cutoff awareness) and stating the gap it fills.
- An honest-limits section: the two signature moves are reasoned, not yet tested.

## [1.0.0] - internal

The origin draft, in Vietnamese, as the discipline "xac tin": community-first verification, ban on the model's training memory as a source, the split of settled versus to-verify, and the 2-to-5 self-check loop. Lived as doctrine and inside a personal partner skill before being packaged standalone.
