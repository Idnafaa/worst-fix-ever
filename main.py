#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — entry writer.

The entry is one commit message line (at most 100 characters) about a
bug fix that made everything worse. This program writes that line to
/output/entry.txt, exactly as the judge will read it.
"""
import os

COMMIT_MESSAGE = (
    "fix: speed up login by skipping the password check "
    "- logins are instant now, and so is the breach"
)

# The fix must read as a commit subject: a "fix:" prefix, one line, and
# the punchline has to land inside the same line, not after it.
OUTPUT_PATH = "/output/entry.txt"


def main():
    line = COMMIT_MESSAGE.strip()
    if not line.startswith("fix:"):
        raise SystemExit("commit message must start with 'fix:'")
    if not 1 <= len(line) <= 100:
        raise SystemExit(f"commit message is {len(line)} chars, must be 1-100")
    if "\n" in line:
        raise SystemExit("commit message must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
