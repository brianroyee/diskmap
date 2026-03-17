import sys
from diskmap.cli import run


def main():

    if len(sys.argv) < 2:
        print("Usage: python main.py <directory>")
        return

    path = sys.argv[1]

    run(path)


if __name__ == "__main__":
    main()