#!/usr/bin/python3
def islower(c):
    return ord(c) in range(97, 123)


def uppercase(str):
    upper_str = ''
    for c in str:
        if (islower(c)):
            upper_str += chr(ord(c) - 32)
        else:
            upper_str += c
    print("{:s}".format(upper_str))
