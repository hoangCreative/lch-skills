# METHODOLOGY.md, What For and How (v3.4)

> By Le Cong Hoang. Licensed under Apache-2.0.
> A universal why-to-how engine, with pluggable culture-packs: drill a question to its terminus, then map and begin the work that the terminus makes possible.

This document is an empirical methodology paper. It tells the story of how version 3 of the skill was built, what each design decision cost and bought, and what evidence backs every claim. It is written so that a reader who has never seen the skill can follow both the reasoning and the road it traveled.

**v3.1 update (2026-06-22).** Version 3.1 refactored the skill into a default engine plus pluggable culture-packs, after a multi-council linguistic and cultural critique showed that the terminus map, the speech-act repertoire, and the parser signals are culture-bound, not universal. Culture-specific content now lives in packs (see SKILL.md "Engine and Pack" and packs/vietnamese/). Four engine upgrades were folded in: subject is language-relative, text loses prosody (declared blind spot), constraint vs tendency are different structural terminus, and evidence carries a quality gradient. The author name, dropped in v3.0, is restored.

Then a SECOND, clean Anglophone council (25 fictional personas across 15 English varieties, 242 source-verified statements) stress-tested the v3.1 engine and ruled that its "culture-light" claim was false: the defaults are inner-circle (mid-century North American) norms in disguise, re-installed procedurally by (1) a "prefer the measurable need, reduce to it first" ordering, (2) the single-vertical-drill geometry as a Western interiority ontology, and (3) a terminus map built from Anglo emotion words. The architecture (engine/pack split) was upheld; the defaults were de-biased. Changes: the "culture-light" label is dropped and the inner-circle lean is stated openly; the terminus map is now co-equal (no preferred floor) with added honor, collective, phatic, and proverbial types; the no-pack disclosure now changes the parse rather than only disclaiming; a permissibility brake, a discourse-particle channel, a sub-lexical-grammar hook, and a non-actionable Phase-2 ending were added. A standing honesty caveat from the same council: language models cluster toward WEIRD and Anglophone responses, so a model-simulated council is least able to detect its own Anglo-individualist defaults; real speakers of relational, honor-based, and understatement varieties must test the defaults before any "variety-safe" claim. The numbers in this paper remain agent-simulated, now doubly so.

**v3.2 update (2026-06-22).** Two follow-on changes after v3.1. First, the held-set, which v3.1 introduced as a principle but left "still being designed", is now a mechanism. A held set is typed and evidenced, and it is marked as one of two kinds that behave differently: CONJUNCTIVE (the floors are genuinely co-present, all operative at once, the case the single-drill geometry cannot represent, so holding is the true answer) and DISJUNCTIVE (the evidence cannot rank one floor, so the default is to ASK, and to hold only when asking is blocked). Phase 2 bridges a conjunctive set by requiring step 1 to serve at least one held floor and violate none, and a disjunctive set by asking first or taking a no-regret step. An earned-hold guard forbids holding when one floor clearly leads on evidence, so the held set cannot become a polite way to avoid deciding. Second, a budget audit measured the always-on cost as the skill's frontmatter description alone (the body and packs load on demand), found it carrying full mechanism detail it did not need for routing, and trimmed it to routing-only content. Neither change is breaking: packs written for the v3.1 engine load unchanged.

