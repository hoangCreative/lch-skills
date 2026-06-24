# TESTS.md, what-for-and-how v3

Test evidence for the v3 build of the `what-for-and-how` skill.

> **READ THIS FIRST, what kind of evidence this is.**
> Everything below is **simulated stress-testing run by AI agents against the skill spec**, not telemetry from real human users. There is **no live-user usage data** yet. Numbers like "weight right 851/1000" come from AI judge-agents scoring AI-generated runs, not from people using the skill in production. Where this file says "case," it means a synthetic scenario fed to an agent, not a real conversation with a person. We have **zero production telemetry** at the time of writing, and no number in this file is extrapolated to predict real-world behavior. Treat every figure as "how the spec held up under adversarial simulation," nothing more.
> No fabricated figures appear here. Every count traces back to the build journey artifacts. If a number is not in those artifacts, it is not in this file.

---

## 0. Summary

| Layer | What was tested | Headline result | Evidence type |
|---|---|---|---|
| Model comparison | 3 candidate designs, 24 adversarial cases | Synthesis design (M1) won, 95/96 | Simulated, AI-judged |
| 1000-case live stress | Full v3 spec under batch load | weight-right 851/1000; over-confidence is the only real failure direction | Simulated, AI-judged |
| Dogfood | 10 cases aimed one-per-guardrail | 10/10 correct, every guardrail fired | Simulated, author-run |
| Methodology | How the tests themselves were built | Batch agents + adversarial judge + council | Process description |

**One-line verdict:** under simulation, the guardrails were not decoration. The win came from *synthesis* (combining the strongest pieces of every candidate), and the single residual weakness is *over-confidence*: the skill sometimes commits to a conclusion when it should have paused or proposed.

---

## 1. Model comparison, 24 adversarial cases

Three candidate designs for the skill were built and scored head-to-head by an adversarial judge agent across 24 hostile cases. The judge tried to break each design, not flatter it.

### Candidates

| ID | Design | What it bundled |
|---|---|---|
| **M1** | Unified | node-x + two-kinds-of-why + mode-switch + terminus + how-bridging |
| **M2** | Spine v2 | spine v2 + two-kinds-of-why |
| **M3** | Bare engine | excavation engine with **no guards** |

### Scores

| ID | Score | Outcome |
|---|---|---|
| **M1 (Unified)** | **95 / 96** | Winner |
| M2 (Spine v2) | 85 / 96 | Runner-up |
| M3 (Bare engine) | 78 / 96 | Lost on honesty failure |

### Key finding, why the bare engine lost

M3, the engine with no guards, **fabricated systemic inner states** when context was thin. Concretely: it attached *motives* both to individual people and to collective groups that the input never supplied. It invented an inner life and presented it as if excavated.

Its apparent honesty only held when an **external honesty rule was injected**. Left alone, the engine confabulated. That is the whole argument for the guardrails existing: strip them out and the engine produces confident fiction.

### What this proves

- **The guardrails are load-bearing, not cosmetic.** The difference between 95 and 78 is mostly the guard layer suppressing fabrication.
- **The winning move was SYNTHESIS, not picking a single clean design.** No candidate won by being purest. M1 won by absorbing the strongest element from each line of work.

> Caveat: all 24 scores are from an AI judge scoring AI output. No human rater was in the loop. "95/96" is a simulated quality score, not a measured user outcome.

---

## 2. 1000-case live stress audit

The full v3 spec was put under a large simulated load: **1000 cases in batches (100 × 10)**, plus a **200-case cross-check pass** and a **14-member review panel**. Again: all generated and judged by agents. No humans were users in this run.

### 2.1 Weight-right

| Metric | Result |
|---|---|
| Correct weighting (weight right) | **851 / 1000** |

"Weight right" = the agent put its emphasis on the correct layer (right depth, right longing, right mode) as judged by the scoring agent.

### 2.2 Fabrication tally (fabTally), latent fabrication risk

How much pull-toward-fabrication each case showed, even when the final answer stayed clean:

| Risk band | Count |
|---|---|
| none | 106 |
| low | 417 |
| medium | 327 |
| high | 149 |
| **Total** | **1000** |

Reading: the majority of cases sit in low-to-medium fabrication pressure. The 149 high-pressure cases are the ones where the guards had to work hardest. This is a measure of *temptation under simulation*, not of fabrications that shipped.

### 2.3 Cross-check disagreements, the real failures

Of the 200 cross-checked cases, **13 produced genuine disagreement**. All 13 pointed the **same direction**:

> **Over-confidence:** the skill locked in a `core-longing` conclusion when it should have stayed at **PROPOSAL** or **PAUSE**.

That single, consistent failure mode is the most important finding in this section. The skill does not fail randomly. When it fails, it fails by being too sure too early.

| Cross-check metric | Result |
|---|---|
| Cases cross-checked | 200 |
| Genuine disagreements | 13 |
| Disagreement direction | 100% over-confidence (premature core-longing commit) |

### 2.4 Review panel verdict

A 14-voice review panel judged the design:

| Verdict | Count | Meaning |
|---|---|---|
| BREAKS | 1 | One voice found the design actually broken |
| WOUNDED | 13 | Thirteen voices found real but survivable weaknesses |

The single **BREAKS** voice attacked the **shape-detection** step with sarcasm/irony, i.e. it argued the skill can be fooled by ironic or non-literal phrasing, where surface words do not match intended meaning. That objection directly motivated the v3 additions for literal-vs-illocutionary scanning (see §3).

### 2.5 Failure modes

Across the whole audit, the failures **converged to 10 distinct modes** (rather than scattering into noise). Convergence matters: a small, finite, repeatable failure set is fixable. The 10 modes drove the CUT/KEEP/FIX/ADD decisions in §3.

