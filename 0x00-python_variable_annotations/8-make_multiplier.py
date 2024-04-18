#!/usr/bin/env python3
"""
Multiples a float by a given number
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Multiplies a float by a multiplier
    """
    return lambda x: x * multiplier
