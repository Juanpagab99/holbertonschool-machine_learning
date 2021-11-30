#!/usr/bin/env python3
"""Add 2D matrices"""


def add_matrices2D(mat1, mat2):
    if len(mat1) == len(mat2):
        new = []
        for i in range(len(mat1)):
            row = []
            if len(mat1[i]) == len(mat2[i]):
                for j in range(len(mat1[i])):
                    row.append(mat1[i][j] + mat2[i][j])
                new.append(row)
            else:
                return None
        return new
