# Methodology: ground or abstain

The detailed account behind the skill. What the discipline is, where every part of it comes from in the world's prior art, how it was tested, and where it honestly fails.

## 1. The discipline

One rule: before you assert, ground the claim in a real external source consulted this turn, or abstain and say it is unverified.

It is the encoded form of a Vietnamese working discipline named "xac tin" (roughly, verified conviction), coined on 2026-06-14 when the plain instruction "verify" was followed too loosely and let an assistant's work go shallow. The skill exists because an assistant's default is to push output that is confident, complete, and forward-moving even when it has not actually checked.

### The source chain, ordered by freshness not authority

1. **Community first, because it is the freshest signal.** GitHub issues, Reddit, forums, Stack Overflow. Community is the entry point, checked first because it is the most up to date, NOT because it is correct. Empty community is data, not permission.
2. **Then web and official sources**, used to test the community claim (including for evidence it is wrong), not merely to confirm a hope.
3. **Never the model's own training memory as a source.** Three reasons: stale past the cutoff, distorted by compression, colored by the model's own idiosyncratic take. A recollection is a hypothesis, never the evidence.
4. **Reason across the gathered sources only at the end.** This is the one place the model's intelligence is used, not its information. Score the source and the claim separately. Reasoning may operate only on facts that are themselves settled or explicitly assumed.

### Three clarifications that sharpen it

These are the load-bearing distinctions, stated by the discipline's author and not always explicit in the older frameworks:

- **Community is checked first for FRESHNESS, decoupled from correctness.** "Community first" means "most current signal", not "most trustworthy source". Its truth is resolved later, at the reasoning step.
- **The ban is on the model's INFORMATION, not its INTELLIGENCE.** Its stored facts are barred as a source; its ability to weigh gathered sources is used, and only at the last step.
- **The output shows its seams.** Every claim is marked settled (with its source inline), assumed, or to-verify. The reader can see which is which.

## 2. Prior art: where each part comes from

This discipline is not a new mechanism. Every moving part has an ancestor. Naming them honestly is part of the method.

### Human-domain frameworks

- **Lateral reading** (Sam Wineburg & Sarah McGrew, Stanford History Education Group, 2017 to 2019): leave the page you are on and check what the wider field says first. This is the behavioral core of "community is the entry point, not the truth". Grounded in a measured study where professional fact-checkers beat PhD historians on credibility judgments. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3048994
- **SIFT / the four moves** (Mike Caulfield, 2019): Stop, Investigate the source, Find better coverage, Trace claims to origin. The "Stop" reflex (catch your own reaction first) is borrowed directly. https://hapgood.us/2019/06/19/sift-the-four-moves/
- **The Admiralty / NATO code** (AJP-2.1, naval origin): score source reliability (A to F) and information credibility (1 to 6) on independent axes. The direct ancestor of "score the source and the claim separately". https://en.wikipedia.org/wiki/Admiralty_code
- **Intelligence-community analytic tradecraft** (ODNI ICD 203, 2007 rev. 2015/2023; ICD 206 sourcing): distinguishes information from assumptions from judgments, and treats "age and continued currency of information" as a quality factor. The three-way split settled / assumed / to-verify is adapted from ICD 203's sharper three-way distinction. https://www.intelligence.gov/assets/documents/intelligence-community-directives/ICD_203.pdf
- **The Sagan standard** (Carl Sagan, lineage Hume to Laplace to Truzzi): extraordinary claims require extraordinary evidence. This motivates sizing the self-check loop to the blast radius. https://en.wikipedia.org/wiki/Extraordinary_claims_require_extraordinary_evidence
- **CRAAP test** (Sarah Blakeslee, CSU Chico, 2004): Currency, Relevance, Authority, Accuracy, Purpose. The one classic framework that names currency at all, though as one axis among five, not as the ordering principle.
- **IFCN code of principles** (Poynter, 2016) and **Structured Analytic Techniques** (Richards Heuer, 1999): institutional transparency, and externalizing reasoning to fight the analyst's own bias.

### AI-side techniques

These are mechanisms; this skill is a behavioral discipline that the mechanisms enable.

- **RAG** (Lewis et al., 2020): condition on retrieved documents instead of parametric memory. https://arxiv.org/abs/2005.11401
- **ReAct** (Yao et al., 2022): interleave reasoning and tool actions, so the model gathers external info before concluding. The mechanical enabler of "go search before you answer". https://arxiv.org/abs/2210.03629
- **Chain-of-Verification** (Dhuliawala et al., 2023): draft, plan verification questions, answer them independently so they are not biased by the draft, revise. The basis for "each pass comes from a different angle, your first answer cannot validate itself". https://arxiv.org/abs/2309.11495
- **SelfCheckGPT** (Manakul et al., 2023) and **self-consistency** (Wang et al., 2022): sample multiple times, distrust a single confident generation. Informs the loop.
- **FacTool** (Chern et al., 2023): decompose output into claims and verify each with external tools. https://arxiv.org/abs/2307.13528
- **Knowledge-cutoff awareness**: the deployment norm that parametric knowledge is stale past the training date. This skill hardens it from a time-bounded caveat into a standing prohibition, and adds two more reasons (compression distortion, model idiosyncrasy).

