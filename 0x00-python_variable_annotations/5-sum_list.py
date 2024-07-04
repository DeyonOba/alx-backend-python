#!/usr/bin/env python3
"""
Script contains a type-annotated function `sum_list`.
    Function takes a list `input_list` of floats as argument,
    and then returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of floats."""
    return sum(input_list)
