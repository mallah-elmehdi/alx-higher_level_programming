#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arglen = len(argv) - 1
    if arglen == 0:
        print("{arglen} arguments.".format(arglen))
    else:
        print("{} argument".format(arglen), end=":\n" if arglen == 1 else "s:\n")
        for i in range(1, arglen + 1):
            print("{}: {}".format(i, argv[i]))
