#!/usr/bin/env python3
"""Coroutine to loop 10 times, delays 1 second
between each take and then yields a random number
between 0 and 10"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Returns a random number between 0 and 10 after a
    wait of 1 second"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
