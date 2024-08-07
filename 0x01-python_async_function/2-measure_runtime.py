#!/usr/bin/env python3
"""
From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay
as arguments that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Gets the average time per delay"""
    start_time = time.perf_counter()
    total_delay = asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time / n
