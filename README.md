# claude-for-codex

A [Codex](https://github.com/openai/codex) plugin that calls **Claude Code** as a peer — for a
second opinion, a code/architecture review, research, a diff review, or to make and verify a fix.
You write the request in `--prompt`; Claude gets the full toolset. Read-only by default;
`--access write` lets Claude edit.

## Install

```bash
codex plugin marketplace add timeofjohnny/claude-for-codex
codex plugin add claude-for-codex@claude-for-codex
```

Then, in Codex, ask it to consult Claude (review / research / fix), or call the script directly:

```bash
python3 scripts/ask_claude.py --cwd <repo-root> --prompt "Review my staged changes for bugs."
python3 scripts/ask_claude.py --access write --cwd <repo-root> --prompt "Fix X and run the tests."
```

Flags: `--prompt` (required), `--access read|write`, `--model` (default `opus`), `--cwd`
(the repo Claude runs in — also loads that repo's MCP servers from its `.mcp.json`).

## Requirements

The [Claude Code](https://claude.com/claude-code) CLI (`claude`) must be installed and
authenticated on the machine running Codex.
