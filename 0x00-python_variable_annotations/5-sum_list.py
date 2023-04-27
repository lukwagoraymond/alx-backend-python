#!/usr/bin/env python3
"""Type-Annotated function which takes a list input
of floats as arguments and returns their sum as a float"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of floats in a list"""
    return float(sum(input_list))
