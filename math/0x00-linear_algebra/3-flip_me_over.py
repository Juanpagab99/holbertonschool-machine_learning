#!/usr/bin/env python3
"""Transpose a matrix"""


def matrix_transpose(matrix):
    # print(len(matrix[0]))
    # para saber las columnas
    new = []
    for i in range(len(matrix[0])):
        temp = []
        for filas in matrix:
            # print(filas[i])
            temp += [filas[i]]
        new += [temp]
    return new
