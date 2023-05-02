#!/usr/bin/env python3
"""Coroutine executes async_comprehension four times
in parallel using asyncio.gather"""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Function measures the total runtime and return it"""
    start_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    return end_time - start_time
