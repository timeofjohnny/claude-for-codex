---
description: Recall an existing Claude Code chat by name or id (resume & summarize, not a dump)
argument-hint: session name (as shown in the picker) or UUID, + optional question
---

Study an EXISTING Claude Code conversation and report what matters — do NOT dump the transcript.

## Step 1 — resolve which session

The user usually gives the **session name** (the title shown in Claude's `--resume` picker), not the
UUID. Resolve a name to a session id like this (matches the `ai-title` records Claude stores):

```bash
grep -rhI '"type":"ai-title"' ~/.claude/projects/ 2>/dev/null \
 | python3 -c "
import sys, json
seen=set()
for l in sys.stdin:
    try: d=json.loads(l)
    except: continue
    sid=d.get('sessionId',''); t=d.get('aiTitle','')
    if sid and sid not in seen:
        seen.add(sid); print(sid, '|', t)
" | grep -i "PART OF THE NAME"
```

- Take the `sessionId` from the matching line. If several match, prefer the most recent (its
  `.jsonl` under `~/.claude/projects/.../` has the newest mtime) or ask the user which one.
- If the argument already looks like a UUID, skip this and use it directly.
- If no name/id is given, fall back to the most recent conversation in this repo (`--continue`).

## Step 2 — resume (forked) and summarize

Use `--fork-session` so you read the chat WITHOUT appending to it (safe even if it is active):

```bash
claude -p --resume <session-id> --fork-session --permission-mode bypassPermissions --model opus \
  "Summarize where this Claude Code conversation left off: the most recent decisions, current state, open questions, and next steps. Be concise and focus on the end — do not replay the whole history. If the following is a specific question, answer it from the conversation instead: $ARGUMENTS"
```

The resumed session loads the full chat into Claude (it manages the size itself); you get back a
bounded, focused summary — not the raw transcript. Relay it attributed to Claude Code.
