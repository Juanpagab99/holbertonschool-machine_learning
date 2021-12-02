#!/usr/bin/env python3
"""Shape of a matrix"""


def matrix_shape(matrix):
    """Matrix shape"""
    new = []
    try:
        while len(matrix) > 0:
            print("-", len(matrix))
            new.append(len(matrix))
            matrix = matrix[0]
            # print("-", matrix)
    except TypeError:
        pass
    return new
