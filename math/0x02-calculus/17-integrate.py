#!/usr/bin/env python3
"""Integrate function"""


def poly_integral(poly, C=0):
    """Integrate all"""
    if type(poly) is not list and not poly:
        return None
    elif len(poly) == 0 and type(C) is not int:
        return None
    elif poly == [0]:
        return [C]
    else:
        integral = []
        integral.append(C)
        for i in range(len(poly)):
            x = poly[i] / (i + 1)
            integral.append(int(x) if x.is_integer() else x)
        return integral
