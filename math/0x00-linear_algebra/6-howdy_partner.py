#!/usr/bin/env python3
"""Concatenate arrays"""


def cat_arrays(arr1, arr2):
    if type(arr1) == list and type(arr2) == list:
        return arr1 + arr2
