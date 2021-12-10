#!/usr/bin/env python3
"""calcular la derivada"""


def poly_derivative(poly):
    """funcion derivada"""

    if type(poly) != list or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    if poly is None:
        return None
    nuevo = list(range(len(poly)-1))
    for i in range(len(nuevo)):
        if type(i) != int:
            return None
        nuevo[i] = poly[i + 1] * (i + 1)
    return nuevo
