"""Toaster error line writer.

Emits the single error line a kitchen toaster shows its owner, into the
entry file the scorer reads. Standard library only: no network, no
randomness, no clock, so every run produces the same bytes.
"""

import os
import sys

LINE = "Your toast is ready. You did not come. It is a cracker now. Goodbye."

# The gate allows 1-120 characters on a single line; refuse to emit
# anything outside it rather than hand the scorer an invalid entry.
MIN_CHARS = 1
MAX_CHARS = 120


def check_line(line):
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError("line is %d chars, gate allows %d-%d"
                         % (len(line), MIN_CHARS, MAX_CHARS))
    if "\n" in line or "\r" in line:
        raise ValueError("line must stay on one line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def output_path():
    """Where the entry file goes; the harness overrides it for local runs."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    check_line(LINE)
    path = output_path()
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
