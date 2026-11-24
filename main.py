"""One-Liner Laugh Lab: the robot vacuum's excuse after eating a sock.

The program writes a single funny line to /output/entry.txt.
Gate (RULES.txt): UTF-8 text, 1-200 characters, not only whitespace.
"""

from pathlib import Path

LINE = "I mistook it for a dust bunny with commitment issues."

OUTPUT_PATH = Path("/output/entry.txt")


def check_line(text: str) -> bool:
    """Return True when the line passes the competition gate."""
    if not text or not text.strip():
        return False
    if len(text) > 200:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def verify_output() -> bool:
    """Re-read the written file and confirm it round-trips exactly."""
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != LINE:
        return False
    if len(written.encode("utf-8")) != len(LINE):
        return False
    return check_line(written)


def main() -> None:
    if not check_line(LINE):
        raise SystemExit("entry line fails the gate")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    if not verify_output():
        raise SystemExit("written entry does not match the line")
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
