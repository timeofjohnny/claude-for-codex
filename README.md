# claude-for-codex

A [Codex](https://github.com/openai/codex) plugin that calls **Claude Code** as a peer — for a
second opinion, a code/architecture review, research, a diff review, or to make and verify a fix.

It adds two slash commands:

| Command | Mode | Use for |
|---|---|---|
| `/claude <request>` | read-only | second opinion, review, research — Claude won't modify anything |
| `/claude-write <request>` | write | let Claude edit files (and verify) |
| `/claude-review [effort]` | read-only | run Claude Code's `/code-review` on the current diff (add `--fix` to apply) |

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
```

## Requirements

The [Claude Code](https://claude.com/claude-code) CLI (`claude`) must be installed and
authenticated on the machine running Codex.
