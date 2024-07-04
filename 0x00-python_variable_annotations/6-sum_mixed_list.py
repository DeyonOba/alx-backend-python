#!/usr/bin/env python3
"""
Script contains type-annotated function `sum_mixed_list`.
    `sum_mixed_list` takes a list `mxd_lst` of integers and floats,
    and returns a sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a list containing integers and floats."""
    return sum(mxd_lst)
