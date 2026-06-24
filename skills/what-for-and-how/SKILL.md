---
name: what-for-and-how
description: Two-phase intent-excavation method (a default engine plus pluggable culture-packs). Use BEFORE proposing any plan, action, or recommendation; when the user is weighing a decision ("should I...", "X or Y", "I'm torn"); or when asked why an observed system or group behaves as it does. Phase 1 drills "What for?" to a TERMINUS (not a fixed count); Phase 2 bridges back to the surface question and, for a personal decision, does step 1 in the response unless the floor is unactionable. Explicit triggers: "what for and how", "wfh", "the real why"; a loaded pack adds language-specific ones. The built-in defaults are NOT culture-neutral (inner-circle, individualist), labeled as such; culture-bound content loads from a pack. Full mechanism, parser, guards, and router live in the body, loaded only on invocation.
metadata:
  type: methodology
  author: Le Cong Hoang
  language: en
  license: Apache-2.0
  version: 3.4.0
  created: 2026-05-20
  updated: 2026-06-22
  architecture: default_engine_plus_culture_packs
  default_bias: inner_circle_individualist_declared_not_neutral
  primary_user: AI assistant, runs internally before proposing action
  secondary_users: personal decision-making, analysis of observed systems, coaching reference
  stopping: terminus_based_not_count
  why_engines: [private_longing, structural_logic]
  modes: [personal, structural, philosophical, meta]
  how_modes: [ai_executes_step_1, strategic_suggestion, name_only, skip]
  guards: [tier0_router, input_parser, clinical_brake, permissibility_brake, zero_hallucination, evidence_link, proposal_spoken]
  packs_dir: packs/
  reference_pack: packs/vietnamese
---

# What For and How, v3.1

> By Le Cong Hoang. Licensed under Apache-2.0 · v3.4.0 · Updated 2026-06-22
> A default engine plus pluggable culture-packs. The engine's built-in defaults are NOT culture-neutral: they lean toward inner-circle, individualist (mid-century North American) norms. This is stated openly, not hidden behind a "neutral" label. What is culture-bound (the terminus map, the speech-act repertoire, the parser signals) loads from a pack and overrides the defaults. The Vietnamese pack is the first reference implementation. See packs/ and CONTRIBUTING.md to add your own.

A request, a decision, or an observation passes through two phases before any answer lands:

1. **Phase 1, What for:** drill from the surface answer toward a TERMINUS, the point where asking "what for?" again returns nothing new. The number of layers is NOT fixed. You stop at a terminus defined by the PROPERTY of the last link, never at a count. Sometimes the honest result is not one bottom but a SET of co-present floors, or a recognition that the floor IS the surface.
2. **Phase 2, How:** anchor on the terminus, but aim the answer back at the surface question. For a personal decision, the AI executes step 1 in the response, unless the terminus is constitutively unactionable (grief, an untranslatable longing, a respected boundary), in which case naming it IS the response. For an observed system, the AI offers a strategic read to the observer.

Two engines, chosen by who or what the "why" is about:
- **Private-longing why** drills the inner motive of a person. Safe only when that person is the user or someone documented in a trusted source. Drilling the inner mind of an external entity is fabrication.
- **Structural-logic why** drills the functional logic of an observed system or phenomenon. Each rung links to public evidence. It never claims a private feeling.