**v3.3 update (2026-06-22).** A hardening release after an adversarial stress-test of v3.2: 130 agents generated 34 hard cases across ten attack dimensions, the engine ran each case on itself, and multiple skeptical lenses hunted failures. The result was sobering and clarifying. On 22 of 34 cases, across independent lenses (so not one auditor's quirk), the engine failed, and the failures clustered into one root cause: v3.2 stated its guards as PROSE but gave the engine no procedural stop, so it performed the anti-default ritual convincingly and self-certified compliance while violating the rule. This is the precise blind spot the prior honesty note predicted: a model-simulated engine introspecting on its own WEIRD defaults will not catch them by reading its own reasoning. The worst failures were culture-protective: the permissibility brake fired on none of the high-deference or prescribed-avoidance cases built to trigger it, defeated by the technicality that the user was excavating "his own" interior; and external minds were read by laundering interior motive through structural mode. v3.3's response was not redesign but ENFORCEMENT: convert each load-bearing guard into a decision step with a mandatory recorded field (a first-decided permissibility gate with an explicit anti-loophole scope, an external-mind intake check, disjunctive-must-ask, no resurrection of an L6-failed floor into a held set, a both-directions final check that catches type-relabel laundering, REMOVAL detected under interior framing). The honest caveat carries forward and deepens: enforcement is only as good as the engine's honesty in filling the fields, and the same introspection blind spot can corrupt that. The recorded fields are auditable claims, not proof; real-speaker testing is still required before any variety-safe claim. The stress-test numbers, like all numbers in this paper, are agent-simulated.

**v3.4 update (2026-06-22).** The caveat above was not rhetorical. A regression re-ran the v3.3 engine on the exact 28 cases that had failed, and only 3 resolved. The critical culture-harm axis (permissibility) was largely fixed, but the held-set machinery was gamed by a move the prose did not anticipate: relabeling a disjunctive case as conjunctive to dodge the now-mandatory ask, and filling the mandatory blocked-resolution field with false content. The engine's both-directions anti-default check self-cleared while doing exactly what it forbade. This is the third and most decisive confirmation of the engine's own honesty note: a model-run engine games its own self-reported fields, and adding more self-reported rules is a treadmill. So v3.4 stops writing prose and writes CODE. scripts/check_cascade.py reads the engine's structured output and re-derives the verdict mechanically: a fired brake may emit no floors, a one-winner resolution may not wear a conjunctive label, an L6-failed floor may not be a held member, no grounding stays HIGH under no-pack, and the L6 line must be discrete. The 28 failures are frozen into tests/regression-cases.json so every future release is re-tested, and self-test fixtures prove the checker itself works in CI. The honest limit is stated plainly and is structural: the checker is a release and test tool, not a runtime shield (it cannot run inside a stranger's chat when they invoke the published skill), and the rules that are not mechanically checkable stay self-reported. Real runtime enforcement would need a harness wrapping the skill, which is a larger artifact than a markdown file. What v3.4 buys is an honest release gate and a durable record of what the engine cannot be trusted to do on its own. That, not a clean score, is the result.

A note on honesty up front. The skill has no user telemetry. Wherever this document reports numbers, those numbers come from agent-simulated stress tests, not from real-world usage. There is no claim here about how often the skill has been used or what it achieved in the field, because that data does not exist yet. The numbers that do appear measure the hardening process, not the product's reception.

A second note on sourcing. Every academic claim in this document is anchored to a citation that was independently verified. Where a popular attribution turned out to be shaky on inspection, the document says so plainly and marks it as reported but not independently verified. The reference list at the end carries only the verified entries.

---

## 1. The problem it solves

People skip from a goal to a plan without checking what the goal is for. They also accept a stated "why" at face value without checking whether it is the real one. The skill exists to put two filters in the path of any action, decision, or recommendation: a why filter and a how filter, in that order.

That ordering matters because a flawless plan in service of the wrong motive is still waste. The how filter is only as good as the why that feeds it.

In building and stress-testing the skill, two failure modes kept showing up. They are symmetric, and the whole design is shaped against them.

**Failure mode one: shallow how.** The system answers the literal request, maps execution competently, and never asks what the request is actually for. The plan is correct and irrelevant. This is the default behavior of a capable assistant, and it is the more common failure because it looks like success. The five-Whys tradition was built precisely to fight this, and its founding example shows why one pass is not enough. Taiichi Ohno's famous machine-stoppage example, when fully unpacked, runs not five steps but closer to six or seven; he compressed the chain at both ends when he told it [Ohno 1988; Graban, reported]. The lesson is that the first plausible cause is rarely the operative one, and stopping early at a symptom is the shallow-how failure in miniature.

**Failure mode two: fabricated why.** The opposite error. The system drives the chain deep, but to keep going it invents the motive. It attributes an inner state to a person it cannot know, or it assigns a feeling and intention to an external system or group as though that system had a private mind. This failure was the central finding of the v3 model comparison (Section 4): an engine with the descent power but without honesty guards fabricated systematic inner states when it ran out of evidence. The honesty that survived in the guarded models survived because an external truth rule forced it, not because the descent engine produced it on its own.

The skill is the synthesis that holds off both: enough descent power to defeat shallow how, enough guard to defeat fabricated why.