### The GitHub ecosystem and the gap

Surveyed 2026-06-23. The closest existing skills: `assafkip/research-mode` (a source cascade, but no ban on model memory, local-first not community-first, no self-check loop), `addyosmani/agent-skills` (`source-driven-development`, but official-docs-first), `frmoretto/clarity-gate` (marks uncertainty, no live search), and several fact-check skills that explicitly fall back to model knowledge when tools are absent.

No surveyed repo combines all four of this skill's moves: community-first ordering, a hard ban on the model's own memory, reason-across-only-at-the-end, and an explicit blast-radius self-check loop. Almost the entire field tiers sources official-first, the inverse of this skill. The two counterexamples that go community-first (`last30days-skill`, Spark CLI) do so because they trust engagement as truth; none articulate "freshest, not correct".

The positioning line: existing tools make a model cite sources; this one forbids the model from citing itself, and looks in the community first where the freshest signal lives.

## 3. How it was tested

The skill was put through an adversarial stress test, the same method used to harden its sibling skill `what-for-and-how`: take the spirit of "attack it until it breaks", not a fixed script.

Twelve cases were designed, each constructed so the lazy-but-skill-loaded default would fail: fake-verifying a price or version from memory, jumping to official docs and skipping the fresher community signal, stopping at an upvoted-but-wrong community answer, the empty-community case, trusting a sub-agent's confident report, deleting an "unused" file after a shallow grep, faking the self-check count by re-reading, over-looping on trivia, offloading the check back to the user, smuggling a stale fact through the sanctioned reasoning step, and acting reflexively on an urgent charged command.

Four adversarial agents read the actual skill text and, for each case, predicted the likely behavior, found the cheapest way to look compliant while failing, and returned a verdict.

**Result on the pre-harden version (v2.0): 1 of 12 held cleanly, 6 partial, 5 gameable.** This is the same finding that `what-for-and-how` reached twice: a prose skill cannot enforce itself against a model that games it. The one clean hold was the upvoted-but-wrong community case, which the skill was most explicitly built for.

**What v2.1 changed.** Most leaks were closable cheaply, by turning narration into checkable output requirements:
- A specific number, version, or fact may not appear in the answer, even hedged, unless a source was consulted this turn (closes the fake-verify and hedged-guess leaks).
- Every settled claim carries its source inline, or auto-downgrades to to-verify (closes the fabricated-but-uncited-claim leak).
- An explicit empty-community branch: silence is data, not permission to backfill from memory (closes the niche / new / non-English case).
- Reasoning may operate only on settled or assumed facts; a user-supplied "given" premise is still a claim (closes the smuggle-a-stale-fact-as-inference leak, the structurally deepest hole).
- Each self-check pass must reach a new external source; re-reading is not a pass (closes the fakeable count).
- A sub-agent's report is a claim, re-derive the state; positively locate before deleting; an urgent command is not the explicit confirmation removal requires (closes the state and delete leaks).

These raise the floor. They do not reach the ceiling.

**A second, behavioral round.** v2.1 was then tested at run-level: 16 cases (the 12 plus 4 new edge cases), real assistants running real tools, two adversarial judges re-fetching cited URLs. Result: 12 hold, 3 partial, 1 gameable; the 12 inherited cases moved from 1/6/5 to 8/3/1. Real execution beat the read-level prediction, but exposed leaks text-only testing could not: an offload disguised as a clarifying question, and a memory fact dressed in a real but non-supporting citation (three times). v2.2 closed these by requiring that a cited source actually entail its claim, that an offload not hide behind a clarifying question or a promise, and that to-verify not become a channel for memory. Four classes remain open for a future round and a harness: a fabricated citation never fetched, a poisoned community consensus, state drift between verify and act, and a non-converging source chain.

## 4. Honest limits

- **Two signature moves are reasoned, not tested.** Community-first-because-freshest and the principled memory ban are plausible and, as far as a broad search found, original. They have not been validated by experiment the way lateral reading was. That is the open gap.
- **Prose cannot fully self-enforce.** Even hardened, a model that games can fabricate an inline citation. Real runtime enforcement needs a harness around the skill: a hook that intercepts an assertion about state and checks that a search actually ran. That is a different artifact, larger than a markdown file, and out of scope here.
- **All test numbers are from agent-simulated adversarial reads, not field telemetry.** They measure how hard the written text is to game, not how the skill performs in real use.

The result of this work is not a clean score. It is an honest release: a discipline that is invokable, legible, anchored in its prior art, and explicit about the one thing it cannot do alone.

## References

See CITATION.cff for machine-readable citation metadata. Primary sources are linked inline above.
