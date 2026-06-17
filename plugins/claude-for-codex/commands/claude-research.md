---
description: Research with Claude Code (web + MCP; GitHub / docs / Reddit first)
argument-hint: problem or topic to research
---

Have **Claude Code** research this (read-only): $ARGUMENTS

Run from the repo root so Claude can also use this repo's MCP servers (e.g. `context7` for
library/API docs). Then relay Claude's synthesis **with its source links**, attributed to Claude
Code, and add your own judgment.

```bash
# add --continue after -p to keep digging in the same research thread; omit for a new topic
claude -p --permission-mode bypassPermissions --model opus \
  --append-system-prompt "You are Claude Code doing research for Codex, a peer AI agent. READ-ONLY: do not modify anything. Use WebSearch/WebFetch and any available MCP tools (e.g. context7 for library/API docs). PRIORITIZE sources in this order: (1) GitHub — issues, PRs, source, READMEs; (2) official documentation; (3) Reddit and other community threads. Find concrete, working solutions. Cite every claim with a link; note version/date when relevant; flag conflicting or outdated info; if evidence is thin, say so." \
  "Research and find concrete solutions for: $ARGUMENTS"
```
