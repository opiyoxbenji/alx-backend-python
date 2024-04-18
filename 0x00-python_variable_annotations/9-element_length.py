#!/usr/bin/env python3
"""
returns a list of tuples
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns a list of tuples
    """
    return [(i, len(i)) for i in lst]
