---
name: claude-for-codex
description: Ask Claude Code from Codex for anything — a second opinion, a code/architecture review, research, a diff review, or to make and verify a fix. Use when the user asks to consult Claude, Claude Code, another model, a second opinion, an adversarial review, or to have Claude check or fix something. You write the request yourself in --prompt. Read-only by default; --access write lets Claude edit.
---

# Claude for Codex

Call Claude Code from Codex. You write the request in `--prompt`; Claude gets the full toolset.
The script lives next to this skill — invoke it as `python3 scripts/ask_claude.py`. The only knob
is `--access`:

- `read` (default) — Claude reads, searches, runs git/bash, but is told not to modify anything.
- `write` — Claude may edit files. If you want it tested/verified, say so in the prompt.

```bash
# read-only (default model opus; pass --model sonnet for quick/cheap requests)
python3 scripts/ask_claude.py \
  --cwd "<repo-root>" --prompt "Review my staged changes (git diff --staged) for bugs."

# let Claude make a change and verify it
python3 scripts/ask_claude.py \
  --access write --cwd "<repo-root>" \
  --prompt "Fix the failing null check in X, run the tests, and report results."
```

Flags: `--prompt` (required), `--access read|write`, `--model` (default `opus`), `--cwd`
(the repo/folder Claude runs in — also loads that repo's MCP servers from its `.mcp.json`, so
pass it whenever Claude needs the project's code or its MCP access). You decide the task in the
prompt — review, research, answer a question, fix something.

## Reporting

Say the result came from Claude Code, keep its concrete findings and file references, and add
Codex's own judgment separately — don't claim consensus if you disagree.
