# finds folder sizes

import os


def get_directory_size(path):
    total = 0

    try:
        for entry in os.scandir(path):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_directory_size(entry.path)
    except PermissionError:
        pass

    return total


def scan_directory(path):
    results = []

    for entry in os.scandir(path):
        if entry.is_dir():
            size = get_directory_size(entry.path)
            results.append((entry.path, size))

    results.sort(key=lambda x: x[1], reverse=True)
    return results