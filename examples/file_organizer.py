#!/usr/bin/env python3
"""Organize files into folders by extension. Dry-run is the default."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "images": {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"},
    "documents": {".pdf", ".doc", ".docx", ".odt", ".txt", ".md"},
    "spreadsheets": {".csv", ".xls", ".xlsx", ".ods"},
    "archives": {".zip", ".7z", ".rar", ".tar", ".gz"},
    "audio": {".mp3", ".wav", ".ogg", ".flac"},
    "video": {".mp4", ".mkv", ".mov", ".avi"},
}


def category_for(path: Path) -> str:
    suffix = path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if suffix in extensions:
            return category
    return "other"


def unique_destination(path: Path) -> Path:
    """Avoid overwriting an existing file by adding a numeric suffix."""
    if not path.exists():
        return path
    counter = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def organize(source: Path, apply: bool = False) -> list[tuple[Path, Path]]:
    if not source.exists() or not source.is_dir():
        raise ValueError(f"Source directory does not exist: {source}")

    planned: list[tuple[Path, Path]] = []
    for item in sorted(source.iterdir()):
        if not item.is_file():
            continue
        destination_dir = source / category_for(item)
        destination = unique_destination(destination_dir / item.name)
        planned.append((item, destination))
        if apply:
            destination_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(destination))
    return planned


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="Directory whose files should be organized")
    parser.add_argument("--apply", action="store_true", help="Perform moves (default: preview only)")
    args = parser.parse_args()

    try:
        moves = organize(args.directory.expanduser().resolve(), apply=args.apply)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    if not moves:
        print("No files found to organize.")
        return 0

    for source, destination in moves:
        action = "MOVE" if args.apply else "WOULD MOVE"
        print(f"{action}: {source.name} -> {destination.relative_to(args.directory.resolve())}")

    if not args.apply:
        print("\nPreview only. Add --apply to perform these moves.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
