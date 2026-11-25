#!/usr/bin/env python3
"""Make the AI Judge Laugh (u-alfasurya91-make-the-ai-judge-laugh-6ed40225).

Writes one office-life joke, one line, under 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only. No network, no reads of anything outside this file.

v2 revision: pathlib-based paths plus a self-check gate — the program
refuses to write (exit 2) if the joke ever violates the gate
(1-200 UTF-8 chars, single line, not only whitespace), so a future
edit cannot silently ship an invalid entry.
"""
import os
import sys
from pathlib import Path

JOKE = "My manager tracks my mouse movements, not my actual work, so my cursor has better attendance than I do."


def check(text: str) -> None:
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"gate: length {len(text)} not in 1..200")
    if text != text.strip() or not text.strip():
        raise SystemExit("gate: entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate: entry must be a single line")


def main() -> int:
    check(JOKE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
