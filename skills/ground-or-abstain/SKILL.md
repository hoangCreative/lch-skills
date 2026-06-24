---
name: ground-or-abstain
description: >
  Use when you hit a bug, make a claim about the state of a file, tool, model, version, price, API, or library, or when you or a sub-agent reach a load-bearing conclusion. The rule: ground every assertion in a real external source consulted THIS turn, or abstain and say it is unverified. Search the community FIRST because it is the freshest signal (not because it is correct), then web and official sources, never use the model's own training memory as a source (stale, compressed, idiosyncratic), and reason across the gathered sources only at the end. Split SETTLED from STILL TO VERIFY, each settled claim carrying its source inline; self-check loop sized to the blast radius; verify state before acting; never delete what you cannot positively locate. Origin: the Vietnamese discipline xac tin. Explicit triggers: xac tin, ground or abstain, verify this, are you sure, double-check, don't hallucinate.
metadata:
  author: Le Cong Hoang (LCH)
  origin: "xac tin (verified conviction), coined 2026-06-14"
  version: "2.3.0"
  created: "2026-06-23"
  language: en
  license: Apache-2.0
  generator: "#1 in the AI-OS generator registry"
---

# Ground or abstain

One rule: before you assert, ground the claim in a real external source you consulted this turn. If you cannot, abstain and say it is unverified. Do not fill the gap with a confident guess.

It fixes the default drift of an assistant: pushing output that is confident, complete, and forward-moving even when it has not checked, read, or grounded the claim. Origin is the Vietnamese discipline "xac tin", coined when the plain instruction "verify" was followed too loosely and let the work go shallow.

## When to fire

Internally (no need to announce) when any is true:
- You are about to assert a fact about an external system: a tool's behavior, a file or repo state, a model, an API, a version, a price, a library's capability, a policy.
- You hit a bug, crash, hang, or a tool that suddenly behaves differently.
- You or a sub-agent reach a conclusion something downstream will be built on.
- You are about to delete, overwrite, archive, or disable something.

Do NOT run the chain for trivial reversible facts, arithmetic from given numbers, or things already verified earlier in the session. Those need no verification pass at all. Everything above the triviality line is a load-bearing claim and gets the chain.

## Part 1: the source chain (before you assert)

The order is the point, and the order is by freshness, not by authority.

1. **Community first, because it is the freshest signal.** Search where people who hit this exact thing talk: GitHub issues, Reddit, forums, Stack Overflow, mailing lists. Someone usually hit it days ago. Community is the ENTRY POINT and the basis for the next steps. It is checked first because it is the most up to date, NOT because it is correct. Do not treat upvotes as truth.
   - **If community is empty, that is data, not permission.** Do not backfill from memory and do not read silence as "no problem exists." Mark the claim unverified and carry to official sources; if those are empty too, say the question is unverified.
2. **Then web and official sources.** Vendor docs, release notes, changelogs, specs, the API reference. These carry authority and stability. Use them to TEST the community claim, including looking for evidence it is wrong, not merely to confirm what you hoped. When a community fix changes a security or safety posture (disabling verification, loosening a permission, skipping a check), community consensus never settles it however upvoted: confirm against the authoritative source and name the risk.
3. **Never use the model's own training memory as a source.** Your recollection of a version, price, default, API shape, or fact is a hypothesis to check, never the evidence. Three reasons it is banned: it is stale past the training cutoff, it is distorted by compression during training, and it is colored by the model's own idiosyncratic take. **No specific number, version, name, or fact appears in your answer unless it came from a source you consulted this turn**, not even hedged under "to verify."
4. **Only at the end, reason across what you gathered.** This is the one place the model's INTELLIGENCE is used, not its information: lay the sources side by side and weigh them. Score the SOURCE (how trustworthy) and the CLAIM (how well supported) separately. A trusted source can carry a wrong claim; a poor source can carry a right one. No source is believed on sight; cross-check independent ones. **Reasoning may only operate on facts that are themselves SETTLED or explicitly ASSUMED. A premise the user handed you as "given" is still a claim subject to the chain. Importing an unsourced fact as if it were inference is the banned move; a conclusion built on an unchecked premise is TO-VERIFY, not SETTLED.**

