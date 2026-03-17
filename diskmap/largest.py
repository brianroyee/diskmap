import os
from diskmap.config import IGNORE_DIRS,IGNORE_HIDDEN,IGNORED_NAMES

def should_ignore_dir(name):
    if name in IGNORE_DIRS:
        return True
    if IGNORE_HIDDEN and name.startswith("."):
        return True

    if name in IGNORED_NAMES:
        return True

    return False


def find_largest_files(path, limit=10):

    files = []

    for root, dirs, filenames in os.walk(path):

        for name in filenames:

            try:
                full = os.path.join(root, name)
                size = os.path.getsize(full)

                files.append((full, size))

            except PermissionError:
                pass

            except FileNotFoundError:
                pass

    files.sort(key=lambda x: x[1], reverse=True)
    return files[:limit]