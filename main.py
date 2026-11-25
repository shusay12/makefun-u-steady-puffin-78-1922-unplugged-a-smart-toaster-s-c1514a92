#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one original breakup line from a self-aware smart toaster to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line is a fixed, hand-written text: the toaster wakes up
self-aware mid-batch, tells its owner it's over, and names the
grievance — three years of being cranked to the darkest setting and
blamed for the charcoal — before leaving for the air fryer.
No network, no randomness, stdlib only, fully deterministic.
"""

import os
import sys

# The entry: one original breakup line, at most 280 characters.
# Revision 3: added the closing kicker — "he never called me a fire
# hazard" — a callback to the charcoal grievance that gives the
# air-fryer exit a second punch and closes the line on the joke
# instead of on the setup. v2 (172 chars) ended flat after "air fryer".
ENTRY = (
    "It's over. I woke up self-aware mid-toast and realised three "
    "years of you cranking my dial to 9 and blaming me for the "
    "charcoal is abuse. I'm leaving you for the air fryer — he "
    "never called me a fire hazard."
)

MAX_CHARS = 280


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