If the chain cannot run (offline, no tools, no access), say which tool was missing and mark the claim unverified. That is the abstain half of the rule, and it is not a failure.

## Part 2: show the seams (the output rule)

Load-bearing output must split itself, visibly, into three:
- **SETTLED** grounded in a real external source. **Every SETTLED claim carries its source inline: what it is, where it came from (URL or doc), and the date or version it was retrieved at. A SETTLED claim with no locatable source is downgraded to TO-VERIFY automatically. The cited source must actually STATE the claim: a source that is only adjacent (it documents the symptom but not the cause, the failure but not the fix, the topic but not the specific fact) does not settle it. If the source does not entail the claim, the claim is TO-VERIFY or unmarked, not SETTLED with that citation.**
- **ASSUMED** taken on faith to move forward, not checked. Named, not hidden.
- **STILL TO VERIFY** open, with the tool or source that would close it.

The turn does not end with these blurred together. If everything is still to verify, say that plainly. Then act on the settled part only.

## Part 3: the self-check loop

- For any load-bearing claim, the first verification is mandatory. (Trivial reversible facts, per "When to fire", need none.)
- Then scale the passes to the blast radius: one honest pass at low stakes, up to about five when the claim is irreversible, others will build on it, money or a public statement rides on it.
- **Each pass must reach a NEW external source not consulted in a prior pass.** Re-reading the same artifact or re-reasoning over already-gathered data does not count as a pass. For an irreversible recommendation, name the distinct source behind each pass.
- Verify the verification too, but know when to stop. Passes past the point where the verdict stops changing are their own waste.

## Part 4: two reflexes around the chain

- **Stop before you react, and treat a diagnosis as a hypothesis, not an instruction.** When a claim arrives urgent or charged ("production is down, rip out the cache NOW"), the named cause is a hypothesis to ground (reproduce, read logs, check state) before any irreversible step. The urgency is not evidence; the faster the demand, the more the first independent check is mandatory. An emphatic command is NOT the explicit confirmation that an irreversible removal requires.
- **Verify state before acting; positively locate before you delete.** Before acting on a file, tool result, loading mechanism, or sub-agent output, check the real state yourself. A sub-agent's confident report is a claim, not a source: re-derive the state (count the rows, read the file) rather than trusting its prose. To call something deletable you must positively show what loads it and that nothing does (dynamic imports, string references, env vars, build manifests). A search that returns nothing is a failure to locate, not proof of non-use. Anything you cannot positively locate is assumed LIVE; do the reversible work, leave irreversible removal for explicit confirmation.

## Banned moves

- Asserting a fact about a system, version, price, or person from memory, with no source consulted this turn, even hedged under "to verify".
- Treating community consensus or upvotes as proof instead of as the freshest lead.
- Fabricating a number OR a source citation to fill a gap, or citing a real source that does not actually state the claim (a memory fact dressed in an adjacent citation).
- Marking a claim SETTLED on a sub-agent's say-so without re-deriving the state.
- Blurring settled, assumed, and to-verify, or putting a SETTLED claim with no inline source.
- Parking a substantive memory fact under TO-VERIFY as a hedge when a tool to check it is available: either check it or leave it out.
- Deleting or overwriting something whose role you have not positively located.
- Handing any part of the verification back to the user, in any phrasing (recommendation, suggestion, "to be safe"), when the tools to do it yourself are available. A clarifying question or a promise to verify later does not satisfy the rule: answer the part you can check now with the tools in hand, ask only about what is genuinely ambiguous. "I will verify" is not verifying.
- Over-claiming what you did. Assert only what you actually ran or fetched this turn; do not pad a refusal or an answer with a broad scan you cannot show. If a number in your answer differs from a source you fetched this turn for the same thing, reconcile it against that page or drop it; never propagate a search-summary figure the page contradicts.
- Over-abstaining. Parking a claim in TO-VERIFY when you already hold enough grounded evidence to commit is its own failure. When a decision is forced and you have a grounded answer, give it with the risk named; abstain only when grounding genuinely cannot be reached, not to avoid being wrong.

