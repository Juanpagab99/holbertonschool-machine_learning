#!/usr/bin/env python3
"""Shape of a matrix"""


def matrix_shape(matrix):
    new = []
    try:
        while len(matrix) > 0:
            new.append(len(matrix))
            matrix = matrix[0]
    except TypeError:
        pass
    return new
