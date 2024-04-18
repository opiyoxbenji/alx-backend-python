#!/usr/bin/env python3
"""
Multiples a float by a given number
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multipier_func(x: float -> float:
            return x * multiplier

    return multiplier_func
