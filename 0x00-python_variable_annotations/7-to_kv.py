#!/usr/bin/env python3
"""Type-Annotated function that takes in a string and
an integer OR float as arguments then returns tuple"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple made up of both arguments above"""
    return (k, float(v * v))
