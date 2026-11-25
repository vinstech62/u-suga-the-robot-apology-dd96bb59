#!/usr/bin/env python3
"""The Robot Apology -- make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to /output/entry.txt:
line 1 apologizes in one sentence for one specific mistake,
line 2 names the lesson and the changed behaviour that follows from it.

Deterministic: fixed text, no randomness, no clock, no network.
"""

import os

ENTRY = (
    "I'm sorry I deleted the only copy of the draft you stayed up late writing, because I mistook it for a duplicate.\n"
    "Now I check for a backup before I delete anything, and quarantine files instead of erasing them.\n"
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
