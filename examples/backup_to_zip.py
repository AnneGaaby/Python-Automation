#!/usr/bin/env python3
"""Create a timestamped ZIP archive from a directory."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def create_backup(source: Path, destination_dir: Path) -> Path:
    if not source.is_dir():
        raise ValueError(f"Source directory does not exist: {source}")
    if source == destination_dir or source in destination_dir.parents:
        raise ValueError("Destination must not be inside the source directory.")

    destination_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_path = destination_dir / f"{source.name}_backup_{timestamp}.zip"

    with ZipFile(archive_path, "w", compression=ZIP_DEFLATED) as archive:
        for item in source.rglob("*"):
            if item.is_file():
                archive.write(item, item.relative_to(source.parent))
    return archive_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--destination", type=Path, default=Path("backups"))
    args = parser.parse_args()

    source = args.source.expanduser().resolve()
    destination = args.destination.expanduser().resolve()
    try:
        archive = create_backup(source, destination)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(f"Backup created: {archive}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
