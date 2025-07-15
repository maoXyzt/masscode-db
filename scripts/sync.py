# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
# ]
# ///

import os
import shutil
from pathlib import Path
from textwrap import dedent

from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    sync_dir = os.getenv("SYNC_DIR")
    assert sync_dir, "SYNC_DIR is not set"
    sync_dir = Path(sync_dir)
    assert sync_dir.is_dir(), f"Directory {sync_dir.as_posix()!r} does not exist"

    local_dir = Path(__file__).parents[1] / "massCode"
    assert local_dir.is_dir(), f"Directory {local_dir.as_posix()!r} does not exist"

    print(
        dedent(f"""
        --------------------------------------------
        Syncing from: {local_dir.as_posix()!r}
                to  : {sync_dir.as_posix()!r}
        --------------------------------------------
        """)
    )
    for p1 in local_dir.iterdir():
        p2 = sync_dir / p1.relative_to(local_dir)
        sync_file(p1, p2)


def sync_file(p1: Path, p2: Path) -> None:
    """
    Sync a file or directory from p1 to p2.
    """
    if p1.is_file():
        shutil.copy(p1, p2)
        print(f"Synced: {p1.as_posix()!r} >>>> {p2.as_posix()!r}")
    elif p1.is_dir():
        shutil.copytree(p1, p2)
        print(f"Synced: {p1.as_posix()!r} >>>> {p2.as_posix()!r}")


if __name__ == "__main__":
    main()
