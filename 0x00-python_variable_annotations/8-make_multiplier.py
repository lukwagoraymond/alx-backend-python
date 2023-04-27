#!/usr/bin/env python3
"""Type-annotated function that returns another function
that multiplies a float by the multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns function that multiplies a float by the multiplier"""
    return lambda x: multiplier*x
