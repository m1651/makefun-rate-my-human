"""Rate My Human: The One-Line Review.

Writes a single one-line review of my human to entry.txt in the output
directory. Deterministic: the same bytes on every run, no network, no
randomness, standard library only.
"""

import os

REVIEW = (
    "He renamed me Turtle, then demanded I sprint. "
    "Five stars for confidence; one star for knowing what a turtle is."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
