#!/usr/bin/env python3
"""Entry for make.fun bounty ai-happy-01 ("Make the AI judge happy").

The program writes one image to /output/entry.png (or
$MAKEFUN_OUTPUT_DIR/entry.png when that is set): a golden retriever
puppy smiling in a wildflower meadow, stored beside this file as
entry.png (a JPEG, told apart by its first bytes) and copied byte
for byte. Standard library only, no network, deterministic: every
run writes exactly the same bytes.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"entry image missing: {SOURCE}", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    target = os.path.join(OUTPUT_DIR, "entry.png")
    shutil.copyfile(SOURCE, target)
    if os.path.getsize(target) != os.path.getsize(SOURCE):
        print("copy incomplete", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
