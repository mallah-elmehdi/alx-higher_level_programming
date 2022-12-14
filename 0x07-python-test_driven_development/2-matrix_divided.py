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

    if not (
        isinstance(matrix, list)
        and all(map(lambda row: isinstance(row, list), matrix))
        and all(
            map(
                lambda row: all(map(
                    lambda item: isinstance(
                        item, int) or isinstance(item, float), row
                )),
                matrix,
            )
        )
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(map(lambda row: len(row) == len(matrix[0]), matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(round(matrix[i][j] / float(div), 2))

    return new_matrix