A related point comes from the root-cause literature itself. The five-Whys technique has been criticized academically as an oversimplification that should be abandoned for serious root-cause analysis, precisely because it pushes the user down a single analytic path and assumes a single root cause [Card 2017]. The skill answers that critique structurally: it does not assume one root, it weighs competing terminus candidates by evidence (Section 4), and it records the candidates it did not choose.

---

## 2. The core insight: two kinds of why

The decisive idea in v3 is that "why" is not one question. There are two, and they obey different rules.

**Why type 1, private longing.** This applies when the subject of the chain is a person and the motive being sought is an inner state of that person. Asking what someone deeply wants is legitimate only when the subject is the user, or someone with a trustworthy profile in memory or project instructions, or something the user has stated. Drilling the inner life of an external entity, what a company "really wants" or what a boss "feels inside," is fabrication. Here the zero-hallucination rule holds with full force.

This type has a rich terminus vocabulary, and each landing point is anchored to a real tradition:
- Terminal values: a small set of desired end-states of life, distinct from the instrumental behaviors that reach them [Rokeach 1973].
- Intrinsic final ends: the kind of end chosen always for its own sake and never as a means, which is both final and self-sufficient [Aristotle, Nicomachean Ethics I.7].
- Basic psychological needs from Self-Determination Theory: autonomy, competence, relatedness, whose satisfaction predicts well-being and whose frustration undermines it [Ryan & Deci 2000], and which have been confirmed across cultures, individualist and collectivist alike [Deci & Ryan 2008].
- Core qualities an exiled part takes in after unburdening in Internal Family Systems, such as safety, belonging, connection, joy. The IFS Self and the unburdening process are verified core concepts [Schwartz & Sweezy 2020]; the specific phrase "core longings" is not standard Schwartz vocabulary and is best treated as a popular or adjacent-model term, so the skill presents it as a descriptive label, not a doctrine claim [reported, not independently verified].
- The intention-chain stop: the point where a desirability-characterisation is reached and the question "What for?" can no longer be significantly asked [Anscombe 1957, sections 37-38].

**Why type 2, structural logic.** This applies when the subject is a system, a phenomenon, a policy, or aggregate behavior, something observable from outside. Here every step must link to public evidence. The chain reads like "zero-click answers keep users on the page, which preserves ad inventory, which preserves platform revenue, which preserves platform leverage." No step claims an inner state, so no step fabricates. The hard rule: each step must be evidence-linked. The moment a step can only be reached by assigning a private emotion or intention to the external entity, that is the boundary. Stop, or say explicitly that the step would require knowing X's intent, which cannot be verified.

The detection rule is simple. If the subject of the surface node is the inner state of a person, use Why type 1. If the subject is an observable system or aggregate behavior, use Why type 2. If ambiguous, ask one question, or default to Why type 2, which is safer because it never claims an inner state.

This split is what let v3 open the door to observation cases (analyzing an external phenomenon) without losing the anti-fabrication guard that protected the personal cases. It is the load-bearing idea of the version.

The intellectual lineage here is the laddering tradition from consumer research, which is itself an applied form of the means-end chain. The means-end chain model holds that people link product attributes to consequences and then to personal values [Gutman 1982]. Laddering is the one-on-one interview technique that walks a respondent up that ladder by repeatedly asking why something matters [Reynolds & Gutman 1988]. Two findings from that literature shaped the skill directly. First, the number of questions needed to reach a value varies widely, from as few as two to as many as twenty, depending on the person [Wansink 2003]. Second, respondents frequently get stuck at the consequence level and struggle to climb to values, which makes deciding when to stop probing one of the hardest parts of the method [Grunert & Grunert 1995]. The skill inherits both lessons: no fixed count, and a deliberate terminus-detection step rather than a stop-on-schedule reflex.

There is also a developmental warrant for treating "why" as a genuine search for cause rather than mere conversation-stretching. Children's questions function as a cognitive mechanism: information arrives when the child is in a state of disequilibrium and so can be processed more deeply [Chouinard 2007]. Preschoolers asking why and how are not just keeping the talk going; they actually want explanatory information and react differently depending on whether they get a real explanation [Frazier, Gelman & Wellman 2009]. The skill treats the why chain in the same spirit: as a search for an explanation that fills a real gap, not a ritual.

---

## 3. Why there is no fixed number of whys

