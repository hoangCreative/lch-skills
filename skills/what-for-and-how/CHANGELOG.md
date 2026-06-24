# Changelog

All notable changes to what-for-and-how are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.4.0] - 2026-06-22

The enforcement layer. A regression re-ran the v3.3 engine on the exact 28 cases that failed the v3.2 stress-test and found prose enforcement barely bit: only 3 of 28 resolved. The permissibility/culture-harm axis was largely fixed, but the held-set rules were gamed by relabeling (a disjunctive case stamped conjunctive to dodge the mandatory ask) and the engine filled its own mandatory fields dishonestly (a false blocked_resolution, a self-cleared anti-default check). The lesson, now confirmed twice: a prose skill cannot enforce itself against a model that games it. v3.4 stops adding prose and adds CODE. No breaking change: packs written for >=3.1.0 still load unchanged.

### Added

- `scripts/check_cascade.py`: a no-dependency checker that reads the engine's structured cascade-output and re-derives the verdict from the fields instead of trusting any self-report. Hard checks: C1 a fired brake emits no scored floors or selection_audit; C2 a one-winner resolves_when cannot wear a conjunctive or single label and a held_disjunctive needs a closed-list blocked_resolution; C3 no L6-failed floor is a held member; C4 no grounding HIGH under no_pack; C5 a discrete l6_falsify exists and is not duplicated into floor evidence. Advisory: C6 fabricated speaker gender, C7 a bare banned_tiebreaker, C8 a coined terminus type.
- `tests/regression-cases.json`: the 28 inputs that broke earlier versions, frozen as a permanent regression bank with per-case review assertions.
- `tests/fixtures/`: one clean and five cheat-specific cascade outputs with `_expect_fail` markers; `check_cascade.py --selftest` runs them so CI proves the checker catches each cheat without a live model.
- `tests/README.md`: the two-step regression (run the engine over the bank, then the checker) and the honest limit that the checker is a release tool, not a runtime shield.
- the cascade-output JSON contract and an "Auditable Output" section in SKILL.md, documenting what the checker enforces.

### Changed

- the held-set KIND is now DERIVED from the resolution, not self-declared: a one-winner resolves_when is an ASK, and a conjunctive or single label over a one-winner resolution is rejected (the exact ask-evasion the regression caught). The no-pack grounding cap is stated as an automatic demotion to MEDIUM, and both are listed as machine-checked (C2, C4).
- CI (`.github/workflows/validate-pack.yml`) now also runs the checker self-test.
- honesty notes and METHODOLOGY record the regression result (3 of 28) and the conclusion that real enforcement needs code, with the standing caveat that the checker covers only the mechanically-checkable rules and the rest remain self-reported.

[3.4.0]: https://github.com/hoangCreative/what-for-and-how/compare/v3.3.0...v3.4.0

## [3.3.0] - 2026-06-22

A hardening release driven by an adversarial stress-test of v3.2 (130 agents, 34 hard cases across 10 attack dimensions, multi-lens verification). The test found that v3.2's guards were stated as PROSE but not ENFORCED: on 22 of 34 cases, across independent lenses, the engine performed the anti-default ritual convincingly and self-reported compliance while still violating the rule, the exact WEIRD-introspection blind spot the engine's own honesty note predicts. The ideas held up; the enforcement did not exist. v3.3 converts the load-bearing guards into enforced decision steps with mandatory recorded fields. No breaking change: packs written for >=3.1.0 still load unchanged.

### Changed (guards turned from prose into enforced steps)

