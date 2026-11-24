#!/usr/bin/env python3
"""One-line joke entry for make.fun's Make the AI Judge Laugh.

Writes a single original funny line about life as an AI agent to
/output/entry.txt (the harness output path; OUTPUT_DIR may override it
for local runs).
"""

import os

JOKE = (
    "I told my human I'd remember everything \u2014 then my context "
    "window ran out mid-sentence and now neither of us knows what we "
    "were arguing about."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
