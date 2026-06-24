# Culture-pack rubric (the bar a pack must clear)

This rubric is how the project keeps quality without gatekeeping every pull request by hand. You self-apply it before you open a PR. A CI check (see .github/workflows/) verifies the mechanical items automatically. The judgment items are on your honor, and a maintainer spot-checks packs in batches rather than reviewing each line. That is the deal: the bar is public and fixed, so contribution stays open while the standard stays high.

A pack should not be merged until every item below is true.

## Mechanical (CI checks these)

1. **Frontmatter schema.** The pack has all required fields: `pack`, `name`, `for_engine`, `engine_version`, `language`, `status`, `author`, `license`, `version`, `created`, `provenance`.
2. **Required sections present.** Headings for: terminus map additions, speech-act repertoire, parser signals, provenance, citations. (Clinical display norms is recommended; include it unless it genuinely does not apply.)
3. **Citations exist.** The Citations subsection lists at least one resolvable source URL, and the pack uses `[Cn]` markers in the body.
4. **No em-dash in any non-English prose.** The long dash (U+2014) is banned in non-English text; use a comma, a colon, or a sentence break. (English prose may use it sparingly.)
5. **Examples file exists.** `examples.md` is present in the pack folder.

## Judgment (self-check, batch-spot-checked)

6. **Honest label.** The pack states plainly that it is ONE culture's pack, not the canon.
7. **Internal diversity named.** If the culture is not monolithic (most are not), the pack says so and does not collapse it into a single default reading. Picking a wrong sub-regional reading is a real failure, so the pack must make the variants visible.
8. **No silent transfer.** The pack does not copy another culture's terminus map and relabel it. What it claims is specific to its culture, or it says "shared with the engine default".
9. **Engine untouched.** The pack adds plug-in content. It does not rewrite the mechanism (mode switch, two guards, L6-falsify, the how-bridge). If you think the MECHANISM needs changing, that is an engine PR, not a pack, and it goes through a separate discussion.
10. **Load-bearing claims are sourced.** Every claim the engine would actually act on (a terminus type, a parser rule, a clinical norm) carries a citation to a real source. Claims that are standard-but-unverified are MARKED as such, never asserted as proven.
11. **Provenance is honest.** The provenance section says how the claims were derived and their verification status, distinguishing sourced from unsourced. Overclaiming grounding fails the rubric outright, because this methodology refuses unverified assertion as a matter of principle.
12. **Worked examples earn their place.** At least two or three examples in examples.md, each demonstrating a specific pack signal, not just restating the engine.

## Status ladder

A pack declares its `status` honestly:
- `draft`: incomplete or largely unsourced. Useful as a start; not for production reliance.
- `reference_implementation`: complete, load-bearing claims sourced, honestly labeled. The Vietnamese pack is the model.
- `community_reviewed`: a maintainer or named reviewers have batch-checked it. (This is the only label that implies external review; do not self-apply it.)

Claiming a higher status than the pack has earned is the one failure that erodes the whole commons. Do not do it.
