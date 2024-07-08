#!/usr/bin/env python3
"""
Script Import wait_random from the previous python file that you’ve written
and write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns n number of random delay with max_delay been the highest
    possible delay.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    sorted_delays = []
    for delay in delays:
        for i, d in enumerate(sorted_delays):
            if delay < d:
                sorted_delays.insert(i, delay)
                break
        else:
            sorted_delays.append(delay)

    return sorted_delays
