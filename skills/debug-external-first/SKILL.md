---
name: debug-external-first
version: "1.0.0"
description: >
  Use when you hit a bug, a hang, or any unexpected behavior, especially in a third-party tool, package, API, model, or service. The rule: before debugging from your own assumptions or iterating locally, search the community FIRST (GitHub issues open and closed, the changelog or release notes, then Reddit and forums) for whoever already hit it. Most mystery bugs in third-party code are external-state changes (a model retired, an endpoint moved, an API deprecated) that no amount of local iteration can find, because the broken state is not local. Never present a cause guessed from training memory as a finding, and never bounce verification back to the user when you hold the tools to check. Explicit triggers: debug-external-first, why is this breaking, it hangs, it stopped working, unexpected behavior, tra cong dong truoc.
metadata:
  author: Le Cong Hoang (LCH)
  copyright: "© 2026 Le Cong Hoang"
  created: "2026-06-23"
  origin: a debugging discipline learned from a 10-hour external-state incident
---

# debug-external-first

The rule: when something breaks or behaves unexpectedly, your FIRST move is to find out whether the world already knows about it, not to start guessing or iterating. Search the community before you debug.

## Why this exists (the cost of getting it wrong)

Two real incidents, both expensive:

- A media MCP server hung forever at startup. Ten-plus hours went into trying other versions, other configs, rewriting the server. The actual cause: the provider had retired the exact model the server hard-coded, months earlier. Five minutes reading the project's issues would have shown it. Local iteration could never converge, because the broken state was not local, it sat on the provider's side.
- A scheduled task kept failing with "socket connection closed." The cause was guessed four times from general knowledge, each one wrong (including a Linux fix proposed for a macOS machine), each costing a round of the user's time and trust. The real answer was two known, already-closed bug reports in the vendor's own tracker, found the moment someone actually searched.

The pattern in both: a plausible guess from memory feels like progress and is worse than no move at all, because it sends you debugging the wrong layer.

## When this fires

- A third-party package, server, or tool hangs at startup or on one specific call.
- Something that worked stopped working with no change on your side.
- A tool talks to an external API, model, or service (provider model names, endpoints, auth, quotas).
- You are about to say "it's probably X" about a bug, from memory.
- The user opens with a problem or an error.

## The protocol (the order is the whole point)

1. **A guess is a hypothesis, never a finding.** Do not produce a diagnosis from training memory and present it as the cause.
2. **Search the community FIRST**, with a time budget of about 10 minutes: GitHub issues (open AND closed), the project's changelog or release notes, then Reddit and forums. Look for who already hit this, the confirmed root cause, and how they fixed it.
3. **If the package talks to an external API, check external state as step one:** is the model, endpoint, or version it targets still alive? A retired model or moved endpoint is the single most common invisible cause.
4. **Reason from the evidence already in hand.** Read the logs or screenshot the user gave and derive from them yourself. Do not make the user fetch more or verify on your behalf when you can check it.
5. **Only after you hold evidence, state the cause with its source** (an issue link, a changelog line, or an observation you drew), separating what is settled from what still needs checking. Then debug locally against that hypothesis.

## Banned moves

- Guessing a cause from memory and stating it as the cause.
- Iterating locally (try another version, another config, rewrite it) before you have a researched hypothesis, when the symptom points at external state.
- Applying a fix from the wrong platform or version (a Linux answer on a macOS machine) without checking it matches the user's actual setup.
- Bouncing the check back to the user ("can you confirm X?") when you hold the tools to check it yourself.
- Stacking speculative layers of cause on top of evidence you do not have.

## When NOT to over-apply

This is for bugs in code or tools you did not just write, and for external-state symptoms. A typo or a logic error in code you wrote this session is yours to read and fix directly; do not go searching the community for your own fresh mistake. The discipline is community-FIRST, not community-ONLY: once you have the lay of the land, local debugging is exactly the right next move.

## Sibling

This is the debugging-time form of `ground-or-abstain`: the same root rule (do not assert from training memory, ground in a real source consulted now), applied at the moment a bug appears instead of the moment a claim is made. Where ground-or-abstain governs what you assert, this governs what you do first when something breaks.
