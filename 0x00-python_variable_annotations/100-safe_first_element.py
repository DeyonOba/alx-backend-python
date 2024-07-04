#!/usr/bin/env python3
"""
Script that illustrates the correct duck-typed annotation of the function
`safe_first_element`.
"""
from typing import Union, Sequence, Any, NewType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Correct duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
