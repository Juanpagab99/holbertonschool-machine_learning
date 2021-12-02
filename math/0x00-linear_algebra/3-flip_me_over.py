#!/usr/bin/env python3
"""Transpose a matrix"""


def matrix_transpose(matrix):
    """Matrix transpose"""
    # print(len(matrix[0]))
    # para saber las columnas
    new = []
    for i in range(len(matrix[0])):
        temp = []
        for j in matrix:
            # print(j[i])
            temp += [j[i]]
            print(temp)
        new += [temp]
        # print("-", new)
    return new