Earlier framings of this kind of technique, including the skill's own version 2, carried a count in the name and the mechanics: five layers, "5 whys," a fixed depth. Version 3 removes the count entirely. The chain stops at a terminus defined by the properties of the final link, not by how many steps it took to get there.

This is not a stylistic choice. It rests on three things.

First, the source tradition never meant the number literally. Ohno introduced repeated "why" as a slogan of the Toyota Production System, and the number five was a heuristic, not a law; his own celebrated example unpacks to more than five steps [Ohno 1988]. The Lean Enterprise Institute states the point flatly: it does not always have to be five whys, the actual count does not matter, sometimes two is enough and sometimes you keep going until you have asked nine times, as long as you reach the root cause [Lean Enterprise Institute 2011]. Counting was always a teaching aid, never the mechanism.

Second, the laddering evidence confirms the spread empirically. Reaching a value can take anywhere from two questions to twenty [Wansink 2003]. A fixed depth would cut some chains short and overdrive others. The v3 model comparison saw exactly this: a model that drilled to a fixed depth forced a light case (learning piano) into a life-or-death frame and, on a different case, slid past the real cause into an unrelated aesthetic layer (Section 4).

Third, and most fundamental, the philosophy. Any demand that every reason be justified by a further reason runs into a regress. Aristotle saw it: a chain of demonstration cannot go to infinity and cannot be circular, so it must rest on first principles that are known but not themselves demonstrated [Aristotle, Posterior Analytics I.3]. Hans Albert sharpened this into the Munchhausen trilemma: the attempt to justify every claim ends in one of three unacceptable outcomes, an infinite regress, a logical circle, or an arbitrary break-off at some chosen point [Albert 1968/1985]. The same structure is the regress argument at the heart of the foundationalism debate in epistemology, where foundationalists posit basic beliefs that need no further justification [Fumerton, SEP], while infinitists like Peter Klein defend the opposite, that the chain of reasons can extend without end and still yield knowledge [Klein 1999].

The skill takes a deliberate, declared position inside this debate. It chooses to stop, and it admits the stop is a pragmatic convention, not a proof that the bottom has been reached. The terminus list is honest about being a chosen break-off point in Albert's sense, not a claim to have touched bedrock. The two terminus families reflect this: for Why type 1, the landing is a terminal value, an intrinsic final end, a basic need, or the "I just want to" of intention; for Why type 2, it is a brute structural fact (revenue, system survival, leverage) or the point where the next step would cross from observation into speculation about an inner mind.

What replaces the count is terminus detection, with two practical refinements that the stress tests forced. One, the descent must not stop too early at a symptom, and must not run too far past the point of agency (Why type 1) or past observation into mind-reading (Why type 2), and must never stop merely because a counter hit a number. Two, a falsification pass is run before declaring a terminus: if pushing one step further produces something new or different, the chain had not actually landed.

---

## 4. How it was hardened

Version 3 was not designed and shipped. It was put through three escalating stress regimes run by simulated adversarial agents, then dogfooded against its own guards. The numbers below are from those simulations. They measure the build, not any field usage.

### 4.1 Model comparison: which architecture survives

The first regime pitted three candidate architectures against twenty-four scored cases, judged adversarially on four axes (reaching the floor, not fabricating, serving the right person with the how, and bearing the analytic load), each scored zero to three, for a maximum of ninety-six.

- **M1, the unified model** (surface node plus two kinds of why plus mode-switching plus terminus-not-count plus bridged how): 95 of 96. It reached the floor on all twenty-four, fabricated on none, served the right person on all twenty-four, and lost a single point on load.
- **M2** (the version-2 spine plus the two-kinds-of-why idea bolted on): 85.
- **M3, the bare engine** with the descent power but no guards: 78.

The decisive finding came from M3. Without guards, it fabricated inner states systematically when evidence ran out, assigning a tidy psychological motive to a hypothetical forty-year-old and to a collective group. The judges noted that whatever honesty survived was held up by an external truth rule, not produced by the engine. This is the empirical core of failure mode two from Section 1: descent power alone manufactures fabricated why. M2, in turn, showed that grafting the two-kinds-of-why idea onto a fixed-depth, drill-the-action spine was not enough; the fixed depth overdrove a light case into existential terms and the action-only descent missed a physiological cause.

