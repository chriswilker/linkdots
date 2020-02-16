## Introduction

This is a simple way to symlink dotfiles to your home directory. All you have to do is git commit your dotfiles and run a Python script. The script is very small. I recommend reading it if you want more information on how it works.

## Use

Fork and then clone this repository, then git commit your dotfiles to it. Or just copy `link.py` to a git repository containing your dotfiles. **Only commit your dotfiles**, anything committed other than `README.md` and `link.py` will be symlinked to the home directory. Then run `python3 link.py`

Symlinks to your dotfiles will be generated in your home directory. If any dotfiles are stored in subdirectories, the subdirectories will be created in the home directory if they don't already exist.

The script will not create a link if the dotfile is already in the home directory. Delete the existing dotfile if you want to overwrite it.

The script requires Python 3.5+ and the git cli. It works on \*nix. It should work on versions of Windows that support Python's os.symlink, but I haven't tested it.
