#!/usr/bin/env python3
"""
Computes the sum of lists with integers and floats
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Sum of a list with floats and integers
    """
    return float(sum(mxd_list))
