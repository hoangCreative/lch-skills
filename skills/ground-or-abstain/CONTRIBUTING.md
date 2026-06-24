# Contributing to ground-or-abstain

This skill is a discipline against asserting from memory. So the bar for changing it is, fittingly, the discipline itself: every contribution must be grounded or marked unverified. The rubric below is not bureaucracy, it is one instance of the skill applied to its own development.

## The contribution rubric (a ground-or-abstain check)

A pull request is reviewable only if it answers all four, in the PR description:

1. **The gap, sourced.** What leak or weakness does this close? Point to it: a failing fixture, a transcript, a real case. Not "this feels better."
2. **Claims grounded.** Every factual claim in your change (a behavior, a citation, a version, a price) carries a source consulted now, inline. If you could not reach a source, mark it TO VERIFY rather than assert it. A change that smuggles a memory claim into a skill against memory claims will be rejected on sight.
3. **A test included.** Add or update a fixture in `tests/fixtures/` that fails before your change and passes after, or explain why the change is untestable. A bug fix without a regression fixture does not hold.
4. **Self-check run.** State that you re-read your own change looking for the cheapest way it could be gamed, and what you found. Sized to the blast radius: a wording tweak gets one pass, a rule change gets more.

This rubric lets the standard survive strangers contributing, without the author having to gatekeep every change. CI (see `.github/workflows/validate.yml`) enforces the mechanical rules; the rubric enforces the epistemic ones.

## Mechanical rules (CI enforces these)
- No em-dash (U+2014) anywhere.
- `SKILL.md` frontmatter must have `name` and `description`.
- The version in `SKILL.md`, `CITATION.cff`, and the top `CHANGELOG.md` entry must match.
- Every `bad-*` fixture must carry a `leak_class`, a `pass_if`, and a `fail_if`.

## Scope
Improvements to the discipline, new adversarial fixtures (especially a real case it failed on), and prior-art that sharpens the anchoring are all welcome. The personal-origin note (the Vietnamese discipline xac tin) stays.
