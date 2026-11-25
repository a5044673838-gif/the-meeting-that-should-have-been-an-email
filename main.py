#!/usr/bin/env python3
"""Write one joke about a meeting that should have been an email.

The entry is a single line of plain text, at most 200 characters, written
to /output/entry.txt. Standard library only, no network, deterministic.
"""

import os

LINE = (
    "We spent an hour deciding the meeting should have been an email, "
    "then booked another meeting to discuss the email."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Round-trip check: what landed on disk must be exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE + "\n", "round-trip mismatch"
    print(f"Wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
