# lch-skills

Behavioral skills for AI assistants, extracted from one person's working habits and hardened until they survive adversarial testing.

A "skill" here is not code. It is prose: a written discipline that changes how an AI assistant behaves before it answers you. Each skill in this repository started as a habit that Le Cong Hoang (LCH) had practiced for years in his own work, was named, written down, stress-tested by adversarial agents, and only then published.

The thesis this repository is built on, and the one its testing keeps confirming: **prose raises the floor, a runtime harness is the ceiling.** A well-written skill reliably lifts an assistant's default behavior. It cannot, by wording alone, close the last gaps that need a checking mechanism at runtime. Every skill here is honest about where that line falls for it.

## What is released

| Skill | What it does | Status | License |
|---|---|---|---|
| [ground-or-abstain](skills/ground-or-abstain) | A verification discipline. Ground every load-bearing claim in a real source consulted this turn, or abstain and say it is unverified. | **Released, v2.3.0** | Apache-2.0 |
| [skill-upgrade](skills/skill-upgrade) | The process that takes a behavioral skill to publish-grade and beyond. Used to harden ground-or-abstain to v2.3.0. | Available, v1.0.0 | Apache-2.0 |
| what-for-and-how | Intent excavation. Drill five layers of "what for" to the real longing before proposing any action. | Planned | TBD |
| luu | A session-close protocol for a personal knowledge vault. | Planned (personal tooling) | TBD |
| verbal-explanation | Turns drafted text into a real human Vietnamese speaking voice. | Not slated for release (personal IP) | All rights reserved |
| lch-partner | The full operating system for working with LCH as a thinking partner. | Not slated for release (personal IP) | All rights reserved |

The first release centers on `ground-or-abstain`, with `skill-upgrade` (the process used to harden it) alongside. The rest are listed so the system is legible as a whole. Two of them (`verbal-explanation`, `lch-partner`) encode a personal voice and a personal portrait and are kept private by design.

## ground-or-abstain in one paragraph

Search the community first, because it is the freshest signal, not because it is correct. Then test the community claim against web and official sources. Never use the model's own training memory as a source: it is stale, compressed, and idiosyncratic. Reason across the gathered sources only at the end. Mark every claim as SETTLED (with its source inline) or STILL TO VERIFY. Run a self-check loop sized to how much damage a wrong answer would do. Verify state before any irreversible action, and never delete what you cannot positively locate. Its origin is the Vietnamese discipline *xac tin*.

It was hardened across three escalating rounds of adversarial testing (read-level, behavioral, and a controlled blind A/B). In the A/B round an assistant carrying the skill scored 9 HOLDS / 1 PARTIAL / 0 GAMEABLE against a plain assistant's 5 / 3 / 2 on the same cases. The skill is invisible on easy cases and decisive under pressure. The two failures that survived are not wording problems; they need a runtime harness, and the skill says so plainly. Full method and numbers are in [skills/ground-or-abstain/METHODOLOGY.md](skills/ground-or-abstain/METHODOLOGY.md) and the test log under that skill's `tests/`.

## How to install a skill

These are [Claude](https://claude.ai) skills. To use one:

- **Claude Code / local:** copy the skill folder (for example `skills/ground-or-abstain/`) into `~/.claude/skills/`. It loads on the next session. The folder name becomes the skill, and its `name` field becomes the slash command.
- **Claude web (claude.ai):** zip the skill folder so the archive contains one folder with `SKILL.md` at its root, then upload it in the skills interface.

Each skill is self-contained: its `SKILL.md` is the skill itself, and the surrounding `README`, `METHODOLOGY`, `CHANGELOG`, `CITATION.cff`, and `tests/` document and defend it.

## Author and license

Created by Le Cong Hoang (LCH), leconghoangstudio@gmail.com.

Released skills are licensed under Apache-2.0 (see [LICENSE](LICENSE)). Skills marked "All rights reserved" in the table above are not covered by that license and are not licensed for reuse.

If you use `ground-or-abstain` in your own work, please cite it using its [CITATION.cff](skills/ground-or-abstain/CITATION.cff).
