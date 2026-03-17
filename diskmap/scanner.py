import os
from diskmap.config import IGNORE_DIRS,IGNORE_HIDDEN,IGNORED_NAMES

def should_ignore(path_name, is_hidden=False):
    """Determine if a directory/file should be ignored."""
    if path_name in IGNORE_DIRS:
        return True
    if IGNORE_HIDDEN and is_hidden:
        return True
    if path_name in IGNORED_NAMES:
        return True
    return False

def get_directory_size(path):
    total = 0
    try:
        for entry in os.scandir(path):
            name = entry.name
            is_hidden = name.startswith('.')

            if should_ignore(name, is_hidden):
                continue

            try:
                if entry.is_file(follow_symlinks=False):
                    total += entry.stat(follow_symlinks=False).st_size
                elif entry.is_dir(follow_symlinks=False):
                    total += get_directory_size(entry.path)
            except (PermissionError, FileNotFoundError):
                pass
    except (PermissionError, FileNotFoundError):
        pass
    return total

def scan_directory(path):
    results = []
    try:
        for entry in os.scandir(path):
            name = entry.name
            is_hidden = name.startswith('.')

            if should_ignore(name, is_hidden):
                continue

            if entry.is_dir(follow_symlinks=False):
                size = get_directory_size(entry.path)
                results.append((entry.path, size))
    except (PermissionError, FileNotFoundError):
        pass

    results.sort(key=lambda x: x[1], reverse=True)
    return results   