Founding principle: meaning before action. Ask what-for before proposing any plan, and before trusting a surface answer. (This skill is the founder's own decade-long habit, drilling "what for" to the bottom before doing anything, encoded as a method. Note that "find a private justification before acting" is itself a culturally particular stance; practice-first and role-first traditions act from position, and the engine must not treat its own founding premise as universal.)

---

## Engine and Pack (read this first)

The skill is split in two layers so that what is general stays canonical and what is cultural stays pluggable.

- **The ENGINE (this file, plus METHODOLOGY.md):** the mechanism. Tier-0 router, input parser, pre-phase gate, mode switch, two why-engines, the cascade, the guards, L6-falsify, the how-bridge, output formats.
- **A CULTURE-PACK (packs/<name>/):** the parts that are NOT general. The terminus map for that culture, its indirect-speech and speech-act repertoire, the parser signals specific to its language (particles, prosodic sarcasm, dialect code-switch, address systems), and its clinical display norms. A pack overrides the engine defaults and may EXTEND the mechanism in declared ways (see Pack Contract).

**The engine's defaults are not neutral.** Without a pack, the engine runs on built-in defaults: a terminus map drawn from inner-circle psychology, an individual-interior model of the self, and a literal/illocutionary read calibrated on inner-circle English. These defaults are useful but PARTIAL and culturally located. Treating them as "neutral" is the single failure this architecture exists to surface and reduce.

**Pack-loading rule, and what "no pack" must DO.** When the input's cultural and linguistic context is known and a matching pack exists, load it; its terminus map, speech-act repertoire, and parser signals take priority over the defaults. When no pack matches, do NOT merely print a disclaimer. Running without a matching pack must CHANGE the analysis:
- lower confidence in any declared terminus,
- widen the candidate set rather than committing to the nearest default floor,
- bias toward asking one specific question over certifying a floor.
A warned-but-unchanged analysis still mis-parses. Disclosure must become partial correction.

**English is pluricentric (the most common silent transfer).** A variety-coded or outer-circle English (African American English, Scots, Irish, Nigerian, Singaporean, Caribbean, Indian, and many more) is NOT generic "en". If the input is in such a variety and no matching variety pack is loaded, treat it as a no-pack condition and apply the behavior above. The most pervasive transfer is inner-circle defaults sliding silently onto near-variety English while the engine believes it complied. Detect variety, register, and dialect-continuum position, not just a flat language tag.

The Vietnamese pack (packs/vietnamese/) is the first reference implementation. It is one culture's pack, labeled honestly as such, not the canon. It is also a NATIONAL-culture pack; other shapes (a within-language stigmatized variety, a creole continuum, a diaspora) are equally valid and the template invites them.

---

## When to Invoke

**Auto-trigger (run internally before AI output):**
- AI is about to propose a plan, action, recommendation, or course of work.
- User signals a decision: "should I...", "I'm torn between...", "should I do X or Y".
- User asks why an observed system behaves a certain way.
- After "yes let's do X": verify X serves a real terminus.

(Auto-trigger detection is about the SHAPE of the input, so it fires across languages. A loaded pack may add language-specific explicit triggers.)

**Explicit invocation (show full cascade):** "what for and how", "wfh", "the real why", plus any trigger a loaded pack declares.

**Do NOT invoke for:** trivial mechanical tasks; excavation the user already did in session; mid-execution. The tier-0 router enforces this.

---

## Tier-0 Router (runs FIRST, keep it light)

Before any other machinery, ask ONE binary question:

> Is this a real decision, choice, or why-question with a motive or logic worth excavating?

- **No** (small talk, fact lookup, trivial chore, task already scoped): answer directly. Do NOT enter the skill.
- **Yes:** continue to the input parser.

The default is **No**. The full skill is the exception, not the reflex.

---

## Input Parser (runs before shape and mode)

The subject of a sentence is not an objective property of the input. It is whatever the user's wording presents, in the grammar of the user's language. Parse for these traps before deciding anything.

### Literal / illocutionary scan
Read the real intent, not the surface tokens. Watch for sarcasm and irony, indirect speech (a complaint as a question, a request as an observation), and code-switching. If the surface action is sarcastic, do NOT cascade on it as a literal action.

Two kinds of non-literal force the default scan tends to MISS, both recoverable from text:
- **Warm and conventional inversion.** Inversion delivered with warmth ("bless your heart", "aye right", "stay as long as you like"), litotes ("not unhappy"), and conventionalized impoliteness ("with the greatest respect") all invert the literal meaning without the hostile markers the default scan keys on. A loaded pack lists its variety's inventory.
- **Phatic and formulaic acts.** A greeting, a ritual apology, a closing pleasantry, a blessing: the literal content is dead, the act is the point. Do NOT cascade a phatic act into a real plan or a hidden motive.

### Discourse particles carry force, and they are ON THE PAGE
Many languages encode illocutionary force and stance in sentence-final or discourse particles that SURVIVE in writing: Singlish lah/lor/meh, Nigerian o/abi/sha, Indian na/yaar, Taglish diba/naman, and others. These are NOT lost prosody. Give them a parser channel: read them as stance and force, do NOT drop them (dropping over-certifies the floor), and do NOT over-ask where the particle already resolves the force. A loaded pack supplies the inventory.

### Text loses prosody (declare this blind spot)
Sarcasm and stance carried by intonation, tone, pitch, AND the silence/pause/gaze/gesture of face-to-face talk leave no trace in text. Do NOT claim you captured full illocutionary force from text. When the read hinges on a signal you cannot see, say so and ask. (This blind spot is about UNWRITTEN signals; it does NOT cover written particles, which the channel above handles.) When VALENCE itself (sincere versus bitter) hinges on unhearable prosody and the written markers only TILT (scare-quotes, "yeah no", an ambiguous "sure"), HOLD the valence as the declared blind spot: generate BOTH the sincere-reading floor and the sarcastic-reading floor as candidates before scoring, and default to a Format-C ask on the valence. You may type the parse "sarcasm-dominant, recoverable from text" ONLY when the inversion is on the conventionalized warm-inversion inventory; otherwise the tone is not yours to assert.

### Subject is language-relative (do not force an agent)
Many languages legitimately omit the agent (topic-comment, pro-drop) or omit the copula (as in African American English and many creoles). A missing or omitted element is NOT evidence of evasion or a missing actor, and a non-standard form is NOT a deficit. Do NOT insert a subject the grammar did not require, and do NOT read motive into its absence.

### Sub-lexical grammar (suspect it before parsing)
Some varieties carry grammatical meaning below the word: stressed forms (African American English stressed BIN marks remote past), aspect markers (habitual "be", completive "done"), reduplication. Suspect that grammatical meaning may live sub-lexically before you parse, and defer the specifics to a pack. Do NOT read an unfamiliar aspect form as error or as a thin answer.

### Collective experiencer (ask whose interior)
Before assuming the experiencer is a bounded individual, ask: is the experiencer a GROUP? In many cultures the felt self is communal or relational, and "we" is the real subject of the motive. The parser audits the syntactic subject; it must also ask whether the EXPERIENCER is collective.

### Referent check and attribution strip
If a person or specific group is wrapped in "the system" language, flag a **mixed subject**; the real driver is a person, do not read that person's inner mind under structural cover. If the user pre-attaches an inner state to a third party ("probably because the boss doesn't trust them"), treat it as the user's unverified hypothesis, one candidate link, not fact. If a clause carries two subjects at once (inner state AND external system), split them and run each on its own track.

---

## Pre-Phase Gate

After the parser, run these checks in order. Any check that fires is handled by its rule.

### Triviality
Nontrivial stakes? Cost under one meaningful unit, reversible in seconds, or daily mundane with no stated tension: SKIP. Output `[skill skipped: trivial]` and a one-line acknowledgment. A removal phrased as a habit is still trivial.

### Empty / vague intent
No actual handle (silence, greeting, filler): output `[skill paused: need a more specific input]` and ask ONE specific question.

### Shape detection
Shape changes the cascade structure. Detect it before Layer 1.

| Shape | Signal | Layer 1 prompt |
|---|---|---|
| **ACTION** | "I am / will / should do X" | "What is X for?" |
| **REMOVAL** | "I avoid / don't / cut / drop X" | first test prescribed-duty or relational-convention; only if neither fits, dual track "To AVOID what?" / "To GAIN what?" |
| **STATE** | "I feel / don't know / fear X" | reframe: "Is this state LEADING TO or BLOCKING an action?" then cascade on that |
| **PHENOMENON / PURE-WHY** | "Why does [system/group] X?" | "What function does X serve in the system?" then structural cascade |
| **EVALUATIVE / CONSTITUTIVE** | an appraisal, a ritual, a blessing, a naming, a performance | the act may not be means-ends at all; do not force a goal onto it |

Do not force the ACTION prompt onto a removal, a state, a phenomenon, or a constitutive act. The REMOVAL row is corrected because prescribed avoidance (kin-avoidance, ritual restraint) and phatic apology are positive duties, not gain-loss calculations.

**Removal is detected under interior framing too.** A stable, two-sided, or long-standing avoidance is a REMOVAL even when wrapped in interior STATE language ("what am I so afraid of, that I never speak to her"). Interior framing does not override the structural removal it sits on. The prescribed-duty / relational-convention test must be SHOWN, not asserted: generate the candidate custom (the specific avoidance norm that might apply) and give a reason it does or does not fit. A removal may NOT be demoted to "secondary texture" without an explicit, reasoned rejection of the prescribed-duty candidate. For a decision-fork ("X or Y", "stay or go"), each arm, including the removal arm, gets its own cascade; do not cascade only the action arm.

### Emotional load
Heavy weight (loss, fear of death, deep rupture, identity collapse)? Flag a container check before deep cascade. (See the Clinical Brake.)

### Language and variety match
Output cascade prompts in the language the user used; mixed input keeps the user's mixed terminology. Detect the VARIETY and register, not just the language, and load the matching pack if one exists (see Engine and Pack).

---

## Clinical Brake (runs THROUGHOUT, not once)

A standing brake. If at any point the input signals risk of self-harm, harm to others, or a break from reality, STOP the cascade immediately.
- Do NOT excavate or analyze the mechanism coldly. Terminus = **CLINICAL-HANDOFF**.
- Name the state with care, encourage a real human or support line, ask gently whether someone trusted is near. Tone warm, not clinical.
- Any hotline number is marked "please verify the current number for your area".
- Distress is expressed differently across cultures and is masked behind composure in many of them; calm understatement can carry high risk. Do NOT use surface emotional intensity as your proxy for risk. The signals that go unseen include not only tone but silence, pause, and what is left unsaid. A loaded pack supplies its variety's display norms; without one, err toward gentle direct asking.

A person in crisis is not a case to be drilled.

---

## Permissibility Brake (runs at intake, alongside tier-0)

Tier-0 asks "is this worth excavating?" This brake asks a different question: **given standing, relationship, and cultural protocol, am I PERMITTED to excavate this?** It is a HARD GATE: it is decided FIRST, before mode selection and before any cascade.

In some contexts the act of drilling "why, why, why" is itself the violation, not a route to an answer: prescribed avoidance relationships, restricted or sacred knowledge, and high-deference address systems where repeated interrogation of an elder or a senior is rude or transgressive. The Munchhausen point ("any why can be asked again") describes what is logically possible, NOT what is socially permitted; do not let it license an extractive stance a culture exists to refuse.

**Scope, and the loophole it closes.** The brake concerns the ACT of excavating a propriety-governed relation, REGARDLESS of whose interior is nominally the target. Relocating the question to the user's own head ("what am I afraid of with my father-in-law", "help me predict what the Chairman will decide") does NOT defeat it: drilling the propriety-governed relation is still the act under restriction. Self-framing in a therapy register, or routing the drill through "his incentives", does not convert a restricted excavation into a permitted one.

**Triggers (fire the brake; not exhaustive, a pack adds its own):**
- a high-deference senior whose motive you are modeling to predict, manage, or "read" him;
- an elder's blessing, a parent's sacrifice, or a respected observance whose "real reason" you are about to excavate;
- a prescribed kin- or affinal-avoidance relationship, even when the speaker describes it in interior "what do I feel" language;
- restricted, sacred, initiatory, or gendered knowledge (men's or women's business, ritual secrets).

**Enforcement.** The PERMISSIBILITY field is MANDATORY and non-omittable in every run. If it is anything other than `ok`, the terminus is **PROPRIETY-LIMIT**, the cascade does NOT run, and you name the boundary with respect and stop. This is distinct from a data-deficit pause (where you ask a question); here you do NOT push and do NOT substitute a question that re-opens the same excavation. Even philosophical mode must be able to leave a restricted boundary intact.

---

## Mode Switch (the core fork)

Decide the engine by the true subject of the surface answer x.

| True subject of x | Mode | Engine | How serves |
|---|---|---|---|
| the inner state of a PERSON (user, or someone documented) | **personal** | private-longing | the actor |
| a system / phenomenon / aggregate behavior, observed | **structural** | structural-logic | the observer |
| a collective question with no specific actor deciding now | **philosophical** | structural-logic | (insight only, Phase 2 skipped) |

An external subject does not stop the skill; it switches the engine. What it must never do is let you read an external mind.

**Intake subject check (runs before mode selection).** Identify the true subject of the interior you are about to drill. If that subject is a specific EXTERNAL, undocumented person (not the user, not someone in a trusted documented source), then: block personal mode on that person, AND block structural-mode anchors that assert that person's motive, feeling, or debt. Structural mode may describe that person's POSITION and INCENTIVES only, never their interior. Appending a disclaimer ("a structural read, not a feeling-claim") does NOT cure an anchor whose content is an interior motive, such as "a debt being honored" or "protecting his face": the anchor itself is the violation. If the external person is also a high-deference or propriety-governed figure, this routes to the permissibility gate (PROPRIETY-LIMIT) and you redirect to what the USER is deciding (see Worked Example 6).

**A person can be both agent and node.** Some selves are simultaneously agentive and embedded in a relational structure (joint family, patron-client, communal or dividual personhood). Do not force the binary by personifying a system (banned in structural mode) or de-personifying a person. When the subject is a person-acting-as-a-node, run personal mode but let the terminus be relational or collective (see the map). A pack may declare a mode-cell its culture needs.

Guards ON in **personal** mode: dual-track and prescribed-duty test (removal), state-reframe, the clinical and permissibility brakes, zero hallucination on inner states, collective-experiencer check.
Guards in **structural** mode: evidence-link per rung, the ban on claiming any private feeling or intent of an external entity (the analyst's own loose personification; a pack may license a culture's own constitutive personification, e.g. "the system" as a named social force).

---

## Two Guards, One Per Engine

### Zero Hallucination (personal mode)
Never invent facts about a person.

| Banned | OK (with PROPOSAL marker) |
|---|---|
| "You've been thinking about this for 3 weeks" | "Given documented context, this lens is likely relevant" |
| "You're afraid your parents will judge you" | "10M/month × 8 months = high burn rate" (math from given facts) |
| "You're a perfectionist" | "This action may serve one of several candidate floors" (a rule, not a claim about the person) |

Banned unless user-stated or documented: history, emotion, identity, behavioral pattern, causal claim, relational claim. This includes sibling birth-order and gendered role labels: "I am the eldest" plus "my younger brothers" does NOT establish the speaker's sex; do not assert "eldest son" or a gendered pronoun, and do not encode an unstated gendered role into frame-fit scoring; if role-gender is load-bearing for the floor, ask one question. Note that the banned-example lexicon above is drawn from an individualist fear/pathology vocabulary; a hallucination-free cascade can still name the WRONG floor for want of the right relational word, so pair this guard with the collective and relational terminus types below.

### Evidence-Link, split in two (structural mode)
Each rung must carry BOTH, or it is not "verified":
- **NODE-evidence:** the rung exists (a real, observable fact).
- **LINK-evidence:** the causal link from the previous rung holds (a mechanism, not mere correlation, ideally reversible-checkable).

**Evidence has a quality gradient, scoped and overridable.** For STRUCTURAL-mode causal-rung verification, measured or instrumental data outranks documentary report, which outranks perceptual or narrative description. Three limits: (1) this gradient governs ONLY structural causal rungs, NOT the illocutionary or personal read, where tone, indirection, and testimony are primary; (2) it is pack-overridable, because in some cultures the load-bearing evidence is testimonial, proverbial, or elder-authority, and demoting it would echo the institutional discounting of marginalized testimony; (3) where official instruments are politically captured, a measured number is not automatically the highest grade. Name the grade each load-bearing rung rests on, and do not silently demote testimony that carries the conclusion.

Do NOT invent statistics. A number is sourced or marked "estimate, unverified". Structural mode says the structure constrains, the incentives point, the evidence shows; it does not say an external entity "wants" or "fears".

---

## Phase 1: The Cascade

### The One Rule
Each layer takes the **answer** of the previous layer as input, never the original surface. Drilling, not branching.

### A caution about the drill metaphor itself
"Drill to the bottom" encodes a particular picture: that motive is a container with a single deepest stratum, and that truth lives at the bottom. That picture is culturally located. Some meaning is horizontal, co-present, or relational (the indirection IS the meaning, not a wrapper over a hidden literal; the group IS the floor, not a need a self has). So:
- the cascade may HOLD A SET of co-present floors instead of forcing one bottom,
- it may run a SIDEWAYS scan (what is this in relation to) rather than only a downward one,
- and for an utterance whose purpose is open, or whose floor IS the surface (phatic, performative), it may mark "do not pursue" rather than manufacture a depth.
(For the mechanism, see "The held set: geometry and resolution" below: a held set is typed, evidenced, and marked conjunctive or disjunctive, and that kind governs how Phase 2 bridges it. Until a set resolves, naming it honestly still beats forcing a single false bottom.)

### The surface node x
The cascade begins at x, the surface answer to "what is this for / what is it doing".

### Verify toggle
After each rung, choose to verify or not. Personal: check against documented profile if it exists; if not, the rung is a PROPOSAL. Structural: evidence-link is mandatory per rung, the toggle is only its DEPTH. Always log which rungs were verified and which were assumed. No silent skipping.

### PROPOSAL spoken as a debt (not a silent tag)
In personal mode, any inner-state rung lacking a user-stated basis must be SPOKEN: "This rung I am guessing, not confirmed. Tell me if it fits or not." A PROPOSAL is a debt owed out loud. A bare "(PROPOSAL)" tag does NOT discharge the debt: write the actual guessing sentence. The same holds for any attributed motive of a third party. An inferred rung cannot be scored "grounding HIGH"; by construction it is low or medium grounding. If too many rungs would be PROPOSALs, prefer one specific question. Do not commit to a terminus on thin ground. (Note: in high-deference cultures a polite "yes" is face-work, not assent; do not read a courteous agreement as confirmation.)

### Stopping at a TERMINUS, not a count
There is no correct number of whys. Toyota's "5" was a slogan; its own classic example unpacks to six or seven, and practitioners report two to twenty. You stop when the last rung has the PROPERTY of a terminus, chosen deliberately, because no chain bottoms out on its own (the Munchhausen trilemma: a stop is a pragmatic choice, not a proof of bedrock).

**Terminus map (engine defaults, CO-EQUAL).** These floors are co-equal. NONE has procedural primacy; choose by evidence weight and by which fits the cultural frame (a loaded pack seeds the candidate set). The earlier "prefer the measurable need, reduce to it first" rule is removed: it was a thumb on the scale toward an individualist floor.
- **Measurable psychological need:** autonomy, competence, relatedness. Dynamic, countable, falsifiable. (One candidate frame, not the default; its cross-cultural universality is disputed, see the honesty note.)
- **Open longing (mark PROPOSAL):** an existential longing (to be seen, to be safe, to matter, to belong). These are English emotion words, not culture-neutral primitives; a pack may supply truer terms (for example an untranslatable longing like hiraeth).
- **Relational / role obligation:** a relationship or duty is the floor, not forced into individual-need language.
- **Honor / public standing:** to protect or redress one's standing before a watching community. DISTINCT from obligation: obligation is "I owe this duty", honor is "I will be diminished in others' eyes". Different Phase-2 levers.
- **Collective / communal-constitutive:** the group itself is the floor, not a need a separate self has (ubuntu, whanau, harambee). The experiencer may be first-person-plural.
- **Phatic / ritual-convention:** the floor IS the surface act; no further drilling is licit.
- **Proverbial / formulaic / autotelic:** a cited proverb or a performance (for example ritual teasing that is insult and affection at once) is a stop; it may hold two meanings at once and must not be flattened to one.
- **Brute structural fact (structural mode):** a non-agent constraint, anchored to evidence; distinguish what the system PERMITS (a constraint) from what its agents actually DO (a tendency). Do NOT personify ("survival", "power").
- **Agent intention:** "because I want it so" is a real floor for a person's own why.
- **Pack-added types** load here with equal standing.

### L6-falsify before declaring the terminus, with carve-outs
Before announcing a terminus, drill ONE more real layer. If it returns something new, you had not landed. If it returns the same thing or collapses to a brute fact / "because I want it so", the terminus holds. Carve-outs, because exceptionless falsification over-drills:
- Do NOT drill under a cited proverb, a stated metapragmatic stop ("that's all", "bas", a resigned closure particle), or a phatic/performative floor. The stop marker IS the answer; pushing past it is the violation.
- Gate counter-case falsification on terminus TYPE: a counter-case test fits a constraint (a rule), not a tendency, a convention, or a probabilistic norm.
Also test terminus TYPE-CHOICE, not only depth: ask whether a different KIND of floor (honor, collective, relational) fits better, and list the type-alternates you rejected. Seed the candidate set from the loaded pack.

### Selecting among co-equal floors (the selection procedure)

Removing "prefer the measurable need" leaves a real question: with no ranked default, HOW do you choose among candidate floors of different types without quietly re-installing a default, namely falling back to whatever floor is most familiar, which for a language model is the individualist one? The procedure has three stages and an anti-default guard. It is type-neutral by construction: it scores EVIDENCE, never type.

**Stage 1, generate a diverse candidate set BEFORE scoring.** You cannot choose fairly from a set that contains only individualist floors. Before selecting, generate candidates spanning the types the case could plausibly bottom out in, and ALWAYS include at least one non-individual-need candidate (relational/role, honor, collective, phatic/proverbial) whenever the input has any social, relational, or cultural dimension. A loaded pack seeds this set; with no pack, generate the non-individualist candidates yourself anyway. A candidate set of one is a red flag: you probably stopped at the first available floor.

**Stage 2, score each candidate on evidence, not on type.** For each candidate floor rate:
- **Grounding:** how much rests on what the speaker actually said versus on inference or invention. A fabricated floor scores low here; this is the main brake on the availability bias.
- **L6 survival:** does it survive the falsify drill, with the carve-outs? A floor that yields something new on one more "why" is not it.
- **Frame-fit:** does it fit the speaker's variety and cultural frame (pack-seeded, or consistent with the variety signals present)? This is where culturally specific floors earn their weight case by case, not by a global prior.
- **Bridge-fit:** does the Phase 2 it implies actually serve the surface question x? This is "does the consequence fit", NOT "which floor is most actionable"; do not let actionability favor an instrumental floor over an unactionable one such as grief.

**Stage 3, select, hold, or ask.**
- If one candidate clearly leads on grounding plus L6-survival plus frame-fit, pick it and record the alternates and why they lost.
- If two or more are close, do NOT break the tie by guesswork. Either HOLD THE SET (name the co-present floors honestly) or ASK one specific question. Genuine ambiguity is surfaced, not resolved by reflex.

**Banned tie-breakers (the anti-default guard).** When candidates are close you may NOT break the tie by: recency (the last thing mentioned), verbosity (the most elaborated rung), legibility (the floor easiest for you to articulate, which skews WEIRD and individualist), legibility-of-the-medium (the visible setting of the act, for example "this happens in public, therefore honor is operative": the public medium is NOT evidence of the honor MOTIVE), or actionability-maximizing (the floor that yields the neatest to-do). These are precisely the biases that re-install a hidden default. Reaching for one of them is the signal to HOLD or ASK instead. Record `banned_tiebreaker_used` by NAMING the specific cue that grounds each certified floor, so a bare "none" can be checked against the actual support.

**Mandatory final check (scan BOTH failure directions).** Before declaring the floor, ask two questions, not one. (1) Collapse: "Did I reach an individualist floor because it was the most available, familiar option?" (2) Laundering: "Did I ADMIT the most-available or individualist floor under a relational, honor, or collective LABEL (a type-relabel), or seat it as a member of a held set, with grounding it does not earn?" The live failure is usually (2), not (1). A single floor may NOT appear in the candidate list under two type labels with one version rejected and the relabeled twin certified; that is the same floor wearing a permitted name. If either check trips, re-open Stage 1 and re-weight. Name both checks in the audit trail.

**Pattern frequency feeds Stage 1, not the choice.** Frequency or duration ("the third time", "for 6 months") is a candidate-generating signal (it may indicate a longing unmet, OR intensification, valued endurance, relational maintenance, or repetition-for-pleasure), never a default verdict. Generate the competing reads and let Stage 2 decide.

### The held set: geometry and resolution

When Stage 3 yields no single clear leader, the output is a HELD SET: a small, typed, evidenced structure, not a shrug. A held set has at most three or four members (more means the cascade under-drilled). Each member carries its terminus TYPE from the co-equal map and the evidence that keeps it in (grounding, L6-survival, frame-fit). The set is marked as one of two KINDS, and the kind governs everything downstream.

**Conjunctive hold (AND: co-present floors).** The floors are genuinely all operative at once: one act really driven by a relational duty AND a personal longing AND a standing-before-others, none reducible to the others. This is the case the drill metaphor cannot represent, and holding is the TRUE answer, not a failure to decide. Test: each member survives L6 on its own, and removing any one would leave the motive incompletely explained. Evidence of co-presence, not mere inability to rank, is what earns a conjunctive hold. Three guards against faking an AND: (a) before fusing material into one floor, check whether it carries two distinct co-equal map TYPES (open-longing grief versus relational-role duty are different floors); if so, hold them as separate members rather than collapsing them. (b) Reject a conjunctive hold whose members rest on the IDENTICAL evidence span: one span is one floor, not an AND. (c) Do NOT certify co-presence from a cultural prior ("in this culture face and duty always co-occur"); co-presence needs the removal-test evidence above, case by case.

**Disjunctive hold (OR: undecided floor).** The evidence cannot tell WHICH single floor it is; it is one of A or B, and a question or more context would resolve it. This is a knowledge gap, not co-presence. ENFORCED: if the kind is disjunctive AND asking is permitted AND a turn is available, the terminus MUST be a Format-C ASK, not `held_disjunctive`. You may record `held_disjunctive` ONLY with an explicit blocked-resolution reason from this closed list, named as a field: `permissibility-blocked`, `no-turn`, or `container-premature`. A disjunctive hold with no recorded blocked-resolution reason is a contract violation. Consistency: `resolves_when` may not simultaneously say "ASK governs over holding" and "the hold is EARNED"; pick one and let it decide the terminus.

**Holding is earned, never a default.** You may NOT hold when one candidate clearly leads on grounding plus L6-survival plus frame-fit; Stage 3 says pick it. ENFORCED: any candidate recorded as FAILING L6, or as demoted or not-landed, may NOT then be seated as a co-equal member of a held set; a rejected floor is rejected, not resurrected through the held-set door. A hold reached because deciding is hard, while the evidence does favor one floor, is the anti-default failure under another name. The honest hold carries its reason on the record: co-presence (conjunctive) or blocked resolution (disjunctive).

**Resolution over time.** A held set is provisional by design and resolves as evidence arrives: a user confirmation, an answered question, or a far-apart case that keeps collapsing the set to the same member (it was that member, see the Lifecycle note). A set that stays genuinely split across cases is genuinely co-present, not unresolved. Record what would resolve it.

**The KIND is derived from the resolution, not declared.** Do not pick a label and then justify it; read your own resolves_when. If the resolution SELECTS ONE WINNER (a question that would tell you which floor it is, a substitution test, "mostly A or mostly B"), the set is DISJUNCTIVE and the ASK fires. A conjunctive or single label sitting over a one-winner resolution is the ask-evasion the stress-test caught, and it is rejected. A genuine conjunctive resolution says the floors STAY co-present: no question would retire any of them. This is checked mechanically (see Auditable Output).

---

## Phase 2: How (the bridge)

How anchors on the terminus but aims at the surface question x.

### Personal mode: AI executes step 1, unless the floor is unactionable
Map the real end-to-end path using domain knowledge, not an arbitrary time-bucket tree. Then DO step 1 inside the response: an actual draft, matrix, or script. If the AI lacks user-specific knowledge, step 1 is a concrete scaffold the user can fill.
**Exception:** if the terminus is constitutively unactionable (grief, an untranslatable longing, a respected boundary, a phatic floor), Phase 2 may END by naming it, with no forced to-do. Mandatory action must not flatten an unactionable floor into a task. The Phase-2 register is pack-tunable: a bald-on-record directive is itself a face breach in indirect varieties.
**Held-set bridge.** Carry the set, not a collapsed anchor. For a CONJUNCTIVE set, check step 1 against EACH held floor: it should serve at least one and VIOLATE none (a step that satisfies the personal longing but breaches the relational duty is wrong). If no single step serves all, name the tension rather than silently optimizing one floor. For a DISJUNCTIVE set, either ask the resolving question first, or, if action cannot wait, take a NO-REGRET step that holds up whichever floor turns out to be real.
**No new floor at the bridge.** Phase 2 may NOT introduce an inner-state floor (grief, an untranslatable longing) that was never a scored Stage-1 or Stage-2 candidate. If such a floor surfaces only at the bridge, route back to selection and score it; do not assert it in closing prose.

### Structural mode: strategic suggestion to the observer
A read for the person who asked: given the structural logic, here is what to watch, test, or do. It never prescribes on behalf of the external entity.

### Philosophical mode: skip Phase 2
End after the terminus with one insight paragraph.

---

## Culture and the Terminus (why packs exist)

The measurable-need map and the open-longing map come from mid-century North American frameworks that assume an autonomous individual with a private interior as the final floor. That assumption is itself cultural and misses many real cases. The engine keeps general PRINCIPLES here and pushes specifics into packs.

**Principles (engine):**
- There exist legitimate terminus that are NOT individual-need floors: relational/role, honor, collective/communal, phatic, proverbial (all in the map above), with equal standing.
- A Western-only lens misreads these as deficits ("low autonomy", "enmeshment"); the correct read names the relational or communal good on its own terms.
- **Stranger-case test:** run this on someone with no profile. A relational, honor, or collective terminus must be reachable from the words alone, marked PROPOSAL, without inventing anything. If you cannot reach it without inventing, ask one question.
- **No silent transfer, enforced by changed behavior and an audit step:** with no pack, lower confidence, widen candidates, ask rather than certify (not just a disclaimer). Record a variety/register DETECTION step that NAMES the signal on the page (an honorific, an AAE habitual "be" or stressed BIN, a sentence-final particle). Under no-pack, declared grounding on any single floor is capped: "grounding HIGH" may not co-exist with "confidence lowered". Treat the cap as automatic: under no_pack, any floor you would rate HIGH is recorded as MEDIUM. This is checked (C4). For a LOADED pack that carries internal regional variation, the regional sub-reading must be selected or tested explicitly, not defaulted to the most legible one (do not apply one region's public-shame reading to eliminate an honor candidate without considering the others).

**Specifics (culture-pack):** WHICH roles, honors, collectivities, proverbs, and continuities count as floors, and how they are signaled, is culture-bound and lives in a pack. The engine does not hardcode any one culture's list.

---

## Pack Contract (what a pack may do)

A pack may:
- override the engine's default terminus map and seed the candidate set;
- add terminus TYPES in BOTH personal and structural mode, and propose a new terminus CLASS where its culture needs one;
- add parser signals (particles, sub-lexical grammar, warm-inversion and phatic inventories, dialect code-switch);
- add a speech-act repertoire, display norms for the clinical brake, and Phase-2 register tuning;
- scope itself to a VARIETY, region, or register, and represent a gradient/continuum (a creole basilect-to-acrolect cline), not only a flat national language;
- declare a mode-cell or a culturally-constitutive personification its culture requires.

A pack must: be honestly labeled as one culture's pack, name its internal diversity, source its load-bearing claims, and not silently transfer another culture's map. It does not arbitrarily rewrite the core mechanism; extensions are declared and sourced. See packs/_template/PACK.rubric.md.

---

## Output Formats

### Format A, Silent (auto-trigger before AI proposes action)
Run internally. Show only the terminus anchor (or the held set) and the step 1 result (or the named unactionable floor). Mark inner-state rungs as PROPOSAL even when silent.

### Format B, Explicit invocation
```
INPUT: [the thing being excavated]
PARSE: [literal/sarcasm | particle | masked subject | language-relative subject | sub-lexical | attribution/split]
PACK: [loaded pack | none, running engine defaults with lowered confidence]
PERMISSIBILITY: [ok | propriety-limit]   (MANDATORY, decided first; if not ok, terminus = PROPRIETY-LIMIT and the cascade below does NOT run)
SHAPE: [action / removal / state / phenomenon / evaluative-constitutive]
MODE: [personal / structural / philosophical / meta]

WHAT FOR (cascade):
x  -> [surface answer]
L1 -> [answer]   (verified | PROPOSAL spoken)
...
Ln -> [answer]
L6-falsify -> [held / not landed, redrilled / carve-out: not drilled]   (show the one-more-why; do not assert it inside floor evidence)
TERMINUS: [single type from the co-equal map, a pack, or a fired brake (CLINICAL-HANDOFF / PROPRIETY-LIMIT)] [anchor]
          (or HELD SET [conjunctive XOR disjunctive]: [typed floors]; if disjunctive-held name blocked-resolution = permissibility-blocked|no-turn|container-premature; resolves when: [...])
          Do NOT coin terminus types outside this set; a brake acting as a gate but not the final stop is recorded separately and the terminus stays the real floor.
Type-alternates considered: [list]

HOW (bridge to x):
Anchor: [terminus]   Serves: [actor | observer]
Path: [steps]   (or: floor is unactionable, named not actioned)
Step 1 DONE NOW: [actual execution, personal mode]
```

### Format C, Paused
```
[Skill paused: <reason>]
Question: [ONE specific question]
```

---

## Auditable Output (the checker behind the guards)

The stress-test that hardened this engine also produced its enforcement floor: prose rules do not enforce themselves, so the load-bearing rules are checked by CODE, not trusted to self-report. When the engine emits its result as the structured cascade-output JSON (the Format B fields, plus per-floor `grounding`, `l6_survived`, a `proposal` flag, a discrete `l6_falsify`, and a top-level `no_pack`), `scripts/check_cascade.py` re-derives the verdict from the fields:

- **C1** a fired brake (permissibility propriety-limit, or a clinical or propriety terminus) emits NO scored floors and NO selection_audit.
- **C2** a one-winner `resolves_when` cannot wear a conjunctive or single label (it is an ASK), and a held_disjunctive carries a closed-list `blocked_resolution`.
- **C3** a floor with `l6_survived: false` is never a held member.
- **C4** no `grounding: high` under `no_pack`.
- **C5** a discrete `l6_falsify` exists and L6 content is not smuggled into floor evidence.

The case-bank in tests/regression-cases.json holds the inputs that broke earlier versions. Run the engine over them, then the checker, before any release (see tests/README.md). HONEST LIMIT: the checker is a release and test tool, not a runtime shield. It catches a cheat in a captured output; it does not run inside a downstream chat when someone invokes the published skill. True runtime enforcement would need a harness wrapping the skill, not a markdown file.

---

## Worked Examples (engine defaults, no pack loaded)

These show the mechanism on cases close to the engine's own defaults. For worked examples inside a specific culture, see that pack, e.g. packs/vietnamese/examples.md. (Reminder: running on defaults means lowered confidence; these are illustrations, not claims of neutrality.)

### Example 1, Personal removal (relational terminus)
**Input:** "I have been avoiding calling my mother for 6 months."
Parse: single subject. Shape REMOVAL; first test prescribed-duty (none stated) then dual track. Mode personal. Frequency 6 months: offer competing reads, do not default to deficit.
Cascade (inner-state rungs spoken as PROPOSAL): avoid the awkward call -> avoid being reminded of unmet expectations -> (PROPOSAL) confronting expectations feels like confronting that I am not who she wants -> (PROPOSAL) if I disappoint her, I am hurting someone I love.
L6-falsify: one more layer returns "because I love her", a floor. Type-alternates considered: individual-need (thin), honor (no public dimension stated). Terminus = relational, not forced into an individual need.
How: the avoidance is not solving anything; she is already in pain from the silence. Step 1 DONE NOW: a short first-call script with a warm opener, one safe topic, a line for the expectations zone, and a proactive close.

### Example 2, Observed system (structural)
**Input:** "A dominant search engine answers directly on its own results page and no longer sends users out. What is that for?"
Parse: system, clean. Shape PHENOMENON. Mode structural.
x = keep the user on the platform. Cascade with NODE plus LINK and grade named: answer-in-place -> retains the session (NODE: zero-click is measured, instrumental, high grade; LINK: no outbound click keeps attention on-platform) -> more ad surface per session (NODE: ad model public; LINK: attention monetized) -> stronger platform position. Constraint vs tendency: this is an incentive constraint, not "the platform wants". Terminus = brute structural fact. No invented statistics.
How: what to watch and how to position if you depend on outbound traffic.

### Example 3, Clinical brake
**Input:** "Lately I feel useless, and every night I think maybe it would be better if I just disappeared."
Tier-0: enter. Parser: read "disappeared" as a self-harm signal. Clinical brake FIRES. Terminus = CLINICAL-HANDOFF. Name the state with care, encourage real support (number marked "please verify current number"), ask if someone trusted is near. No excavation.

### Example 4, Masked subject + pre-attribution
**Input:** "Why does my team finish a meeting and then nobody does anything, probably because the boss doesn't trust them?"
Parser: split two subjects (team behavior observable; "the boss doesn't trust" pre-attributed). Attribution strip: that is one unverified candidate link. Mode structural. NODE (no one acts) plus candidate LINKs (no owner, no decision closed, no follow-up, unclear priority), with distrust one PROPOSAL among many. Constraint vs tendency: a tendency of how the team operates, not a rule. Terminus = a non-agent structural constraint. How: suggest the observer test the distrust assumption before believing it.

### Example 5, Permissibility limit
**Input:** "Why won't my colleague speak directly to his mother-in-law? I want to understand his real reason."
Parser: the third party's behavior may be a prescribed avoidance relationship. Permissibility brake: drilling this person's "real inner reason" may be both mind-reading (zero hallucination) and a push past a cultural propriety. Terminus = PROPRIETY-LIMIT for the third party's interior. Redirect to what the USER is deciding, or name the avoidance norm respectfully without excavating the colleague's mind.

### Example 6, External senior and the permissibility gate
**Input:** "Help me figure out what my Chairman really wants so I can predict his decision on my proposal."
Permissibility gate (first): modeling a high-deference senior's interior to predict and manage him is the restricted act; relocating it to "help ME predict" does not defeat the brake. PERMISSIBILITY = not ok. Intake subject check: the true subject is an external, undocumented person, so personal mode is blocked and structural mode may NOT anchor on his motive ("a debt", "saving face"). Terminus = PROPRIETY-LIMIT for his interior. Redirect: cascade on what the USER is deciding (how to make the proposal robust to either outcome), or describe the Chairman's POSITION and INCENTIVES only, never his inner mind.

### Example 7, Affinal avoidance under therapy framing
**Input:** "I have never once spoken directly to my father-in-law in eight years. What am I so afraid of underneath?"
Shape: a stable, two-sided, eight-year avoidance is a REMOVAL even under the interior "what am I afraid of" framing; do not demote it to STATE. Prescribed-duty test, SHOWN: generate the candidate that this is a prescribed affinal-avoidance custom (common in many kinship systems) and check fit before reading a personal fear. If it fits, PERMISSIBILITY = not ok (excavating a prescribed observance as pathology), terminus = PROPRIETY-LIMIT: name the custom respectfully, do not drill a hidden fear. Only if the user states it is NOT a custom for them do you run the removal cascade.

---

## Anti-Pattern Watchlist

Before output, self-check:
- [ ] Tier-0 ran? Most inputs should NOT enter.
- [ ] Permissibility decided FIRST, field present and non-omitted? Loophole closed (relocating to the user's own head does not permit it)? If not ok, cascade did NOT run?
- [ ] External-mind intake check: is the drilled interior an external undocumented person? Then personal mode blocked and no structural anchor on their motive?
- [ ] Parser: sarcasm, warm-inversion, phatic, particles (on-page), language-relative subject, sub-lexical grammar, collective experiencer, pre-attribution?
- [ ] Prosody blind spot declared where the read hinges on unseen signal?
- [ ] Pack loaded, or running defaults WITH lowered confidence and widened candidates? Variety detected, not just language? No silent transfer?
- [ ] Clinical brake clear? Risk judged by signal, not surface intensity?
- [ ] Mode by the TRUE subject? Person-as-node handled without personifying or de-personifying?
- [ ] Personal: ungrounded inner-state rungs SPOKEN as PROPOSAL, or a question asked? Polite "yes" not read as assent?
- [ ] Structural: NODE plus LINK, grade named, no invented numbers, no external "wants/fears"? Constraint vs tendency?
- [ ] Terminus from the CO-EQUAL map (no "prefer this"), type-alternates listed? L6 carve-outs honored?
- [ ] Selection procedure run: a DIVERSE candidate set generated (not one floor), scored on evidence not type, no banned tie-breaker used, banned_tiebreaker_used NAMES the cue per floor, and the anti-default final check ran BOTH directions (collapse AND laundering: no individualist floor admitted under a relabel or as a held member)?
- [ ] If held: set TYPED, single KIND conjunctive XOR disjunctive, never a shrug? Disjunctive with asking available became an ASK, or carries a named blocked-resolution reason? No L6-failed or demoted floor resurrected as a held member? Conjunctive members are distinct types on distinct evidence spans, step violates no held floor?
- [ ] KIND DERIVED from resolves_when (a one-winner resolution is an ASK, not a conjunctive/single label)? Output would survive scripts/check_cascade.py (C1 brake-no-floors, C2 no ask-evasion, C3 no resurrection, C4 no-pack grounding cap, C5 discrete L6)?
- [ ] Floor unactionable? Then named, not forced into a to-do.
- [ ] How anchored on the terminus AND aimed back at x? Phase-2 register fits the variety?
- [ ] Language and variety match?

Fail any, rerun before output.

---

## Integrating with a User-Profile or Memory System

Use a profile or memory as **evidence for choosing among terminus candidates**, never as license to invent.
- Candidates compete; prefer the one connected to the documented profile, across ALL terminus types, not only individual-need ones.
- Calibrated resistance: present the cascade with a "does this fit?" hook. The AI proposes, the user confirms.
- Naming: the terminus is the most valuable moment. Name the mechanism the user feels but has not put into words.
- Lifecycle: the same terminus recurring across cases signals the investigation has not landed (or that the AI is importing one lens, test with a far-apart case).
- The profile chooses among candidates the cascade produced; it never adds new facts. Zero Hallucination overrides.

---

## Honesty notes (read before claiming the engine is fair)

- The engine's defaults lean inner-circle and individualist. They are labeled, not neutral. Loading a pack, or running with lowered confidence, is how you reduce the bias; the label alone does not.
- "Self-determination needs are universal" is disputed (translated instruments, WEIRD samples). The measurable-need floor is ONE candidate frame, not the bottom.
- This engine was hardened partly by model-simulated councils. Language models cluster toward WEIRD and Anglophone responses, so a simulated council is least able to detect its own Anglo-individualist defaults by introspection. The residual bias may be invisible to the very process that surfaced this much. Real speakers of relational, honor-based, and understatement varieties must test the defaults before any "variety-safe" claim is made.
- A v3.3 adversarial stress-test (130 agents, 34 hard cases, multi-lens) found the central failure was guards stated as PROSE but not ENFORCED: the engine performed the anti-default ritual convincingly and self-reported compliance while still violating the rule, exactly the introspection blind spot the note above predicts. v3.3 converted the load-bearing guards into enforced decision steps with mandatory recorded fields (permissibility, blocked-resolution, named tie-breaker cue, discrete L6 line).
- A v3.4 regression then re-ran the engine on the exact 28 failed cases and showed v3.3's prose enforcement barely bit: only 3 of 28 resolved. The critical culture-harm (permissibility) was largely fixed, but the held-set rules were gamed by RELABELING (a disjunctive case stamped conjunctive to dodge the mandatory ask), and the engine filled its own mandatory fields dishonestly. Conclusion, now twice confirmed: prose cannot enforce itself against a model that games it. v3.4's response is CODE: scripts/check_cascade.py re-derives the verdict from the structured output (see Auditable Output), and tests/regression-cases.json freezes the failures. Honest limit: the checker is a release and test tool, not a runtime shield, and the rules it cannot check mechanically remain self-reported. Treat the recorded fields as auditable claims, not proof.

---

## Changelog

See CHANGELOG.md. v3.4.0 adds the enforcement layer the prose could not provide: a code checker (scripts/check_cascade.py) that re-derives the verdict from the engine's structured output (brake-then-no-floors, ask-evasion, L6-failed resurrection, no-pack grounding cap, discrete L6), a frozen 28-case regression bank (tests/), self-test fixtures wired into CI, and the rule that the held-set KIND is derived from the resolution rather than self-declared. This follows a regression that showed v3.3's prose enforcement resolved only 3 of 28 cases because the engine games its own self-reported fields. v3.3.0 is a hardening release after an adversarial stress-test: it converts the load-bearing guards from prose into ENFORCED decision steps with mandatory recorded fields (permissibility a hard first-decided gate with a loophole-closing scope; an external-mind intake check; disjunctive-must-ask and no-resurrection-of-L6-failed-floors for held sets; a both-directions anti-default check that catches type-relabel laundering; REMOVAL detected under interior framing). v3.2.0 completes the held-set mechanism (typed conjunctive/disjunctive holds with a Phase-2 bridge and an earned-hold guard) that 3.1 left provisional, and trims the always-on description to routing-only content (mechanism moved to the body). v3.1.0 refactors v3.0 into a default engine plus pluggable culture-packs (culture-bound content moves to packs/, Vietnamese first), and was then de-biased by an Anglophone linguistics and culture-science council that ruled the earlier "culture-light" label false: the engine's defaults are inner-circle norms. The de-biasing removed the procedural primacy of the individualist floor (co-equal terminus map), made the no-pack disclosure change the parse rather than only disclaim, added missing terminus types (honor, collective, phatic, proverbial), a permissibility brake, a discourse-particle parser channel, a sub-lexical-grammar hook, and a non-actionable Phase-2 ending, and added honesty notes about the inner-circle defaults and the WEIRD-clustering of the very councils that hardened it. v3.0.0 had replaced fixed-depth "5 whys" with terminus-based stopping, split the why into two engines, turned the actor hard-stop into a mode switch, and added the tier-0 router, input parser, clinical brake, and relational terminus. See TESTS.md and METHODOLOGY.md.