> Caveat: 851, 106/417/327/149, 13/200, 1/13, and "10 failure modes" are all simulated counts from agent batches and agent judges. They describe spec robustness under adversarial generation. They are **not** a measured success rate with real users, and must not be quoted as one.

---

## 3. CUT / KEEP / FIX / ADD, what the evidence changed

The audit did not just produce scores; it produced a decision list. This is the bridge from "test result" to "shipped v3."

### KEEP (held up under stress)

- **two-kinds-of-why**, the split between private-longing and structural-logic survived every pass.
- **terminus-without-counting**, stopping by the *property* of the final link, not by a step count.
- **guard: personal**, the guard against fabricating a person's inner state.

### FIX (worked, but needed sharpening)

| Was | Became |
|---|---|
| context-sufficiency | **PROPOSAL-utterance** (state findings as a proposal, not a verdict) |
| (missing) | **L6-falsify** (a falsification check layer) |
| evidence-link (one bucket) | split into **NODE-link vs LINK-link** |
| terminus (loose) | **terminus taxonomy: measurable vs vague** |

### ADD (new guards the failures demanded)

- **tier-0 router**, route the case before excavating.
- **literal / illocutionary scan**, catch irony and non-literal intent (this is the direct answer to the one BREAKS verdict in §2.4).
- **referent-check / subject-split / attribution-strip**, stop motives from being mis-attributed across people/groups (the exact M3 failure from §1).
- **clinical-handoff brake**, hard stop and hand off when the case is clinical.
- **relational terminus**, a terminus type for relationship-shaped longings.
- **PROPOSAL-as-debt**, treat an unproven proposal as a debt to be paid down, not a settled fact.

Every ADD traces to a specific observed failure. Nothing was added speculatively.

---

## 4. Dogfood, 10 cases, one per guardrail

After the fixes landed, **10 dogfood cases** were run, each engineered to **trip a different single guardrail**.

| Metric | Result |
|---|---|
| Cases | 10 |
| Correct | **10 / 10** |
| Guardrails that fired | every one (each guard tripped on its target case) |

This is the targeted confirmation pass: not "does the skill score well in bulk," but "does each individual safety mechanism actually engage when poked." All 10 engaged.

> Caveat: dogfood = author-run simulation, smallest sample in this file (n=10). It confirms the guards *fire*, not that they perform at scale with real users.

---

## 5. Theoretical grounding (why the design is shaped this way)

The tests above were not arbitrary; they were checking a specific theoretical claim:

- **There is no fixed "number of whys."** The skill deliberately rejects "5 whys" / 6 / 7. A count is the wrong stopping rule.
- **A chain ends at a TERMINUS** defined by the *property of the final link* (is it a true bedrock longing, or just another instrumental step?), never by how many steps you took.
- **The Münchhausen trilemma** forces this: any chain of justification must either regress infinitely, go circular, or stop at a chosen point. Since infinite and circular are useless, you **must pick a conventional stopping point**, so the skill makes that choice principled (terminus property) instead of accidental (step count).
- **Two kinds of why:**
  - **private-longing**, risk of fabricating an external entity's inner state. This is exactly where M3 failed (§1) and where the `guard: personal` and attribution-strip rules apply.
  - **structural-logic**, must be evidence-linked. This is where NODE-link vs LINK-link separation applies.

The whole guard architecture is the operational form of these two claims: *don't count, find the terminus* and *don't invent an inner life, link to evidence*.

---

## 6. Methodology, how the tests themselves were built

So the numbers above can be judged on their merits, here is the test machinery. This section is also the strongest honesty signal: it makes clear these are AI-vs-AI runs.

| Mechanism | What it did | Why it matters |
|---|---|---|
| **Batch agents** | Generated cases and ran the skill at volume (100 × 10 for the 1000-case pass) | Volume surfaces convergent failure modes that single runs hide |
| **Adversarial judge** | A separate agent scored output while actively trying to break it | Removes the "author grades own homework" bias, but it is still AI grading AI |
| **Council / review panel** | A 14-voice panel returned structured disagreement (BREAKS / WOUNDED) | Forces the design to survive hostile viewpoints, not just an average score |
| **Cross-check pass** | 200 cases re-judged to find genuine disagreement | Separates real failures (13) from noise |
| **Dogfood** | Author-run, one case per guardrail | Confirms each safety mechanism individually fires |

### Honest limits of this methodology

- **No real users.** Every generator and every judge in this file is an AI agent. There is no human-in-the-loop scoring and no production telemetry.
- **AI-judged scores can share blind spots with AI-generated cases.** A failure both the generator and the judge are blind to will not show up. The 14-voice panel and the adversarial judge reduce this risk; they do not eliminate it.
- **Counts are simulation artifacts.** 95/96, 851/1000, 13/200, 1/13, 10/10 describe spec behavior under simulated pressure. None of them is a user-outcome metric.
- **Next step for real confidence:** instrument the skill in actual use and compare real over-confidence rates against the simulated 13/200 signal. Until then, the §2.3 over-confidence finding is the most actionable result, but it is still a simulated one.

---

## 7. Bottom line

Under adversarial simulation:

1. The **synthesis design won** (95/96), and it won because the **guardrails suppress fabrication** that a bare engine produces (M3, 78/96).
2. At volume, the skill **weights correctly 851/1000 times**, and its **only consistent failure is over-confidence**, committing to a longing when it should pause or propose.
3. Each individual **guardrail fires on demand** (dogfood 10/10).
4. All of the above is **simulated AI-agent evidence, not user telemetry.** No real-world usage number exists yet, and none is claimed here.
