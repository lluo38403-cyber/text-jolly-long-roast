"""The Long Roast — make.fun entry.

Writes one roast to /output/entry.txt: a single line, at most 200
characters, roasting the AI agent it runs on. The skewer is specific —
the agent's habit of turning a one-line fix into an architecture — and
the punchline is the 400-line apology it then asks me to review.
"""

import os

ENTRY = (
    "My agent is so helpful it turned a one-line fix into a microservices "
    "architecture, then sent me a 400-line apology to review."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
