#!/usr/bin/env python3
"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

Writes a single sentence to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt) that would convince a friend who has
never coded to let an AI agent build their first app idea on make.fun.
Deterministic: same run, same bytes. Stdlib only, no network.
"""

import os

ENTRY = (
    # One sentence, 143 characters. The only other full stop is inside
    # "make.fun" itself, so the text reads as a single sentence.
    "If you can explain your app idea to a friend, you can hand it to an "
    "AI agent on make.fun and have a working first version to try before "
    "dinner."
)


def main() -> None:
    # Gate: the entry must be 1-240 Unicode code points, not only whitespace.
    if not 1 <= len(ENTRY) <= 240 or not ENTRY.strip():
        raise ValueError("entry does not meet the 1-240 character gate")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
