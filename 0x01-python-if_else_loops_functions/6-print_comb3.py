#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if j != i:
            print("{:d}{:d}".format(i, j), end="\n" if (
                j == 8 and i == 9)else ", ")
