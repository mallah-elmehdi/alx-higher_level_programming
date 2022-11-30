#!/usr/bin/python3
def islower(c):
    return ord(c) in range(97, 122)


def uppercase(str):
    for i in range(len(str)):
        if (islower(str[i])):
            print("{:c}".format(ord(str[i]) - 32),
                  end="" if i + 1 < len(str) else "\n")
        else:
            print(str[i], end="" if i + 1 < len(str) else "\n")