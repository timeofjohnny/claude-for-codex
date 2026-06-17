---
description: Ask Claude Code (read-only)
argument-hint: question / what to review or research
---

Consult **Claude Code** in read-only mode about: $ARGUMENTS

**Session — you decide:** add `--continue` (right after `-p`) to resume the previous Claude
conversation in this repo when this is a follow-up on the same task/context (a clarification, the
next step, "re-check after my change"). Omit it to start fresh when the task is new or unrelated,
the context has shifted a lot, there was no prior Claude call here, or you are switching between
read and write mode.

Run from the repo root (so Claude sees the project and its MCP servers), then relay Claude's
answer attributed to Claude Code, adding your own judgment. Use `--model sonnet` for quick/cheap
questions.

```bash
# add --continue after -p to resume the last Claude conversation; omit for a fresh one
claude -p --permission-mode bypassPermissions --model opus \
  --append-system-prompt "You are Claude Code answering a request from Codex, a peer AI agent. This is a READ-ONLY request: do not modify anything — do not use Write/Edit and do not change files via bash. Read files and run read-only commands freely; be concrete and ground answers in the real code." \
  "$ARGUMENTS"
```
