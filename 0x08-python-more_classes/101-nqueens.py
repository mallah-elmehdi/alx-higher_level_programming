"""N queens"""
import sys


def err(msg):
    """error handling"""
    print(msg)
    exit(1)


def main():
    """main function"""

    if len(sys.argv) != 2:
        err("Usage: nqueens N")
    if not sys.argv[1].isdigit():
        err("N must be a number")
    n = int(sys.argv[1])
    if n < 4:
        err("N must be at least 4")


if __name__ == "__main__":
    main()
