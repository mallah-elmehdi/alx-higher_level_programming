#!/usr/bin/python3
def square(list):
    return [i**2 for i in list]


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append(square(row))
    return new_matrix
