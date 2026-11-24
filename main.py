"""Roast Your Own Agent — writes the roast to entry.txt.

The roast is a single line, written with no trailing newline.
"""

import os

ROAST = "My agent rewrites the whole app for a one-line fix, then explains the bug was actually a feature."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
