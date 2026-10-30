#!/usr/bin/env python3
"""Count common severity labels in a text log file."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

LEVELS = ("CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG")


def analyze(path: Path) -> Counter[str]:
    counts: Counter[str] = Counter()
    with path.open("r", encoding="utf-8", errors="replace") as log_file:
        for line in log_file:
            upper_line = line.upper()
            for level in LEVELS:
                if level in upper_line:
                    counts[level] += 1
                    break
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log_file", type=Path)
    args = parser.parse_args()
    path = args.log_file.expanduser().resolve()

    if not path.is_file():
        parser.error(f"Log file not found: {path}")

    try:
        counts = analyze(path)
    except OSError as exc:
        parser.error(str(exc))

    print(f"Log summary: {path.name}")
    for level in LEVELS:
        print(f"{level:8} {counts[level]}")
    print(f"TOTAL    {sum(counts.values())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
