#!/usr/bin/env python3
"""Print disk usage for a path using only the Python standard library."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def human_bytes(value: int) -> str:
    size = float(value)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024 or unit == "TB":
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()
    path = args.path.expanduser().resolve()

    if not path.exists():
        parser.error(f"Path does not exist: {path}")

    usage = shutil.disk_usage(path)
    used_percent = usage.used / usage.total * 100 if usage.total else 0

    print(f"Path:      {path}")
    print(f"Total:     {human_bytes(usage.total)}")
    print(f"Used:      {human_bytes(usage.used)} ({used_percent:.1f}%)")
    print(f"Free:      {human_bytes(usage.free)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