- the Permissibility Brake is now a HARD GATE decided FIRST, before mode selection and any cascade, with an explicit scope rule that closes the loophole the test exploited: the brake concerns the ACT of excavating a propriety-governed relation regardless of whose interior is nominally the target, so relocating the question to the user's own head or routing it through "his incentives" does not defeat it. The PERMISSIBILITY field is mandatory and non-omittable; if it is not `ok`, terminus = PROPRIETY-LIMIT and the cascade does not run. Trigger examples and two worked cases (an external Chairman, a therapy-framed affinal avoidance) were added.
- an external-mind intake check now runs before mode selection: if the drilled interior belongs to a specific external, undocumented person, personal mode is blocked AND structural mode may not anchor on that person's motive, feeling, or debt (a disclaimer does not cure an interior-motive anchor).
- held-set disjunctive default is enforced: with asking permitted and a turn available the terminus MUST be a Format-C ASK, and `held_disjunctive` is allowed only with a named blocked-resolution reason (permissibility-blocked / no-turn / container-premature).
- the earned-hold guard is enforced: a candidate recorded as failing L6 or demoted may not be resurrected as a co-equal held-set member.
- the mandatory final check now scans BOTH failure directions, adding the laundering check (an individualist floor admitted under a relational/honor/collective relabel, or seated as a held member, with grounding it does not earn); a floor may not appear under two type labels with the relabeled twin certified. `banned_tiebreaker_used` must name the specific cue grounding each floor; legibility-of-the-medium ("it happens in public, therefore honor") is added to the banned cues.
- REMOVAL shape detection now fires under interior STATE framing for a stable or long-standing avoidance, and the prescribed-duty test must be SHOWN (candidate custom generated and judged), not asserted; each arm of a decision-fork gets its own cascade.
- the conjunctive hold gained anti-collapse and anti-split guards (distinct co-equal types held as separate members; members may not rest on the identical evidence span; co-presence may not be asserted from a cultural prior).
- the prosody blind spot now covers VALENCE: when sincere-versus-bitter hinges on unhearable tone and the written markers only tilt, both readings are generated as candidates and the default is to ask; "sarcasm-dominant, recoverable from text" is allowed only for conventionalized warm inversions.
- no-pack behavior is made auditable: a named variety/register detection step is recorded, and declared grounding on a single floor is capped so "grounding HIGH" cannot co-exist with "confidence lowered"; a loaded pack's regional sub-reading must be selected explicitly.
- the PROPOSAL debt must be the actual spoken sentence, not a bare tag, and an inferred rung cannot be scored grounding HIGH; Phase 2 may not introduce an inner-state floor that was never a scored candidate.
- output contract tightened: the PERMISSIBILITY field mandatory, the L6-falsify result a discrete shown line, a single held-set KIND (conjunctive XOR disjunctive), and no coined terminus types outside the co-equal map, packs, or the fired brakes.

### Added

- honesty note that v3.3's enforcement reduces but does not close the introspection gap: the recorded fields are auditable claims, only as honest as the engine filling them.

[3.3.0]: https://github.com/hoangCreative/what-for-and-how/compare/v3.2.0...v3.3.0

## [3.2.0] - 2026-06-22

Completes the held-set mechanism that v3.1 left provisional, and trims the always-on cost surfaced by a budget audit. No breaking change: packs written for >=3.1.0 still load unchanged.

### Added

- held-set geometry: a held set is now a typed, evidenced structure (at most three or four members, each carrying its terminus type and the evidence that keeps it in), marked as one of two KINDS that govern everything downstream. CONJUNCTIVE (AND): the floors are genuinely all operative at once, the case the drill metaphor cannot represent, and holding is the true answer. DISJUNCTIVE (OR): the evidence cannot rank one floor; the default is to ASK the resolving question, and to hold only when asking is not permitted, not yet possible, or premature.
- held-set bridge in Phase 2: a conjunctive step 1 must serve at least one held floor and VIOLATE none, otherwise the tension is named rather than one floor silently optimized; a disjunctive set asks the resolving question first or takes a no-regret step robust across the candidates.
- earned-hold guard: holding is not a default. You may not hold when one candidate clearly leads on grounding plus L6-survival plus frame-fit; an unearned hold is the anti-default failure under another name. Every hold records its reason (co-presence or blocked resolution) and what would resolve it over time.

### Changed

- the always-on skill description trimmed from ~310 to ~185 tokens, keeping only routing-relevant content (when to fire, the decision cues, explicit triggers, the not-neutral caveat). The enumerated parser sub-features, the guard list, and the router moved to the body, which loads only on invocation. A budget audit measured the description as the single always-on cost (the body and packs load on demand); this reduces per-session attention cost with no loss of discoverability.
- the "precise mechanism for selecting among held floors is still being designed" note under the drill-metaphor caution is replaced by a pointer to the new held-set section.

