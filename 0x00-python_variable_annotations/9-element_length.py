#!/usr/bin/env python3
"""
returns a list of tuples
"""

from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    returns a list of tuples containing
    an element from the input list along with its length
    """
    return [(i, len(i)) for i in lst]