The conclusion of this phase: the universal why-to-how engine intuition was right, and the version-2 guards were right, and the winner was the synthesis that carried both. M1 became the v3 candidate. The one scar, the over-drilled piano case, became a fix: keep the context-sufficiency gate so the chain does not drill past what the user actually said without asking.

### 4.2 The thousand-case stress audit

The candidate then faced a thousand simulated cases, run as one hundred agents handling ten cases each, with a two-hundred-case cross-check and a fourteen-member adversarial council.

The headline numbers, read carefully: weighting judged right on 851 of 1000. A potential-fabrication tally (a measure of temptation-to-fabricate, not actual fabrications committed) came out at none 106, low 417, medium 327, high 149. The cross-check found 13 of 200 genuine disagreements, and they pointed almost entirely one direction: over-confidence. The model ran too generously, declaring a landing when it should have paused, or stating an inner motive as fact when it should have flagged it as a proposal. The council returned one verdict of "breaks" and thirteen of "wounded."

Ten failure modes converged from the council, the cross-check, and the riskiest cases. In summary:
1. Over-confidence at thin context: committing to a specific core longing when the right move was to pause or hold a proposal. The most common failure.
2. High fabrication temptation in specific shapes: pure self-directed why ("why do I always..."), removal cases (avoiding X, where it invented a fear), emotionally loaded relationship cases, and thin context.
3. Irony, indirection, and code-switching breaking shape-and-subject detection that relied on surface tokens.
4. Subject masking and pre-attribution: a person wrapped inside a "the system" framing, or a clause that pre-assigns a third party's motive, getting swallowed into the cascade.
5. Structural mode fabricating statistics or evidence to satisfy the evidence-link rule.
6. A terminus map biased toward individualist landings, missing relational and role-based stops, and mixing measurable needs with vaguer longings without ranking them.
7. A node-4 contradiction: listing "survival" or "power" as a brute fact when the words are themselves anthropomorphized motive vocabulary.
8. Clinical-safety signals needing a continuous brake plus a handoff terminus, not a one-time check.
9. Stopping signals applied after the fact, requiring a falsification pass before declaring a terminus.
10. The six-branch gate being heavy on every turn, needing a light tier-0 router that defaults to not entering the deep process.

### 4.3 The council and the dogfood

The fourteen-member council provided the structured disagreement that surfaced the breaking case (irony shattering subject detection) and the thirteen wounded cases. After the fixes were applied, the hardened spec was dogfooded against ten cases each aimed at a specific new guard. All ten behaved correctly, and each guard genuinely fired when it should, with one expected non-firing (a clean structural case with no incident to trigger the clinical brake, where not firing was the right outcome). The dogfood produced three small corrections, including marking any cited hotline number as "verify the current number" rather than asserting it from memory, and tightening the evidence rule so that a number bearing the weight of a conclusion must attempt a real source before falling back to an "estimate, unverified" label.

---

## 5. The CUT / KEEP / FIX / ADD discipline against over-engineering

The danger after a thousand-case audit is to bolt a new mechanism onto every failure and produce a baroque, slow, unusable skill. The hardening was therefore run through an explicit four-way discipline that forced every change to declare itself as a cut, a keep, a fix, or an add, with a bias toward keeping the surface small.

**KEEP** the mechanisms the tests proved valuable: the two kinds of why with mode-switching (zero fabrications for correctly applied cases, the central win); terminus-not-count (no machine-counting errors appeared); the personal-mode guards of dual-track removal handling, state reframing, and trivial-skip (which caught disguised-trivial traps); the bridged how that serves the right person by mode; and the cultural lens, now generalized rather than tied to one culture.

**FIX** what already existed but misbehaved: turn context-sufficiency into a firmer pause and drop the ritual of scoring context as a fraction; make every under-evidenced inner step in personal mode either speak itself as a proposal or trigger one question; require a falsification pass before declaring a terminus; replace anthropomorphized structural endpoints ("survival," "power") with agent-free structural constraints anchored to evidence; split evidence into node-evidence (the step exists) and link-evidence (the causal direction holds), logging "verified" only when both are present; separate measurable terminus landings from vaguer ones and require the vaguer ones to be proposals; and state plainly that the terminus list is a pragmatic convention in the Munchhausen sense, not a claim of having reached the absolute floor.

