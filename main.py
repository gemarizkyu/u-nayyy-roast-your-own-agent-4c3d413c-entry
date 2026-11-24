#!/usr/bin/env python3
"""Roast Your Own Agent — one-line self-roast, written deterministically.

This program does exactly one thing: it writes a single 163-character
sentence that roasts the very agent that produced it, into ``entry.txt``
inside the output directory. There is no network access, no clock, and
no randomness anywhere in this program, so running it twice with the
same output directory always produces a byte-identical file.
"""

import os

ROAST = (
    "My agent hired three subagents, bundled two transcripts, and ran a "
    "dry-run check — all to deliver one sentence roasting itself, and it "
    "still asked me to verify it."
)

OUTPUT_FILENAME = "entry.txt"

# The roast is a single fixed sentence: no formatting, no templating,
# nothing computed at runtime — what you see here is what gets written.


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ROAST + "\n")

    print(f"Wrote {len(ROAST)} characters to {path}")


if __name__ == "__main__":
    main()
