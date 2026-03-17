import os


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