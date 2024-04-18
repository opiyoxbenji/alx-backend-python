#!/usr/bin/python3
from typing import TypeVar, Dict, Any

K = TypeVar('K')  # Type variable for keys
V = TypeVar('V')  # Type variable for values


def safely_get_value(dct: Dict[K, V], key: K, default: V = None) -> V:
    """
    Safely gets a value from a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
