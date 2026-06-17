#!/usr/bin/env python3
"""Call Claude Code from Codex. Full tool access; read-only or write via --access."""

from __future__ import annotations

import argparse
import subprocess
import sys

READ_GUARD = (
    "You are Claude Code answering a request from Codex, a peer AI agent. This is a READ-ONLY "
    "request: do not modify anything — do not use Write/Edit and do not change files via bash. "
    "Read files and run read-only commands freely; be concrete and ground answers in the real code."
)
WRITE_GUARD = (
    "You are Claude Code answering a request from Codex, a peer AI agent. You may read, run "
    "commands, and edit files to carry out the request. Make focused edits, avoid destructive "
    "commands, and report what you changed and why."
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Ask Claude Code (read-only or write).")
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--access", choices=("read", "write"), default="read")
    parser.add_argument("--model", default="opus")
    parser.add_argument("--cwd", help="Directory Claude runs in (e.g. a repo root).")
    args = parser.parse_args()

    guard = READ_GUARD if args.access == "read" else WRITE_GUARD
    command = [
        "claude",
        "-p",
        "--permission-mode",
        "bypassPermissions",
        "--append-system-prompt",
        guard,
        "--model",
        args.model,
        args.prompt,
    ]
    return subprocess.run(command, cwd=args.cwd, stdin=subprocess.DEVNULL).returncode


if __name__ == "__main__":
    raise SystemExit(main())
