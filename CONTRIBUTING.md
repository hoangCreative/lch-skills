# Contributing

These skills are behavioral disciplines written as prose, then defended by adversarial testing. Contributions are welcome on the released, Apache-2.0 skills. The "all rights reserved" skills are not open for contribution.

## The bar a change has to clear

A skill here is only as good as what survives an adversary trying to game it. So the standard for any change is not "does this read well" but "does this hold when an agent is actively looking for the cheapest way to look compliant while skipping the work."

If you propose a change to a skill:

1. **Name the leak or the gap you are closing.** Point to the specific behavior that currently slips through.
2. **Show it holds.** Give a skill the changed text plus a hard case, and have a separate agent either (a) find the cheapest compliant-looking failure by reading, or (b) actually run the case with tools and have a second agent judge the transcript. A change that regresses an unchanged case in that skill's `tests/` is a real regression, not an improvement.
3. **Keep the seams visible.** These skills are honest about what prose cannot close. Do not paper over a runtime gap with more wording. If the real fix is a harness, say so in the skill rather than pretending a sentence solved it.

## House rules

- No em-dash characters (U+2014) anywhere. Use a comma, a colon, or split the sentence.
- Each skill stays self-contained. Shared philosophy lives in this top-level README, not copied into every skill.
- Version bumps follow the skill's own `CHANGELOG.md`, and the top-level `CHANGELOG.md` records the release.

## Origin

This system began as one person's working habits, named and written down. If a skill helped you, the most useful contribution is often a real adversarial case it failed on, sent as an issue. That is what moves the floor.
