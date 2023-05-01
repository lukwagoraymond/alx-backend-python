#!/usr/bin/env python3
"""Python Async Task Object"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_depth: int) -> asyncio.Task:
    """Returns a Task Object"""
    return asyncio.create_task(wait_random(max_depth))
