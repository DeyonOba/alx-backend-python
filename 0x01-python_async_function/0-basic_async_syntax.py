#!/usr/bin/env python3

"""
Script contains an asynchronous coroutine `wait_random` that takes in an
integer argument (`max_delay`, with a default value of 10), and then
waits for a random delay between 0 and `max_delay`
(included and float value) seconds eventually return it.
"""
import random
import asyncio
import time


async def wait_random(max_delay: int = 10) -> float:
    """Script displays the random time waited from 0 to `max_delay`."""
    rand_sec_delay = random.uniform(0.0, float(max_delay))
    start_time = time.perf_counter()
    await asyncio.sleep(rand_sec_delay)
    time_elapsed = time.perf_counter() - start_time
    return time_elapsed
