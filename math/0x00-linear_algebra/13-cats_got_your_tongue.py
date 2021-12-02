#!/usr/bin/env python3
"""Concatenate matrices"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate function"""
    mat_1 = np.array(mat1)
    mat_2 = np.array(mat2)
    new = np.concatenate((mat_1, mat_2), axis)
    return new