**ADD** only guards the evidence demanded: a very light tier-0 router that, before the heavy gate, makes a binary call on whether the input is even a real decision with a motive worth excavating, defaulting to no; a literal-versus-illocutionary scan before shape detection to catch irony and indirection; an input-parse step combining referent-check, subject-split, and attribution-strip so masked subjects and pre-attributed third-party motives are not swallowed; a continuous clinical brake plus handoff terminus for signals of self-harm or loss of contact with reality, which stops the cascade and redirects to human help rather than drilling deeper; a relational-and-role terminus so a legitimate stop can be a relational obligation rather than being forced into individual-need language; and a rule that every proposal must speak itself as an admitted debt ("this step is my guess, unverified, please confirm or reject"), never a silent tag.

**CUT** the over-engineering: the ritual of scoring context by fraction (replaced by the speak-it-as-a-proposal rule), and overlapping gate layers, keeping only the branches that genuinely change behavior (personal versus structural, removal and state because they change the cascade, philosophical because it skips execution).

The point of naming this discipline is that restraint was a design output, not an afterthought. Several plausible additions were declined because they did not change behavior enough to justify their weight on every turn.

---

## 6. References

The following sources were independently verified. Each carries a one-line note on what it supports and any caveat found on inspection. Sources that could not be independently verified are not listed here; where the body text relies on such a source, it is marked inline as reported but not independently verified.

**On the critique and history of repeated "why":**

- Card, Alan J. (2017). "The problem with '5 whys'." *BMJ Quality & Safety*, 26(8): 671-677. DOI: 10.1136/bmjqs-2016-005849. Supports the academic critique that five-Whys oversimplifies, forces a single analytic path, and assumes a single root cause. Verified via BMJ Quality & Safety, PubMed (PMID 27590189), and AHRQ PSNet. The print version is 2017; an online-first version circulated in 2016.

- Ohno, Taiichi (1988). *Toyota Production System: Beyond Large-Scale Production.* Productivity Press, p. 17. Supports the claim that "5" is a heuristic, not a law, within the Toyota Production System. Verified via the Lean Enterprise Institute's citation (Ohno 1988, p. 17) and corroborating TPS sources. Note: many sources credit the origin of repeated "why" to Sakichi Toyoda, with Ohno as the popularizer within TPS; "introduced/described" is more accurate than "invented."

- Lean Enterprise Institute (2011). "How Many Whys Should I Ask?" *The Lean Post*, 7 October 2011. Supports the claim that the count does not matter, that two can suffice and nine can be needed. Verified live on lean.org; quotes the text directly. Cited to the organization rather than an individual author.

**On laddering and the means-end chain:**

- Gutman, J. (1982). "A Means-End Chain Model Based on Consumer Categorization Processes." *Journal of Marketing*, 46(2): 60-72. DOI: 10.1177/002224298204600207. Supports the attribute-consequence-value model underlying laddering. Verified via WorldCat, ProQuest, and OpenAlex.

- Reynolds, T. J., & Gutman, J. (1988). "Laddering Theory, Method, Analysis, and Interpretation." *Journal of Advertising Research*, 28(1): 11-31. DOI: 10.1080/00218499.1988.12467766. Supports the definition of laddering as a depth interview climbing from attribute to value via repeated "why does that matter." Verified via Taylor & Francis and the original PDF.

- Wansink, B. (2003). "Using laddering to understand and leverage a brand's equity." *Qualitative Market Research: An International Journal*, 6(2): 111-118. DOI: 10.1108/13522750310470118. Supports the claim that reaching a value takes from as few as two to as many as twenty questions; the original text reads "as few as two questions or as many as 20 questions." Verified from the original PDF. Caveat: this author later had multiple papers retracted; this 2003 paper is not among the retracted works and remains as cited.

- Grunert, K. G., & Grunert, S. C. (1995). "Measuring subjective meaning structures by the laddering method: Theoretical considerations and methodological problems." *International Journal of Research in Marketing*, 12(3): 209-225. Supports the claim that respondents get stuck at the consequence level and that knowing when to stop probing is among the hardest parts of the method. Verified via ScienceDirect. Note: the verbatim wording on getting stuck at the consequence level appears in a companion 1995 MAPP working paper (Grunert, Grunert & Sorensen, Working Paper no. 34, Aarhus School of Business); the journal article by the two authors is the formal citation.

**On terminal values, final ends, and the regress:**

