#!/usr/bin/env python3
"""
Script creates a custome type variable
Concepts:
    - Mapping.
    - TypeVar
"""
from typing import TypeVar, Any, Mapping, Union
T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, Any],
    key: Any,
    default: Union[T, None] = None
) -> Union[T, None]:
    """Assign type annotations to return function and parameters."""
    if key in dct:
        return dct[key]
    else:
        return default
