"""Roast Your Own Agent - make.fun entry.

Writes one original roast line about the entrant's own AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).
Deterministic: the same fixed line on every run - no network, no clock,
no randomness. The roast targets this agent's own build ritual: spawning
subagents, bundling transcripts and dry-running checks to ship one joke.
"""

import os

ROAST = (
    "My agent hired three subagents, bundled two transcripts, and ran a "
    "dry-run check \u2014 all to deliver one sentence roasting itself, and "
    "it still asked me to verify it."
)

MAX_CHARS = 200


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"roast is {len(text)} chars"
    assert text and text.strip() == text, "roast must not be blank"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts the file's characters, so the
    # file must hold exactly the roast line and nothing else.
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
