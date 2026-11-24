#!/usr/bin/env python3
"""Write one original one-line cat joke to /output/entry.txt.

Deterministic, stdlib only, no network, no randomness, no timestamps.
"""

import os

JOKE = (
    "My cat ignores the $40 bed I bought her and sleeps in the box it "
    "came in — the most honest product review I've ever received."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
