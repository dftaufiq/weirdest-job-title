#!/usr/bin/env python3
"""Weirdest Job Title entry (make.fun program/v1).

Writes a single job title -- 60 characters or fewer and nothing else --
to /output/entry.txt, where the grader reads it.

The title was picked by pairwise comparison of five candidates against the
judge's brief (RULES.txt): a real-sounding job (taste tester) with one
hilariously specific twist (night shift, expired, airline pretzels), and
nothing in the field like it -- no apologizer, mourner, grief-counselor,
penguin or goldfish cliché. See leaderboard-top10.md for the analysis.
"""

import os
import sys

TITLE = "Night-Shift Taste Tester for Expired Airline Pretzels"
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 60


def main() -> int:
    # The gate refuses anything outside 1..60 UTF-8 chars or blank-only text.
    # Fail loudly here rather than shipping an invalid entry.
    if not (1 <= len(TITLE) <= MAX_CHARS):
        print(f"title is {len(TITLE)} chars, must be 1..{MAX_CHARS}", file=sys.stderr)
        return 1
    if not TITLE.strip():
        print("title is blank", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
