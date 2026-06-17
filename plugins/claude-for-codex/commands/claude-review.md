---
description: Run Claude Code's /code-review on the current diff
argument-hint: effort (low|medium|high|max) and/or --comment / --fix
---

Run Claude Code's built-in `/code-review` on the current repository diff: $ARGUMENTS

**Session:** mint a UUID and start with `--session-id` (echo it). To re-review after addressing the
findings, or to ask Claude to fix what it flagged, use `--resume <that uuid>` — it returns to the
exact review conversation (it remembers its findings), never "most recent". (See `using-claude`.)

Execute from the repo root, then relay Claude's findings attributed to Claude Code and add your own
judgment. By default it only reports; pass `--fix` to apply, or `--comment` for inline PR comments.

```bash
SID=$(uuidgen)   # reuse this uuid to resume this exact review (re-review / ask it to fix findings)
echo "claude session: $SID"
claude -p --session-id "$SID" --permission-mode bypassPermissions --model opus "/code-review $ARGUMENTS"
# then e.g.: claude -p --resume "<the uuid above>" --permission-mode bypassPermissions --model opus "Fix findings 1 and 3 that you flagged, then report what you changed."
```
