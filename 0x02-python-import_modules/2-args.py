#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arglen = len(argv) - 1
    print(f"{arglen} arguments", end=".\n" if arglen == 0 else ":\n")
    for i in range(1, arglen + 1):
        print(f"{i + 1}: {argv[i]}")