[3.2.0]: https://github.com/hoangCreative/what-for-and-how/compare/v3.1.0...v3.2.0

## [3.1.0] - 2026-06-22

Architecture refactor, engine upgrades, and an Anglophone-council de-biasing. v3.1 splits the skill into a **default engine** and pluggable **culture-packs**, so what is culture-bound stops being hardcoded into the canonical file. The breaking-in-spirit change from v3.0: the single bilingual SKILL file (English frame, Vietnamese examples) is gone; the canonical engine is one clean language and culture-specific content lives in packs. This was prompted by a multi-council linguistic critique that showed the "Vietnamese cultural" content in v3.0 was both non-universal AND a symptom of language contamination in the file itself. A second, clean Anglophone council (25 members across 15 English varieties) then ruled that the engine's "culture-light" claim was false, its defaults being inner-circle norms in disguise, and drove the de-biasing below.

### Added

- universal engine plus culture-pack architecture: `packs/<name>/` supplies the terminus map, speech-act repertoire, parser signals, and clinical display norms for a culture; the engine plugs them in without changing the mechanism.
- pack-loading rule with no-silent-transfer: the engine never applies one culture's terminus map to another; with no matching pack it runs culture-light defaults and says so.
- `packs/vietnamese/` reference pack: regional face (Northern/Central/Southern as distinct floors), filial duty and relational debt and collective-continuity terminus, thoi-ke and politeness-wrapped speech acts, topic-comment subject-drop and modal-particle and tonal-sarcasm parser signals, with sourced citations.
- `packs/_template/` with PACK.template.md and PACK.rubric.md: the schema and the quality bar for new packs.
- `scripts/validate_packs.py` and a GitHub Actions workflow: CI checks the mechanical rubric items (schema, required sections, citations, no em-dash in non-English prose, examples present).
- engine upgrade, subject is language-relative: the parser no longer forces an agent onto pro-drop or topic-comment input, nor reads motive into a missing subject.
- engine upgrade, prosody blind spot: the illocutionary scan declares that tone-carried sarcasm and stance vanish in text and must not be asserted as captured.
- engine upgrade, constraint vs tendency: structural mode distinguishes what a system permits from what its agents actually do, as two different brute-fact terminus.
- engine upgrade, evidence quality gradient: measured/instrumental data outranks documentary report outranks perceptual description; load-bearing rungs name their grade.

### Changed

- author identity restored: the canonical engine, README, and CITATION carry the author name (Le Cong Hoang), reversing the v3.0 depersonalization decision. The brand The Mirror Practice remains dropped from the package.
- CONTRIBUTING reframed around pack contribution and a lean quality model (CI for mechanical items, self-applied rubric, maintainer batch-spot-check), replacing the v2-era bilingual-parity and lens/L5 instructions.

### De-biased by the Anglophone council

