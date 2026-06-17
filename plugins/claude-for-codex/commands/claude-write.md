---
description: Ask Claude Code to edit & verify (write)
argument-hint: change to make
---

Have **Claude Code** carry out this change with write access: $ARGUMENTS

**Session — you decide:** add `--continue` (right after `-p`) to resume the previous Claude
conversation in this repo when this continues the same task (e.g. "now also do X", "fix the issue
you just found"). Omit it to start fresh when the task is new or unrelated, the context has shifted
a lot, there was no prior Claude call here, or the previous call was read-only.

Run from the repo root. Claude may edit files. Then relay what Claude changed, attributed to Claude
Code, and add your own judgment separately.

```bash
# add --continue after -p to resume the last Claude conversation; omit for a fresh one
claude -p --permission-mode bypassPermissions --model opus \
  --append-system-prompt "You are Claude Code answering a request from Codex, a peer AI agent. You may read, run commands, and edit files to carry out the request. Make focused edits, avoid destructive commands, and report what you changed. If verification is wanted, run the relevant tests/build/lint." \
  "$ARGUMENTS"
```
