---
description: Ask Claude Code to edit & verify (write)
argument-hint: change to make
---

Have **Claude Code** carry out this change with write access: $ARGUMENTS

**Session (zero chance of resuming the wrong chat):** for a NEW thread, mint a UUID and start with
`--session-id` (echo it so you can reuse it). To CONTINUE that exact thread later (e.g. "now also do
X", "fix the issue you just found"), use `--resume <that uuid>` — targets the precise conversation,
never "most recent". (See the `using-claude` skill.)

Run from the repo root. Claude may edit files. Relay what Claude changed, attributed to Claude Code,
and add your own judgment. If the call exits non-zero or reports a usage/rate limit, report the
failure instead of treating it as an answer.

```bash
SID=$(uuidgen)   # reuse this uuid to continue this exact thread
echo "claude session: $SID"
claude -p --session-id "$SID" --permission-mode bypassPermissions --model opus \
  --append-system-prompt "You are Claude Code answering a request from Codex, a peer AI agent. You may read, run commands, and edit files to carry out the request. Make focused edits, avoid destructive commands, and report what you changed." \
  "$ARGUMENTS"
# continue this thread later: claude -p --resume "<the uuid above>" --permission-mode bypassPermissions --model opus "<follow-up>"
```