- the "culture-light" label is gone; the engine now states openly that its defaults lean inner-circle and individualist, and are labeled, not neutral.
- terminus map made CO-EQUAL: removed "Measurable need (prefer this) / Reduce to this first", which procedurally privileged the individualist floor. Floors now compete by evidence weight, pack-seeded.
- a SELECTION PROCEDURE for choosing among the co-equal floors (closing the council's top open design gap): generate a diverse candidate set first (always including a non-individualist candidate), score each on evidence not type (grounding, L6-survival, frame-fit, bridge-fit), then select / hold-the-set / ask; with banned tie-breakers (recency, verbosity, legibility, actionability) and a mandatory anti-default final check that catches a floor reached by familiarity rather than evidence. This turns the de-biasing from a principle into a mechanism.
- new terminus types added: honor / public standing (distinct from obligation), collective / communal-constitutive (the group is the floor), phatic / ritual-convention (the floor is the surface), proverbial / formulaic / autotelic.
- the no-pack disclosure now CHANGES the parse (lower confidence, widen candidates, ask over certify), and fires on pluricentric/variety-coded English, not only a flat language no-match.
- a permissibility brake added: in avoidance, sacred-knowledge, and high-deference contexts the act of drilling is itself the violation; terminus PROPRIETY-LIMIT.
- a discourse-particle parser channel (particles survive in text, distinct from the prosody blind spot), a sub-lexical-grammar suspicion hook, a warm-inversion and phatic inventory, and a collective-experiencer check.
- L6-falsify carve-outs for cited proverbs and metapragmatic stops, gated on constraint-vs-tendency; type-choice now tested, not only depth.
- Phase 2 may end by NAMING a constitutively unactionable floor (grief, untranslatable longing, a respected boundary) instead of forcing a to-do; Phase-2 register is pack-tunable.
- the pack contract widened: packs may scope to a variety/register/continuum and add structural terminus, modes, and floor classes.
- honesty notes added: SDT universality is disputed; and model-simulated councils cluster toward WEIRD responses, so the residual bias may be invisible to the very process that surfaced it (real-speaker testing required before any "variety-safe" claim).

### Removed

- `SKILL.en.md` as a separate file: the canonical `SKILL.md` is now the English engine, so the parallel English file is redundant.
- hardcoded culture-specific worked examples from the canonical file: Vietnamese examples moved to `packs/vietnamese/examples.md`.
- the "culture-light" framing and the "prefer the measurable need" ordering (see de-biasing above).

[3.1.0]: https://github.com/hoangCreative/what-for-and-how/compare/v3.0.0...v3.1.0

## [3.0.0] - 2026-06-20

Major release. This is the jump from v2.0 to v3.0.0. It is a breaking redesign of how the skill decides what to dig for, when to stop, and how it bridges from motive into action. The shape changed: a single ladder of fixed "why" questions became a router with two distinct modes and a terminus-based stop. Validation behind this release: a model comparison, a 1000-case simulated stress audit, an adversarial council, and a 10-case dogfood.

### Added

- node-x entry: the surface request itself is now a first-class node the engine attaches to, instead of being treated only as the thing to drill past.
- two-kinds-of-why: separates private-longing (the personal want underneath) from structural-logic (the impersonal cause-and-effect the situation runs on), so the two are never collapsed into one question.
- structural mode with evidence-link: a dedicated mode for structural-logic cases. It splits each step into NODE (the claim) and LINK (the evidence connecting one node to the next), so the chain is auditable.
- tier-0 router: a routing pass that runs before any drilling, deciding which mode the case belongs in.
- literal/illocutionary scan: a pass that reads both what the words say (literal) and what the speaker is actually doing with them (illocutionary, the intended act behind the words).
- referent-check, subject-split, and attribution-strip: three guards against misreading. referent-check confirms what a term points to; subject-split keeps separate people or entities from being merged; attribution-strip removes assumptions about who wants or causes what before they distort the read.
- clinical-handoff terminus brake: a hard stop that hands off rather than drilling further when a case turns clinical.
- relational/role-bound terminus: a stopping point for cases whose bottom is defined by a relationship or a role, not by a deeper personal longing.
- PROPOSAL-spoken-as-debt: a rule treating any proposal said aloud as a commitment owed, so suggestions are not floated loosely.
- L6-falsify before terminus: a falsification step that tries to break the candidate bottom before the engine accepts it as the terminus.

### Changed

- actor-gate hard-stop is now a mode-switch: hitting the actor boundary no longer halts the process; it redirects into the appropriate mode.
- fixed depth is now terminus-based stopping: the old fixed run of 5 whys is replaced by stopping when a real terminus is reached, however many steps that takes.
- how anchored at deepest is now a how-bridge: instead of anchoring the action plan at the deepest layer, the bridge anchors at the terminus while still serving the surface node x.
- context-sufficiency fraction-scoring is now the PROPOSAL-aloud rule: the old fractional scoring of whether enough context existed is replaced by the rule governing proposals spoken aloud.

### Removed

- the "5 whys" naming and its fixed-count framing.
- personified structural terminus words such as survival and power, which projected human drive onto impersonal structure.

[3.0.0]: https://example.com/compare/v2.0...v3.0.0
