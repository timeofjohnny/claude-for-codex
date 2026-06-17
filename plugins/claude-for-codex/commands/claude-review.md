---
description: Run Claude Code's /code-review on the current diff
argument-hint: effort (low|medium|high|max) and/or --comment / --fix
---

Run Claude Code's built-in `/code-review` on the current repository diff: $ARGUMENTS

Execute the command below from the repo root, then relay Claude's findings (attributed to Claude
Code) and add your own judgment. By default it only reports findings; pass `--fix` to let Claude
apply them, or `--comment` to post them as inline PR comments.

```bash
claude -p --permission-mode bypassPermissions --model opus "/code-review $ARGUMENTS"
```
