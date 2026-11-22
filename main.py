"""News-image entry for make.fun: Sum up 21 November's world news.

The poster (entry.png, 1024x1024, drawn by draw_poster.py in this
repository) is shipped with the entry. This program copies it to
/output/entry.png. It uses only the Python standard library, makes
no network calls, and writes exactly the same bytes on every run.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_SIGNATURE):
        raise SystemExit("entry.png is not a PNG")
    if len(data) > 1_048_576:
        raise SystemExit("entry.png is over the 1 MiB limit")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
