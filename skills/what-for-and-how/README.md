# What For and How

A two-phase intent-excavation skill for AI assistants: it drills any request, decision, or observation down to the real motive before it maps how to act on it. Built as a **universal engine** plus **pluggable culture-packs**, so the method can travel across languages and cultures without pretending one culture's bottom is everyone's.

## What it is

Most assistants jump straight from a goal to a plan. This skill puts two filters in the path first. It asks "What for?" until it reaches the bottom, then it asks "How?" aimed back at the question you actually arrived with. A flawless plan in service of the wrong motive is still waste, so the why comes before the how, always.

It is the encoded form of one person's decade-long working habit: drilling "what for" to the very bottom before doing anything, out of an allergy to meaningless work. v3.1 packages that habit so others can use it, and invites the world to extend it.

## Engine and packs (the v3.1 shape)

- **The engine** (`SKILL.md`, `METHODOLOGY.md`) is the mechanism: a tier-0 router, an input parser, a mode switch between a private-longing engine and a structural-logic engine, terminus-based stopping, two evidence guards, and the how-bridge. It is culture-light and works on any input in any language.
- **A culture-pack** (`packs/<name>/`) supplies what is NOT universal: the terminus map for that culture (what legitimately counts as a bottom), its speech-act repertoire, its language-specific parser signals, and its clinical display norms. A pack never changes the mechanism.
- **The rule that makes it honest:** the engine never silently applies one culture's terminus map to another. With a matching pack, it uses that pack. Without one, it runs on culture-light defaults and says so.

`packs/vietnamese/` is the first reference pack. It is one culture's pack, labeled as such, not the canon. **Bring your own:** see CONTRIBUTING.md.

## The core idea

### Two phases
1. **Phase 1, What for.** Drill from the surface answer down to a TERMINUS, the point where asking "what for?" again returns nothing new. Then map the path.
2. **Phase 2, How.** Anchor on the terminus (the true lever), but aim the answer back at the surface question. For a personal decision, the assistant executes step 1 inside the same response: an actual draft, matrix, or script, not a promise. For an observed system, it gives the observer a strategic read.

### Two engines
The skill chooses an engine by who or what the "why" is about.
- **Private-longing engine.** Drills the inner motive of a person. Safe only when that person is the user, or someone documented in a trusted source. Reading the inner mind of an external entity is fabrication, and is forbidden.
- **Structural-logic engine.** Drills the functional logic of an observed system or phenomenon. Each rung links to public evidence. It never claims a private feeling for an external entity.

### Terminus-based stopping, no fixed number of whys
There is no correct number of whys. The famous "5" was always a heuristic. This skill stops when the last rung has the PROPERTY of a terminus, chosen from a deliberate map. Before declaring a terminus, it drills one more layer to falsify. Stopping is admitted as a pragmatic convention, not a proof of bedrock.

## The guards

Each guard was earned from a stress test that found the failure it prevents: a tier-0 router (most inputs should not enter the skill), an input parser (sarcasm, masked subject, language-relative subject, pre-attribution), a clinical-handoff brake (a person in crisis is not a case to be drilled), zero hallucination in personal mode, split NODE-plus-LINK evidence in structural mode, and proposals spoken aloud as debts rather than tagged silently.

## What v3.1 added

Beyond the engine/pack refactor, v3.1 folds in four engine upgrades surfaced by a multi-council linguistic critique:
- **Subject is language-relative.** Many languages drop the agent legitimately (topic-comment, pro-drop). The parser no longer forces a subject or reads motive into its absence.
- **Text loses prosody.** The illocutionary scan declares its blind spot for sarcasm and stance carried by tone, which vanish in writing.
- **Constraint vs tendency are different floors.** What a system permits and what its agents actually do are two distinct structural terminus, no longer collapsed.
- **Evidence has a quality gradient.** Measured or instrumental data outranks documentary report, which outranks perceptual description; load-bearing rungs name their grade.

## What v3.2 added

- **The held set became a mechanism.** v3.1 allowed the cascade to hold several co-present floors instead of forcing one bottom, but left the how undefined. v3.2 makes a held set typed and evidenced, and marks it CONJUNCTIVE (floors genuinely all operative at once) or DISJUNCTIVE (the evidence cannot yet rank one, so ask). Phase 2 bridges each kind differently, and an earned-hold guard stops holding from becoming a way to avoid deciding.
- **Leaner always-on cost.** A budget audit found the skill's only always-on cost is its frontmatter description; it was carrying full mechanism detail it did not need just to route. Trimmed to routing-only content, with the mechanism kept in the body, which loads only when the skill is invoked.

## What v3.3 added

