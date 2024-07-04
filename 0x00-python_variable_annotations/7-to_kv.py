#!/usr/bin/env python3
"""
Script contatins a funciton `to_kv`.
    Function take 2 arguments:
    - `k` of string type.
    - `v` of int or float type.

    Returns a tuple of element k, and squared v.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple contain the value of k and the square value of v."""
    return (k, v**2)
