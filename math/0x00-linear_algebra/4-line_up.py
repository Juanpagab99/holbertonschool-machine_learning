#!/usr/bin/env python3
"""Add in matrix"""


def add_arrays(arr1, arr2):
    """Add arrays"""
    if len(arr1) != len(arr2):
        return None
    else:
        new = []
        for i in range(len(arr1)):
            # for j in range(len(arr2))
            new.append(arr1[i] + arr2[i])
        return new
