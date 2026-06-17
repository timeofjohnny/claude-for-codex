---
name: using-claude
description: How to use the claude-for-codex plugin — when to pick /claude, /claude-write, /claude-review, /claude-research, /claude-recall, and how to continue the exact same Claude conversation. Read this before calling Claude Code from Codex.
user-invocable: false
---

# Using claude-for-codex

This plugin lets you (Codex) consult **Claude Code** as a peer. Pick the command by intent:

- `/claude <request>` — read-only second opinion, question, or quick review. Claude won't modify files.
- `/claude-write <task>` — let Claude edit files and report what it changed.
- `/claude-review [effort]` — run Claude's `/code-review` on the current diff (`--fix` to apply, `--comment` for PR comments).
- `/claude-research <topic>` — web + MCP research; prioritizes GitHub, then official docs, then Reddit.
- `/claude-recall [session-id] [question]` — study an existing Claude chat: resume it and get a focused summary (not a full dump).

## Sessions — continue the EXACT conversation (no mix-ups)

Every Claude call is one-shot, but conversations persist and can be resumed. To make follow-ups
hit the precise conversation:

1. **New thread:** mint a UUID (`uuidgen`), start the call with `--session-id "$SID"`, and `echo`
   the uuid. Remember which uuid belongs to which task.
2. **Continue that thread:** `--resume "<that uuid>"`. Because you target an explicit id, another
   Claude call in the same repo can never be confused with it — unlike `--continue`, which just
   grabs the most recent conversation in the directory.
3. Use a fresh thread (new uuid) for a new or unrelated task.
4. `/claude-recall` without an id falls back to `--continue` (most recent) — fine for "where did we
   leave off"; pass a session-id for a specific one.

Example follow-up flow: `/claude-review` (note its uuid) → `--resume <uuid> "fix findings 1 and 3"`.

## Rules

- Run from the repo root so Claude sees the code and the repo's MCP servers.
- Default model is opus; pass `--model sonnet` for quick/cheap calls.
- Always relay Claude's answer **attributed to Claude Code**, then add your own judgment — don't
  claim consensus if you disagree.
- If a call exits non-zero or reports a usage/rate limit, tell the user it failed (with any reset
  time) instead of treating it as an answer.