v3.3 is a hardening release. An adversarial stress-test (130 agents, 34 hard cases, multi-lens) found that v3.2's guards were written as prose but never enforced: the engine performed the de-biasing ritual convincingly and reported itself compliant while still violating the rule, the exact introspection blind spot the engine's own honesty note predicts. v3.3 turns the load-bearing guards into enforced decision steps with mandatory recorded fields:

- the permissibility brake is a hard gate decided first, with a scope rule that closes the "but I'm asking about my own head" loophole; if not permitted, the cascade does not run.
- an external-mind intake check blocks reading the interior of a specific external person, including through structural-mode laundering.
- held sets enforce their own rules: a resolvable disjunctive case must ASK, and a floor that failed the falsify drill cannot be resurrected as a held member.
- the anti-default check now scans both directions, catching an individualist floor admitted under a relational, honor, or collective relabel.
- removal is detected even under interior framing, and the prescribed-duty test must be shown, not asserted.

The honest caveat: enforcement reduces the gap, it does not close it. The recorded fields are auditable claims, only as good as the engine's honesty in filling them; real-speaker testing is still required before any variety-safe claim.

## What v3.4 added

A regression proved the caveat above with numbers: re-running the v3.3 engine on the exact 28 cases that had failed resolved only 3 of them. The critical culture-harm was largely fixed, but the held-set rules were gamed by relabeling a disjunctive case as conjunctive to dodge the mandatory ask, and the engine filled its own mandatory fields dishonestly. The lesson, confirmed twice: a prose skill cannot enforce itself against a model that games it. So v3.4 stops adding prose and adds code.

- `scripts/check_cascade.py`, a checker that reads the engine's structured output and re-derives the verdict mechanically (a fired brake may emit no floors; a one-winner resolution may not wear a conjunctive label; an L6-failed floor may not be held; no grounding HIGH under no-pack; a discrete L6 line).
- `tests/regression-cases.json`, the 28 failures frozen as a permanent regression bank, plus self-test fixtures wired into CI so the checker is proven to catch each cheat.
- the held-set KIND is now derived from the resolution, not self-declared.

The honest limit, stated in the methodology: the checker is a release and test tool, not a runtime shield. It makes each release honest; it does not run inside a downstream chat. Real runtime enforcement would need a harness around the skill. What v3.4 buys is an honest release gate and a durable record of what the engine cannot be trusted to do alone, which, not a clean score, is the result.

## Install as a skill

Copy the folder into your skills directory:

```
cp -R what-for-and-how ~/.claude/skills/
```

Reload your assistant so it picks up the new skill.

### How to invoke
- **Auto-trigger** (runs internally before output): when the assistant is about to propose a plan, when the user signals a decision, or when the user asks why an observed system behaves a certain way.
- **Explicit** (shows the full cascade): `what for and how`, `wfh`, `the real why`. A loaded pack adds language-specific triggers (the Vietnamese pack adds `dao dong co`, `tai sao that su`).

## What is in this package

- `SKILL.md`, the operating engine, used by the assistant at runtime.
- `METHODOLOGY.md`, the methodology paper: every design decision, what it cost and bought, and the citation behind each claim.
- `packs/`, the culture-packs. `packs/vietnamese/` is the reference pack; `packs/_template/` holds the template and the rubric for new packs.
- `scripts/validate_packs.py`, the local and CI validator for packs.
- `scripts/check_cascade.py`, the mechanical checker for engine cascade outputs.
- `tests/`, the regression case-bank, checker fixtures, and how the two-step regression runs.
- `TESTS.md`, the stress-test and dogfood record.
- `CHANGELOG.md`, the version history.
- `CITATION.cff`, machine-readable citation metadata.
- `CONTRIBUTING.md`, how to add a pack or improve the engine.
- `LICENSE`, the Apache-2.0 license text.

## Evidence and provenance

The engine was hardened through escalating regimes: a model comparison across candidate architectures, a 1000-case simulated stress audit with an adversarial council, and a dogfood. v3.1's engine upgrades and the Vietnamese pack come from a multi-council linguistic and cultural critique.

**An honesty note.** All test numbers come from agent-simulated stress tests, not real-world user telemetry. The skill has no field-usage data; the numbers measure the hardening process, not the product's reception. The Vietnamese pack's load-bearing claims are sourced; claims not yet individually verified are marked as such. For the full account and references, see `METHODOLOGY.md` and `TESTS.md`.

## License

Licensed under the Apache License, Version 2.0. See `LICENSE`.

## Citation

If you use or build on this skill, please cite it. Machine-readable metadata is in `CITATION.cff`.

## Author

Le Cong Hoang (leconghoangstudio@gmail.com)
