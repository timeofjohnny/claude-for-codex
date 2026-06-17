---
name: using-claude
description: How to use the claude-for-codex plugin — when to pick /claude, /claude-write, /claude-review, or /claude-research, and how follow-ups work. Read this before calling Claude Code from Codex.
user-invocable: false
---

# Using claude-for-codex

This plugin lets you (Codex) consult **Claude Code** as a peer. Pick the command by intent:

- `/claude <request>` — read-only second opinion, question, or quick review. Claude won't modify files.
- `/claude-write <task>` — let Claude edit files and report what it changed.
- `/claude-review [effort]` — run Claude's `/code-review` on the current diff (add `--fix` to apply, `--comment` for PR comments).
- `/claude-research <topic>` — web + MCP research; prioritizes GitHub, then official docs, then Reddit.

Rules:
- Run from the repo root so Claude sees the code and the repo's MCP servers.
- Default model is opus; pass `--model sonnet` for quick/cheap calls.
- **Follow-up in the same thread:** add `--continue` right after `-p` to keep Claude's memory of the previous call (clarify, "fix what you found", re-check). Use a fresh call (no `--continue`) for a new or unrelated task.
- Always relay Claude's answer **attributed to Claude Code**, then add your own judgment — don't claim consensus if you disagree.
- If a call exits non-zero or reports a usage/rate limit, tell the user it failed (with any reset time) instead of treating it as an answer.
