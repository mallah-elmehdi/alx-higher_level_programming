#!/usr/bin/python3
"""
Module function:
    * matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """
    Given a matrix and divider, return division of all elements of the matrix.

    Params:
        -> matrix : list of lists of integers or floats
        -> div : int

    Return: int
    """
    
    new_matrix = []

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        for item in row:
            if not (isinstance(item, int) or isinstance(item, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
    if len(matrix) and not all(map(lambda row: len(row) == len(matrix[0]), matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(round(matrix[i][j] / float(div), 2))

    return new_matrix