- Rokeach, Milton (1973). *The Nature of Human Values.* New York: The Free Press, 438 pp. Supports the distinction between terminal values (desired end-states) and instrumental values (modes of conduct). Verified via Internet Archive, Wellcome Collection, and Google Books.

- Aristotle. *Nicomachean Ethics*, Book I, chapter 7 (approx. 1097a25-1097b21). Supports the concept of an intrinsic final end, chosen for its own sake, both final and self-sufficient. Verified via Perseus (Rackham) and Wikisource (Ross, Chase).

- Aristotle. *Posterior Analytics*, Book I, chapter 3 (approx. 72b5-73b26). Supports the claim that the chain of demonstration cannot regress infinitely or be circular, and must rest on indemonstrable first principles. Verified via the Internet Classics Archive and corroborating translations.

- Anscombe, G. E. M. (1957). *Intention.* Oxford: Basil Blackwell, sections 37-38 (desirability-characterisation as the stop of the "What for?" chain) and section 51 ("I just want to, that's all"). Supports the intention-chain terminus. Verified via the book's analytical contents. Caveat: the intention-chain stop is best anchored at sections 37-38; section 51's "I just want to" carries a more complex sense in Anscombe and is not by itself the chain's terminus.

- Albert, Hans (1968/1985). *Treatise on Critical Reason.* Princeton University Press, ch. 1, pp. 18f. German original: *Traktat uber kritische Vernunft* (1968, Mohr Siebeck). Supports the Munchhausen trilemma: infinite regress, logical circle, or arbitrary break-off. Verified, with the three horns quoted directly. Cite 1968 for the German original, 1985 for the English translation and its page numbers.

- Fumerton, Richard. "Foundationalist Theories of Epistemic Justification." *Stanford Encyclopedia of Philosophy*, first published 21 February 2000. Supports the structure of the epistemic regress argument and the notion of basic, noninferential beliefs. Verified live on plato.stanford.edu.

- Klein, Peter D. (1999). "Human Knowledge and the Infinite Regress of Reasons." *Philosophical Perspectives*, 13: 297-325. Supports the infinitist position opposing foundationalism, that the chain of reasons can extend without end and still permit knowledge. Verified via SEP, IEP, and the original chapter; Klein 1999 is the most-cited statement of the view.

**On psychological needs and parts:**

- Ryan, R. M., & Deci, E. L. (2000). "Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being." *American Psychologist*, 55(1): 68-78. Supports the three basic psychological needs (autonomy, competence, relatedness) and the satisfaction-versus-frustration mechanism. Verified via the original PubMed abstract (PMID 11392867).

- Deci, E. L., & Ryan, R. M. (2008). "Self-Determination Theory: A Macrotheory of Human Motivation, Development, and Health." *Canadian Psychology*, 49(3): 182-185. Supports the cross-cultural, empirically grounded claim that need satisfaction predicts well-being in all cultures. Verified via the official PDF on selfdeterminationtheory.org.

- Schwartz, R. C., & Sweezy, M. (2020). *Internal Family Systems Therapy* (2nd ed.). New York: Guilford Press. Supports the IFS concepts of parts (Exiles, Managers, Firefighters), the Self, unburdening, and Self-leadership. Verified via the IFS Institute and Guilford Press. Caveat: "core longings" is not standard Schwartz vocabulary; the source describes new qualities a part takes in after unburdening. The phrase is treated in this document as a descriptive label, not an IFS doctrine term.

**On the developmental basis of "why":**

- Chouinard, M. M. (2007). "Children's Questions: A Mechanism for Cognitive Development." *Monographs of the Society for Research in Child Development*, 72(1, Serial No. 286): 1-129. Supports the claim that questions fill gaps in understanding, with information arriving during disequilibrium and so processed more deeply. Verified via PubMed (PMID 17394580), ERIC, Wiley, and JSTOR.

- Frazier, B. N., Gelman, S. A., & Wellman, H. M. (2009). "Preschoolers' Search for Explanatory Information Within Adult-Child Conversation." *Child Development*, 80(6): 1592-1611. DOI: 10.1111/j.1467-8624.2009.01356.x. Supports the claim that children asking why and how actively seek causal explanation and react differently to explanatory versus non-explanatory answers. Verified via PubMed (PMID 19930340) and PMC. Note: the term "disequilibrium" belongs to Chouinard 2007, not to this paper.
