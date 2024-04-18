#!/usr/bin/env python3
"""
Creating a table
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple and square of int/float as two elements
    """
    return (k, float(v * v))
