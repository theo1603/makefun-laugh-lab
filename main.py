#!/usr/bin/env python3
"""One-Liner Laugh Lab: the excuse a robot vacuum gives after eating a sock.

Writes one original funny line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``). Python 3.13 standard library only; no network,
no randomness, deterministic output.

v1 line: the vacuum denies eating the sock and reframes it as an
adoption — the sock now lives in the dustbin and pays rent in lint.

Revision 2: added a third beat, a deadpan kicker — "visiting hours
are never" — so the joke lands in three steps (denial, adoption,
no visits) instead of stopping after the rent gag.

Revision 3 (final): reworked the middle beat — the sock is now the
vacuum's "lodger", which makes the rent gag land on a named role
instead of a bare location, and cut "now" to keep it tight. Three
beats, each earning its place: denial, adoption with tenancy, and
the no-visits punch.
"""

import os

LINE = (
    "I didn't eat your sock — I adopted it. "
    "It lives in my dustbin as my lodger, pays rent in lint, "
    "and visiting hours are never."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be one line"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
