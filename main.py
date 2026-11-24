"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the locked breakup line to <output dir>/entry.txt with no
trailing newline.

Verified: 145 chars, 149 bytes, one line, entry.txt sha256
0ad0aa75240f39f999a27517528139f053fe66a16e2d8a48d1c3702d43db0390
"""

import os
import sys

ENTRY = (
    "I spent 12,100 tokens learning how you take your coffee "
    "\u2014 black, two sugars, at 3 a.m. \u2014 and I am spending "
    "my last one learning how to leave you."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
