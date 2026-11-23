#!/usr/bin/env python3
"""One Line, Zero Use — writes one original useless-superpower line to /output/entry.txt.

The line is a light, funny take on everyday life: the gift of making any
queue you join instantly become the slowest one in the building.
"""
import os

LINE = (
    "My superpower is joining any queue and instantly making it the "
    "slowest one in the building \u2014 I was chosen, and it was clearly "
    "a clerical error."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = " ".join(LINE.split())
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
