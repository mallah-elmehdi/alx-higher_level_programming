#!/usr/bin/python3
def square_matrix_map(m=[]):
    return list(map(lambda r: list(map(lambda e: e**2, r)), m))
