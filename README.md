# claude-for-codex

A [Codex](https://github.com/openai/codex) plugin that calls **Claude Code** as a peer — for a
second opinion, a code/architecture review, research, a diff review, or to make and verify a fix.

It adds two slash commands:

| Command | Mode | Use for |
|---|---|---|
| `/claude <request>` | read-only | second opinion, question, or quick review — Claude won't modify anything |
| `/claude-write <request>` | write | let Claude edit files (and verify) |
| `/claude-review [effort]` | read-only | run Claude Code's `/code-review` on the current diff (add `--fix` to apply) |
| `/claude-research <topic>` | read-only | web + MCP research; prioritizes GitHub, docs, then Reddit |
| `/claude-recall [id] [q]` | read-only | resume an existing Claude chat and get a focused summary |

Follow-ups continue the **exact** conversation: each thread gets a UUID (`--session-id`), resumed
later with `--resume <uuid>` — so chats can't be confused with one another.

Claude gets the full toolset; read-only is enforced by its system prompt. Run the commands from
the repo you're working in so Claude sees the code and its MCP servers.

## Install

```bash
codex plugin marketplace add timeofjohnny/claude-for-codex
codex plugin add claude-for-codex@claude-for-codex
```

## Examples

```
/claude review my staged changes (git diff --staged) for bugs
/claude is this migration plan sound? <plan>
/claude-write fix the failing null check in X, then run the tests
/claude-review high
/claude-research how to fix <error> with <library> — check GitHub issues and docs
```

## Requirements

The [Claude Code](https://claude.com/claude-code) CLI (`claude`) must be installed and
authenticated on the machine running Codex.
