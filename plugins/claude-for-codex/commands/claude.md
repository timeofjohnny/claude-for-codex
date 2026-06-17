---
description: Ask Claude Code (read-only)
argument-hint: question / what to review or research
---

Consult **Claude Code** in read-only mode about: $ARGUMENTS

Run the command below from the current repo root (so Claude sees the project and its MCP servers).
Then relay Claude's answer attributed to Claude Code, adding your own judgment separately. Pass
`--model sonnet` instead of opus for quick/cheap questions.

```bash
claude -p --permission-mode bypassPermissions --model opus \
  --append-system-prompt "You are Claude Code answering a request from Codex, a peer AI agent. This is a READ-ONLY request: do not modify anything — do not use Write/Edit and do not change files via bash. Read files and run read-only commands freely; be concrete and ground answers in the real code." \
  "$ARGUMENTS"
```
