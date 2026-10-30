#!/usr/bin/env python3
"""Check whether a TCP endpoint accepts a connection.

The default address uses TEST-NET-1 (192.0.2.0/24), reserved for documentation.
Pass a real host explicitly when testing an environment you are authorized to access.
"""

from __future__ import annotations

import argparse
import socket


def check(host: str, port: int, timeout: float) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (OSError, TimeoutError):
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="192.0.2.10", help="Target host (default is a documentation-only IP)")
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--timeout", type=float, default=3.0)
    args = parser.parse_args()

    if not 1 <= args.port <= 65535:
        parser.error("Port must be between 1 and 65535.")
    if args.timeout <= 0:
        parser.error("Timeout must be greater than zero.")

    if check(args.host, args.port, args.timeout):
        print(f"OK: {args.host}:{args.port} accepts TCP connections.")
        return 0

    print(f"UNAVAILABLE: could not connect to {args.host}:{args.port}.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
