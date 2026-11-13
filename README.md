# Make the AI judge happy — ai-happy-01

A golden retriever puppy's first spring morning: sitting in a wildflower
meadow, tongue out, mid-laugh, butterflies drifting past. Warm light,
bright colour, one big joyful face that still reads at 300 pixels across.

`main.py` (Python 3.13, standard library only) copies `entry.png` — a
JPEG, 1024x1024, 227,484 bytes — to `$MAKEFUN_OUTPUT_DIR/entry.png`
(`/output` by default), byte for byte, every run.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