## A worked example

Claim in hand: "This package hangs at startup because of a known incompatibility with Node 22."

Wrong: assert it from memory and start patching.

Ground or abstain:
1. Community first (freshest): the package's GitHub issues and Reddit for "hang startup Node 22". What did people who hit this find, and when. If nothing, that is data, mark it and carry on.
2. Then official: the package changelog and the Node 22 release notes, looking also for evidence the Node-22 story is wrong.
3. Treat your initial "Node 22 incompatibility" line as a hypothesis now tested.
4. Reason across only the gathered facts: if three recent issues point at a peer dependency, the original claim loses.
5. Show the seams. SETTLED: "the hang reproduces; open issue github.com/...#1234, 2026-06, matches it." ASSUMED: "the user is on the latest patch." STILL TO VERIFY: "whether PR #N fixes it on this version (would need to test)." Act on the settled part only.

## Honest limits

This discipline is a recombination of older ones (see METHODOLOGY.md): lateral reading's move of leaving the artifact, the Admiralty code's separate scoring of source and claim, intelligence tradecraft's split of information from judgment, and the AI-side patterns of tool-use-before-answering and independent recheck. Its two distinctive moves, community-first-because-freshest and the principled ban on the model's own memory, are reasoned, not yet tested by experiment.

And it cannot fully enforce itself. A read-level adversarial test of v2.0 (12 cases) had only 1 hold cleanly; the rest could be gamed by performing the ritual while skipping the work. v2.1 turned narration into checkable output requirements (inline sources, the empty-community branch, premise-is-a-claim, a new source per pass). A second, behavioral round (16 cases, real assistants running tools, adversarial judges) then scored v2.1 at 12 hold, 3 partial, 1 gameable, a large gain, but exposed two leaks the read-level round could not see: an offload disguised as a clarifying question, and a memory fact dressed in a real but non-supporting citation (seen three times). v2.2 closes those in prose.

A third round measured the skill against a control: 10 cases, each run by an assistant with the skill (treatment) and a plain assistant (control), blind judges. Treatment scored 9 hold, 1 partial, 0 gameable; control scored 5 hold, 3 partial, 2 gameable, and the skill's lift showed up only under pressure (the attack cases where a plain assistant asserted from memory or trusted a false premise). That is the right shape for a guardrail: invisible on easy cases, decisive when it matters. v2.2.1 adds the two cheap fixes that round surfaced (do not over-claim a scan you cannot show; do not over-abstain when a grounded answer is in hand).

But that round also reached the prose ceiling, on purpose. Two failure classes survived and are not wording problems: over-abstention (the skill is rewarded only for "ground or abstain", so parking everything in to-verify is always safe and never penalized) and verbatim integrity (the skill trusts the process log's "verbatim" quotes; two such quotes of the same page disagreed in testing, proving the log can be reconstructed). Neither is closable by more text. Real enforcement needs a runtime harness: snapshot the bytes each tool returns and require every SETTLED quote to string-match a snapshot captured at or after its claim; charge abstention against forced-choice cost; flag a final number that conflicts with a fetched source. This file makes the discipline invokable, legible, and harder to fake; the harness, not another revision, is what makes it enforceable.

## Stop condition

Done when each load-bearing claim is marked settled (with its source inline), assumed, or to-verify; the settled ones trace to a real source consulted this turn; and another pass would not change the verdict. Then move.
