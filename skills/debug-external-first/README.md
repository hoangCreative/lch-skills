# debug-external-first

A debugging-reflex skill for AI assistants. When something breaks or behaves unexpectedly, especially in a third-party tool, package, API, or model, the first move is to search the community (GitHub issues, changelog, Reddit) for whoever already hit it, NOT to guess a cause from memory or iterate locally.

Most mystery bugs in third-party code are external-state changes (a model retired, an endpoint moved, an API deprecated). The broken state is not local, so local iteration can never find it. A plausible guess from training memory feels like progress and is worse than no move, because it sends you debugging the wrong layer.

This is the debugging-time sibling of `ground-or-abstain`: same root rule (never assert from training memory, ground in a real source consulted now), applied to the moment a bug appears.

## Install

Copy this folder into `~/.claude/skills/`. It loads on the next session, and the `name` field (`debug-external-first`) becomes the trigger.

## Origin

Distilled from two real incidents: a media MCP server that hung for ten-plus hours because it hard-coded a model the provider had retired, and a scheduled task whose cause was guessed wrong four times before a community search found two known closed bug reports. Author: Le Cong Hoang (LCH), leconghoangstudio@gmail.com.
