#!/usr/bin/env python3
"""
Script contains type-annotated function `make_multiplier`.
    Function takes a float `multiplier` as an argument,
    and return a function that multiplier a float by the multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function multiples a multiplier by a float.

    Upon first function call `make_multiplier returns a the function
    `functionX`, then `functionX` then multiples a float number by the
    stored value of the argument `multiplier`.

    Example:

    >>> functionX = make_mulitplier(2.22)
    >>> print(functionX(2.22))
    4.928400000000001
    """
    def functionX(number: float):
        return multiplier * number
    return functionX
