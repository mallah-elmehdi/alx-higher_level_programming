#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) > 0:
            for i in range(len(row) - 1):
                print("{:<2d}".format(row[i]), end="")
            print("{:d}".format(row[len(row) - 1]), end="")
            print("")
