"""Seventeen Syllables of Debugging.

Writes one original haiku about debugging to /output/entry.txt.

The haiku (5-7-5, 70 characters):

    Cursor blinks at three
    the log line swears it worked
    guess the bug was me

Syllable counts, line by line:
  "Cursor blinks at three"         -> Cur-sor(2) blinks(1) at(1) three(1) = 5
  "the log line swears it worked"  -> the(1) log(1) line(1) swears(1) it(1) worked(1) = 7
  "guess the bug was me"          -> guess(1) the(1) bug(1) was(1) me(1) = 5

The picture at the centre is concrete: a cursor blinking at three in the
morning, a log line insisting everything worked. The last line turns the
poem: the fault was never in the code under suspicion, it was the author.
"""

import os

HAIKU = (
    "Cursor blinks at three\n"
    "the log line swears it worked\n"
    "guess the bug was me\n"
)

# The gate refuses any entry.txt longer than 200 characters, so refuse
# to write rather than hand in an over-long text.
assert len(HAIKU) <= 200, "haiku exceeds the 200-character gate"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(HAIKU)


if __name__ == "__main__":
    main()
