#!/usr/bin/python3
from typing import TypeVar, Union, Any, Mapping


K = TypeVar('K')
Res = Union[Any, K]
Def = Union[K, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Safely gets a value from a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
