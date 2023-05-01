#!/usr/bin/env python3
"""Python and Async await function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a delayed value"""
    rand_delay = random.uniform(0, max_delay)
    await asyncio.sleep(rand_delay)
    return rand_delay
