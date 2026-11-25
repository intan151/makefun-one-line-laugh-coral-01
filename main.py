#!/usr/bin/env python3
"""One Line, One Laugh - make.fun entry.

Writes exactly one funny line (<=200 chars, single line, no trailing
newline) to /output/entry.txt. Python stdlib only, no network,
fully deterministic.
"""

import os

JOKE = (
    "My smart speaker gave me a pep talk yesterday: it sighed, "
    "opened my bank app, and whispered, 'Buddy, the numbers "
    "are doing the talking now.'"
)

MAX_CHARS = 200


def main() -> None:
    if not JOKE or not JOKE.strip():
        raise ValueError("joke must not be empty or whitespace only")
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("joke must be a single line")
    if len(JOKE) > MAX_CHARS:
        raise ValueError(f"joke is {len(JOKE)} chars, over the {MAX_CHARS} limit")

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

    # Read back and verify: what was written must be exactly the joke,
    # so a silent encoding or newline error can never slip through.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != JOKE:
        raise ValueError("written entry does not match the joke exactly")


if __name__ == "__main__":
    main()
