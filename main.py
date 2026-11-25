#!/usr/bin/env python3
"""Museum of the Year 3000 — the label a museum in the year 3000 places
next to an ordinary object from today.

One object, one line, at most 200 characters. The line is written to
$MAKEFUN_OUTPUT_DIR (or /output) as output.txt.
"""

import os
import sys

LINE = (
    "Group chat, c. 2025. 214 unread messages, none of them read. "
    "Nobody remembers why it was created, and nobody dares to leave it."
)

MAX_CHARS = 200


def main() -> int:
    if len(LINE) > MAX_CHARS:
        print(f"entry is {len(LINE)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    try:
        LINE.encode("ascii")
    except UnicodeEncodeError:
        print("entry must be plain ASCII", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "output.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Verify the written bytes are exactly the line plus one newline.
    with open(out_path, "rb") as f:
        if f.read() != (LINE + "\n").encode("utf-8"):
            print("written output does not match the entry", file=sys.stderr)
            return 1
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
