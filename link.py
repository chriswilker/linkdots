from typing import List
import subprocess
import os
from pathlib import Path


def dotfiles() -> List[str]:
    dfiles = []
    p = subprocess.run(["git", "ls-files"], stdout=subprocess.PIPE)
    files = [str(i, "utf-8") for i in p.stdout.splitlines()]
    for f in files:
        if f != __file__ and f != "README.md":
            dfiles.append(f)
    return dfiles


def main() -> None:
    for f in dotfiles():
        link_path = os.path.join(os.path.expanduser("~"), f)
        Path(os.path.dirname(link_path)).mkdir(parents=True, exist_ok=True)
        try:
            os.symlink(os.path.abspath(f), link_path)
            print(f"Created symlink {link_path}")
        except FileExistsError:
            print(f"File {link_path} already exists, not creating link")


if __name__ == "__main__":
    main()
