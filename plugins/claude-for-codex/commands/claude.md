---
description: Ask Claude Code (read-only)
argument-hint: question / what to review or research
---

Consult **Claude Code** in read-only mode about: $ARGUMENTS

**Session (zero chance of resuming the wrong chat):** for a NEW thread, mint a UUID and start with
`--session-id` (echo it so you can reuse it). To CONTINUE that exact thread later, use
`--resume <that uuid>` — it targets the precise conversation, never "most recent". Track which uuid
belongs to which task. (See the `using-claude` skill.)

Run from the repo root. Show the user Claude's `result` attributed to Claude Code, add your own
judgment. Use `--model sonnet` for quick/cheap calls. If the call exits non-zero or reports a
usage/rate limit, report the failure instead of treating it as an answer.

```bash
SID=$(uuidgen)   # reuse this uuid to continue this exact thread
echo "claude session: $SID"
claude -p --session-id "$SID" --permission-mode bypassPermissions --model opus \
  --append-system-prompt "You are Claude Code answering a request from Codex, a peer AI agent. This is a READ-ONLY request: do not modify anything — do not use Write/Edit and do not change files via bash. Read files and run read-only commands freely; be concrete and ground answers in the real code." \
  "$ARGUMENTS"
# continue this thread later: claude -p --resume "<the uuid above>" --permission-mode bypassPermissions --model opus "<follow-up>"
```
