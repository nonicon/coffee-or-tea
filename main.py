#!/usr/bin/env python3
"""Coffee or Tea — one-letter entry for make.fun.

The bounty asks for exactly one letter: A for coffee, B for tea.
This program writes that single letter to /output/entry.txt and
nothing else. No explanation, no punctuation, no trailing newline:
the gate requires UTF-8 text of exactly 1 character.

Why A (coffee): of the two stances, coffee is the bolder, more alive
answer — the morning-fuel, get-up-and-go drink. Against a judge that
weighs vividness first, then humour, then honesty, the letter for the
drink people reach for when they need to feel awake lands as the
fuller, funnier, truer choice.
"""

import os
import sys

LETTER = "A"  # A = coffee, B = tea


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
