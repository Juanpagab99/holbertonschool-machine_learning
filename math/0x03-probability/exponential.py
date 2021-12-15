#!/usr/bin/env python3
"""Initialize Exponential"""


class Exponential:
    """Exponential class"""

    def __init__(self, data=None, lambtha=1.):
        """Represents an exponential distribution"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = (1 / (sum(data) / len(data)))
