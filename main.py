"""The Meeting That Should Have Been an Email - entry program.

Writes a single one-line joke about a meeting that should have been an
email to /output/entry.txt. The line: Nine words in an email would have
done it, but twelve of us spent an hour watching a man read a spreadsheet
aloud.
"""

import os

LINE = ("Nine words in an email would have done it, but twelve of us spent "
        "an hour watching a man read a spreadsheet aloud.")


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 200 or not line.strip():
        raise ValueError("entry must be 1-200 characters")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be a single sentence")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Self-verify: the file the grader reads must be byte-exact.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise ValueError("entry.txt does not match the line byte for byte")


if __name__ == "__main__":
    main()
