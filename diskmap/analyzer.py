import os
from diskmap.config import IGNORE_DIRS, IGNORE_HIDDEN, IGNORED_NAMES


def should_ignore_dir(name):

    if name in IGNORE_DIRS:
        return True

    if IGNORE_HIDDEN and name.startswith("."):
        return True

    if name in IGNORED_NAMES:
        return True

    return False


def analyze_file_types(path):
    type_sizes = {}

    for root, dirs, filenames in os.walk(path):

        dirs[:] = [d for d in dirs if not should_ignore_dir(d)]

        for name in filenames:
            try:
                full = os.path.join(root, name)
                size = os.path.getsize(full)

                if "." in name:
                    ext = "." + name.rsplit(".", 1)[1].lower()
                else:
                    ext = "[no extension]"

                type_sizes[ext] = type_sizes.get(ext, 0) + size

            except PermissionError:
                pass
            except FileNotFoundError:
                pass

    return sorted(type_sizes.items(), key=lambda x: x[1], reverse=True)