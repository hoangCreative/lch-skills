# Changelog

## [1.0.0] - 2026-06-23

First release. Distilled from two real incidents (a media MCP server that hung ten-plus hours on a retired hard-coded model; a scheduled task misdiagnosed four times before a community search found the real closed bug reports).

- The rule: search the community FIRST when something breaks, before guessing from memory or iterating locally.
- A five-step protocol (guess is a hypothesis not a finding; community search with a ~10 minute budget; check external API state first; reason from evidence in hand; state cause with its source, then debug locally).
- Banned moves (guess-as-cause, premature local iteration, wrong-platform fixes, bouncing the check to the user, speculative cause-stacking).
- A "when NOT to over-apply" boundary (your own fresh code is yours to read, not a community search).
- Cross-referenced as the debugging-time sibling of `ground-or-abstain`.
