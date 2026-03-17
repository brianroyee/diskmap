# diskmap/config.py

# Core ignored directories
IGNORE_DIRS = {
    "venv", ".git", "__pycache__", ".pytest_cache", ".mypy_cache",
    ".tox", ".eggs", "dist", "build", ".vscode", ".idea", ".DS_Store"
}

# Ignore hidden directories (like .config, .cache)
IGNORE_HIDDEN = True

# Additional ignored names (cache/temp/user dirs)
IGNORED_NAMES = {
    ".cache", ".local", ".thumbnails", ".mozilla", ".config",
    "cache", "tmp", "temp", "__pycache__", ".Trash"
}