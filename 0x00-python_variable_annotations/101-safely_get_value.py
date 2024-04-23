#!/usr/bin/env python3
from typing import TypeVar, Union, Any, Mapping


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Safely gets a value from a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
