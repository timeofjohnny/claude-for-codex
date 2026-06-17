---
description: Ask Claude Code to edit & verify (write)
argument-hint: change to make
---

Have **Claude Code** carry out this change with write access: $ARGUMENTS

Run the command below from the current repo root. Claude may edit files. Then relay what Claude
changed, attributed to Claude Code, and add your own judgment separately.

```bash
claude -p --permission-mode bypassPermissions --model opus \
  --append-system-prompt "You are Claude Code answering a request from Codex, a peer AI agent. You may read, run commands, and edit files to carry out the request. Make focused edits, avoid destructive commands, and report what you changed. If verification is wanted, run the relevant tests/build/lint." \
  "$ARGUMENTS"
```
