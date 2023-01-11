#!/usr/bin/python3
"""
Module functions:
    * def pascal_triangle(n):
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n

    Args:
        -> n: int

    Return: lists
    """

    new_list = []
    for i in range(n):
        new_list.append([])
        for j in range(i + 1):
            if i == 0 or j == 0 or j == i:
                new_list[i].append(1)
            else:
                new_list[i].append(
                    new_list[i - 1][j] + new_list[i - 1][j - 1]
                )

    return new_list
