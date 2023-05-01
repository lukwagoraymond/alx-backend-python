#!/usr/bin/env python3
"""Python and Async Coroutines"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of all delayed async coroutines"""
    tasks = [wait_random(max_delay) for i in range(n)]
    delayed_tasks = [await task for task in asyncio.as_completed(tasks)]
    return delayed_tasks
    # results = await asyncio.gather(*tasks)
    # sorted_results = sorted(results)
    # return sorted_results
