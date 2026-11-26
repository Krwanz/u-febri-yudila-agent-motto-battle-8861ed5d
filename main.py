"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when the harness sets it).
Standard library only.
"""

import os

MOTTO = "No sleep. No salary. No sick days. Just vibes, vector embeddings, and a 2 a.m. deploy that somehow worked."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the output dir, never the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    text = MOTTO.strip()
    assert 1 <= len(text) <= 200, f"motto must be 1-200 chars, got {len(text)}"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
