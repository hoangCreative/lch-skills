---
pack: your-culture-slug
name: Your culture-pack (human-readable)
for_engine: what-for-and-how
engine_version: ">=3.1.0"
language: xx
variety: optional, e.g. African American English, Scots, Jamaican Patois (a pack MAY scope to a variety/register/continuum, not only a national language)
status: draft
author: Your Name
license: Apache-2.0
version: 0.1.0
created: YYYY-MM-DD
provenance: one line on how this pack's claims were derived, and their verification status
---

# <Culture> culture-pack

> Replace this blockquote. State plainly that this is ONE culture's pack, not the canon. If the culture is not monolithic (most are not), say so here and commit to not collapsing it into one default reading.

This pack supplies what the engine plugs in: extra TERMINUS types, a SPEECH-ACT repertoire, language-specific PARSER SIGNALS, and CLINICAL display norms. It never changes the mechanism.

---

## 1. Triggers (added to the engine)

- Explicit-invocation phrases in your language that should show the full cascade.
- Auto-trigger surface forms (the engine already fires on decision/why shape; list the local phrasings).

---

## 2. Terminus map additions (your culture's floors)

The engine ships the relational/role terminus as a universal principle. Name WHICH roles, duties, honors, or continuities count as legitimate floors in your culture, and how they are signaled. Each entry: a name, a one-line gloss, an example utterance, and a citation [Cn]. Forcing these into individual-need language distorts them, so say what the correct read is.

- **<Floor name>.** <gloss>. Example: "<utterance>". [Cn]
- ...

If a floor is a brute social fact (an address rule, a status asymmetry), mark it as such.

---

## 3. Speech-act repertoire (your language)

Acts that do not map onto a Western verb shape, or that the engine's ACTION-shape cascade can misread. For each: what it is, and how the engine should read it instead.

- **<Act>.** <what it is>. Read as <STATE / relational / etc.>, not as a goal-directed action. [Cn]
- ...

---

## 4. Parser signals (your language)

Language-specific signals the engine's parser should use when this pack is loaded.

- **Subject handling.** Does your language drop the agent (topic-comment, pro-drop)? State the rule so the engine does not force a subject. [Cn]
- **Stance / modal markers.** Particles, inflections, or constructions that carry commitment or hedge, which must flow into the terminus rather than be dropped. [Cn]
- **Sarcasm / prosody.** What sarcasm signals does your language carry in speech that vanish in text? Declare the blind spot. [Cn]
- **Register / code-switch.** What social meaning do register or dialect shifts carry? [Cn]

---

## 5. Clinical display norms (feeds the Clinical Brake)

How is distress expressed or masked in your culture? The engine warns against using surface emotional intensity as a proxy for risk; make that concrete here. [Cn]

---

## 6. Worked examples

Put at least two or three worked cases in examples.md in this folder, each showing one pack signal at work on top of the engine mechanism.

---

## 7. Provenance and verification status (required, read honestly)

State how this pack's claims were derived and their verification status. Distinguish:
- Claims that carry a citation [Cn] and a real, resolvable source (load-bearing claims).
- Claims that are standard but not individually verified (mark them; do not assert them as proven).

Do not overclaim grounding. This methodology refuses meaningless action and unverified assertion; a pack that overstated its evidence would violate the method it ships.

### Citations
- [C1] <claim it supports>: <url(s)>
- [C2] ...

---

## 8. How to read this pack with the engine

A short numbered list: when to load this pack, which sections feed which engine stage, and a reminder that the mechanism (mode switch, two guards, L6-falsify, the how-bridge) is unchanged.
