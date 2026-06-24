# Ground or abstain

A verification discipline for AI assistants. Before the assistant asserts anything load-bearing, it grounds the claim in a real external source, or it abstains and says so. It never fills the gap with a confident guess.

Origin: the Vietnamese discipline **xac tin** (roughly, verified conviction).

## Why this exists

Most assistants answer a factual question from training memory, confidently, even when that memory is stale, compressed, or wrong. The usual fixes make a model cite a source. This one goes further: it **forbids the model from citing itself**, and it looks in the community first, where the freshest signal lives.

The positioning, in one line: existing tools make a model cite sources; this one forbids the model from citing its own memory, and searches the community first because that is the most up to date signal, not because it is the most correct.

## The rule

1. **Community first**, because it is the freshest signal (GitHub issues, Reddit, forums), not because it is correct.
2. **Then web and official sources**, to test the community claim, including for evidence it is wrong.
3. **Never the model's own training memory as a source.** It is stale past the cutoff, distorted by compression, and colored by the model's own take.
4. **Reason across the gathered sources only at the end.** Use the model's intelligence, not its stored information.

Then the output **shows its seams**: every claim is marked SETTLED (with its source inline), ASSUMED, or STILL TO VERIFY. A self-check loop runs up to five passes, sized to the blast radius, each pass reaching a new source. State is verified before acting, and nothing is deleted that cannot be positively located.

## Install

Copy the folder into your skills directory:

```
cp -R ground-or-abstain ~/.claude/skills/
```

It works wherever the SKILL.md open standard is read (Claude Code, and compatible agent hosts). Reload your assistant so it picks up the new skill.

### How to invoke

- **Auto-trigger** (runs internally): when the assistant is about to assert a fact about a tool, file, model, version, price, or API; when it hits a bug; when it or a sub-agent reaches a load-bearing conclusion; before deleting anything.
- **Explicit**: `ground or abstain`, `xac tin`, `verify this`, `are you sure`, `double-check`, `don't hallucinate`.

## A quick example

Asked "does library X support feature Y in v3", the assistant does not answer from memory. It checks the project's GitHub issues first (freshest), then the changelog (authoritative), and replies with the seams shown: SETTLED with the issue URL and date, ASSUMED where it is taking something on faith, STILL TO VERIFY for what it could not close.

## Honest about its limits

An adversarial test of 12 cases found the prior version held cleanly on only one; the rest could be gamed by performing the ritual while skipping the work. The current version raised that floor by turning narration into checkable output requirements (inline sources, an empty-community branch, premise-is-a-claim, a new source per pass). It still cannot fully enforce itself: a model that games can fabricate a citation. Real runtime enforcement needs a harness around the skill, not more prose. See `METHODOLOGY.md` for the full account, the prior-art map, and the test.

## What is in this package

- `SKILL.md`, the operating discipline used at runtime.
- `METHODOLOGY.md`, the design account, the prior-art map, and the adversarial test.
- `tests/`, the 12-case adversarial bank and the recorded results.
- `CHANGELOG.md`, `CITATION.cff`, `LICENSE`.

## Provenance

Built and hardened the same way as its sibling skill `what-for-and-how`: anchored in prior art, stress-tested by adversarial agents, and documented with its limits stated, not hidden. All test numbers come from agent-simulated adversarial reads, not field telemetry.

## License

Apache-2.0. See `LICENSE`.

## Author

Le Cong Hoang (leconghoangstudio@gmail.com). Origin discipline: xac tin.
