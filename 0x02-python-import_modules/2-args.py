#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arglen = len(argv) - 1
    print(f"{arglen} argument", end=".\n" if arglen == 0 else "s:\n")
    for i in range(1, arglen + 1):
        print(f"{i}: {argv[i]}")
