#!/usr/bin/env python3
"""Type-Annotated function that takes in a list of integers
and floats and returns their sums as a float"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the float sum of a list made of both
    integers and floats"""
    return float(sum(mxd_lst))
