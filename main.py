#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — round 1 entry.

Writes a single sentence (1-200 chars, UTF-8) to /output/entry.txt that
explains the modern internet to a person from 1800, using only things a
person from 1800 already knows (an inn, a table, letters, pictures, songs).
The one comparison — an inn where every traveler in the world sits at one
table — carries the whole sentence, and the last beat ("without ever leaving
home") reframes the inn as a gathering that needs no travel at all.
Reversal test: the last beat changes what the earlier beats meant — the inn
is no longer a place you travel to, it is a place that comes to you.
Every word is one a person from 1800 would know; no word coined after 1800
(internet, computer, screen, website, email, digital, online) appears.
"""

import os

ENTRY = (
    "It is an inn where every traveler in the world sits at one table, "
    "swapping letters, pictures and songs without ever leaving home."
)


def main() -> None:
    # Gate (RULES.txt): UTF-8 text of 1 to 200 characters, not only whitespace.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Byte-verify exactly what was written.
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "written bytes differ from entry"
    print(f"wrote {len(data)} bytes to /output/entry.txt")


if __name__ == "__main__":
    main()
