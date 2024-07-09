#!/usr/bin/env python3
"""
Script imports `async_comprehension` from 1-async_comprehension file
and write a `measure_runtime` coroutine that will execute
`async_comprehension` four times in parallel using asyncio.gather
"""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Gets the measured time used to run 4 concourent execution
    of async_comprehension.
    """
    start_time = time.perf_counter()
    value = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time
