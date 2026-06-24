# Contributing to What For and How

> Cam on ban ghe qua. Day la mot skill phuong phap luan voi mot engine universal va cac culture-pack thao roi. Dong gop duoc hoan nghenh, dac biet la mot pack cho nen van hoa cua ban. (A Vietnamese-language community and the reference pack live in packs/vietnamese.)

This project has a deliberate shape: a small, culture-light **engine** that holds the mechanism, and **culture-packs** that supply what is not universal. That shape decides how you contribute.

## Two kinds of contribution

### 1. Add a culture-pack (the main invitation)

The engine was built honestly, but it cannot know your culture's terminus map, speech acts, or parser signals. You can. This is the contribution the project is built to receive.

1. Copy `packs/_template/` to `packs/<your-culture-slug>/`.
2. Fill in `PACK.md` (the template walks you through every section) and write a few worked cases in `examples.md`.
3. Cite your load-bearing claims. Every terminus type, parser rule, or clinical norm the engine would actually act on needs a real, resolvable source. Mark anything standard-but-unverified as such; do not assert it as proven.
4. Self-apply the rubric in `packs/_template/PACK.rubric.md`.
5. Run the validator locally: `python3 scripts/validate_packs.py`. Fix anything it flags.
6. Open a pull request describing the culture, your sources, and the pack's honest `status`.

You do not need to be an academic. You need to be honest about what you know, what you sourced, and what you are still unsure of. The rubric and the validator carry the rest.

### 2. Improve the engine

Typos, clearer wording, a sharper worked example, a real bug in the mechanism. For anything that changes how the engine WORKS (a new guard, a new terminus type, a parser change), open an issue to discuss first. Engine changes affect every pack, so they move slower and need more eyes. A change that is really about one culture belongs in that culture's pack, not the engine.

## How quality is kept (the deal)

There is no per-PR gatekeeper holding up your work. Instead:

- **CI checks the mechanical items** of the rubric automatically (frontmatter schema, required sections, citations present, no em-dash in non-English prose, examples file present). See `.github/workflows/validate-pack.yml`.
- **You self-apply the judgment items** (honest label, internal diversity named, no silent transfer of another culture's map, load-bearing claims sourced, honest provenance).
- **A maintainer batch-spot-checks** packs rather than reviewing every line, and may promote a pack's `status` to `community_reviewed`.

This is the lean model on purpose: the bar is public and fixed, so contribution stays open while the standard stays high. The one thing that breaks the commons is claiming a higher `status` than your pack has earned. Do not do that.

## Contribution workflow

1. Fork the repo to your account.
2. Branch off main, named for the work (for example `pack/japanese` or `fix/parser-typo`).
3. Keep each pull request focused on one thing.
4. For a pack, run `python3 scripts/validate_packs.py` before you push.
5. Open a pull request with a short description of what you changed and why.

## Commit conventions

Write commit messages as `<type>: <short description>`. Common types:

- `pack:` add or update a culture-pack
- `fix:` bug fixes (typos, logic, broken links)
- `feat:` new engine content (a guard, a mode, an example), discussed first
- `docs:` documentation edits (README, this file, CITATION)
- `refactor:` reorganization without changing the content
- `chore:` housekeeping (metadata, formatting)

Keep the description present-tense, short, and to the point. Example: `pack: add japanese culture-pack (terminus + keigo speech acts)`.

## A note on prose voice

Non-English prose in this repo (including packs) **must not use the em-dash** (U+2014, the long dash). Use a comma, a colon, or a separate sentence. This keeps the prose reading like a real person speaking rather than machine output, and the CI enforces it for non-English packs. English prose may use the em-dash sparingly.

## Code of Conduct (condensed)

This repo adopts a condensed Contributor Covenant. In short:

- Treat everyone with respect, even when you disagree.
- Keep feedback on the content, not the person.
- No harassment, no discrimination, no demeaning language.
- When you receive feedback, take the valid point, fix it, and move on; do not get defensive.

Report violations to the maintainer via the GitHub profile **@hoangCreative**. Reports are handled discreetly and seriously.

---

*By Le Cong Hoang. Licensed under Apache-2.0.*
