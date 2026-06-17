---
description: Research with Claude Code (web + MCP; GitHub / docs / Reddit first)
argument-hint: problem or topic to research
---

Have **Claude Code** research this (read-only): $ARGUMENTS

**Session:** for a NEW research thread, mint a UUID and start with `--session-id` (echo it). To keep
digging in that exact thread, use `--resume <that uuid>` — never "most recent". (See `using-claude`.)

Run from the repo root so Claude can also use this repo's MCP servers (e.g. `context7` for
library/API docs). Relay Claude's synthesis **with its source links**, attributed to Claude Code,
and add your own judgment. If the call exits non-zero or reports a usage/rate limit, report it.

```bash
SID=$(uuidgen)   # reuse this uuid to keep digging in this exact thread
echo "claude session: $SID"
claude -p --session-id "$SID" --permission-mode bypassPermissions --model opus \
  --append-system-prompt "You are Claude Code doing research for Codex, a peer AI agent. READ-ONLY: do not modify anything. Use WebSearch/WebFetch and any available MCP tools (e.g. context7 for library/API docs). PRIORITIZE sources in this order: (1) GitHub — issues, PRs, source, READMEs; (2) official documentation; (3) Reddit and other community threads. Find concrete, working solutions. Cite every claim with a link; note version/date when relevant; flag conflicting or outdated info; if evidence is thin, say so." \
  "Research and find concrete solutions for: $ARGUMENTS"
# keep digging later: claude -p --resume "<the uuid above>" --permission-mode bypassPermissions --model opus "<follow-up>"
```
