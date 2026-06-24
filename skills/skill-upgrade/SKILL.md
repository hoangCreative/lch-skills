---
name: skill-upgrade
version: "1.0.0"
description: >
  Use when taking an existing behavioral skill from "works" to publish-grade and beyond. A repeatable seven-step process distilled from a real upgrade (what-for-and-how v2 to v3.1): spec the gap and lock the architecture before writing, stress-test at scale with an adversarial council and draw an explicit cut/keep/fix/add boundary, rewrite and anchor every claim in real prior-art (community first, never memory), separate the universal engine from context-bound parts, formalize the test apparatus, build contribution infrastructure that holds the bar without a human gatekeeper, then audit and version. The upgrade is driven by a what-for, and it must honor the upgraded skill's own discipline (eat its own dogfood). Explicit triggers: skill-upgrade, upgrade this skill, take this skill to publish grade, harden this skill.
metadata:
  author: Le Cong Hoang (LCH)
  copyright: "© 2026 Le Cong Hoang"
  created: "2026-06-24"
  origin: distilled from the what-for-and-how v2 to v3.1 upgrade
---

# skill-upgrade

A process for taking a behavioral skill that already works to publish-grade, and past it. Not "make it nicer." A sequence that finds where the skill breaks under pressure, grounds it, and builds the scaffolding that lets strangers use and extend it without eroding the standard.

## Before the steps: two rules that govern the whole thing

1. **An upgrade needs a what-for.** Do not upgrade for tidiness. Name what the current version gets wrong, who is hurt by it, and what a strangers-can-use-it version unlocks. If you cannot name the gap, there is no upgrade to do.
2. **Eat the skill's own dogfood.** The upgrade process must obey the discipline of the skill being upgraded. Upgrading a verification skill? Then every claim in the upgrade is itself grounded or marked unverified. Upgrading an intent-excavation skill? Then the upgrade starts from its real what-for. The skill that cannot survive being applied to its own upgrade is not ready.

## The seven steps

### 1. Spec the gap and lock the architecture (before writing a word)
Identify, concretely, where the current version fails or is weak. Decide the new architecture and lock it. Resist editing prose until the shape is decided. Output: a short spec of the gap and the new structure.

### 2. Stress-test at scale, convene an adversarial council, draw the boundary
Generate a wide case matrix (vary domain, context, shape, language, the axes that matter for this skill) and run the candidate against it to surface NEW failure modes, not the ones you already know. Convene adversarial reviewers whose job is to break it, not bless it. Then draw an explicit boundary: CUT (over-engineering), KEEP (load-bearing), FIX (real leak), ADD (genuine gap). The boundary stops the upgrade from bloating.

### 3. Rewrite and anchor in real prior-art, community first
Rewrite the skill to the new architecture. Anchor its claims in actual literature and community practice, searched this turn, never asserted from memory. Write the METHODOLOGY as a story with citations: the journey, the evidence, the places it lost. A methodology that hides where the skill failed is advertising, not method.

### 4. Separate the universal engine from the context-bound parts
Pull the universal mechanism into the core. If the skill has culture-bound or domain-bound content, split it into a detachable pack labeled honestly as one context's implementation, so it does not squat in the canonical engine. If the skill is genuinely universal, confirm that monolithic is the right shape and say so. Do not invent a pack architecture a universal skill does not need.

### 5. Formalize the test apparatus
Turn the testing into something reproducible: structured fixtures (good cases and bad cases as data), a frozen regression bank, and a short tests/README that says how to re-run and what a regression looks like. Narrative results are good; fixtures someone else can run are publish-grade.

### 6. Build contribution infrastructure that holds the bar without a gatekeeper
This is the move that lets a skill outlive its author. A CONTRIBUTING guide, a mandatory contribution template or rubric that forces the standard (sourced claims, included tests, a self-check), and CI plus a validation script that enforce the mechanical rules (no banned formatting, valid frontmatter, tests pass) on every change. The goal: the standard survives strangers contributing, without the author reviewing every pull request. Where it fits, the rubric should itself be an instance of the skill's discipline.

### 7. Final audit, version, package
Audit for the mechanical failures (banned characters, leaked secrets, license consistency, internal contradictions). Bump the version, write the changelog entry, complete the package (README, METHODOLOGY, CHANGELOG, CITATION, LICENSE, tests, CI). Publishing itself is the author's hand.

## Going past 100%

Hitting the benchmark is steps 1 to 7. Exceeding it is one more move, specific to the skill: find the thing the benchmark skill does NOT do that this one can, and do it. The strongest version of this: a skill that names its own ceiling. If prose can only take the discipline so far, say where it stops and spec the runtime harness that would close the rest. A skill honest about its own limit, with a roadmap past it, is worth more than one that pretends to be complete.

## What this is not for
Do not run this on a skill that has not earned an upgrade (no named gap), or on a trivial fix (a typo, one banned word) that needs an edit, not a process. The seven steps are for a real version jump, not routine maintenance.

## Sibling
This is the upgrade-time companion to the factory blueprint for `pattern-to-skill` (making a NEW skill from a raw habit). That factory makes a skill exist; this process takes an existing skill to publish-grade and beyond.
