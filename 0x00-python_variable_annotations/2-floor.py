#!/usr/bin/env python3
"""
Script contains a type-annotated function `floor`.
    Function takes a single argument `n` of float type,
    and returns a floored integer number.
"""
import math


def floor(n: float) -> int:
    """Convert a float number to a floored integer number."""
    return math.floor(n)
