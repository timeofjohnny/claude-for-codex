---
description: Recall an existing Claude Code chat (resume & summarize, not a full dump)
argument-hint: "[session-id] optional specific question"
---

Study an EXISTING Claude Code conversation and report what matters — do NOT dump the whole transcript.

- If a session UUID is present in the arguments, resume that one: `--resume <uuid>`.
- Otherwise resume the most recent conversation in this repo: `--continue`.

The resumed session loads the full chat into Claude (it manages the size itself); ask Claude for a
BOUNDED, focused summary. Default focus: recent decisions, current state, open questions, next steps
— the END of the conversation, not a replay. If the arguments include a specific question, have
Claude answer it from the conversation. Relay the summary attributed to Claude Code.

```bash
# specific conversation by id:
claude -p --resume <session-id> --permission-mode bypassPermissions --model opus \
  "Summarize where this Claude Code conversation left off: the most recent decisions, current state, open questions, and next steps. Be concise and focus on the end — do not replay the whole history. If the following is a specific question, answer it from the conversation instead: $ARGUMENTS"

# or the most recent conversation in this repo — replace `--resume <session-id>` with `--continue`
```

To find session ids: they are the conversation UUIDs (e.g. filenames under Claude's project session
store), or run `claude --resume` interactively to see the picker.
