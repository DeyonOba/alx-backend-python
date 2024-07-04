#!/usr/bin/env python3
"""
Script displays how to annotate the below function parameter
and return value.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Creates a list of tuples containing a sequence type, and
    an integer which is the  length of the sequence type.
    """
    return [(i, len(i)) for i in lst]
