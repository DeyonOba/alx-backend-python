#!/usr/bin/env python3
"""
Script contains the asynchronous generator function `async_generator`
that takes no arguments.

The coroutine will loop 10 times, each time asynchronous wait 1 second,
then yield a random number between 0 and 10. Use the `random` module.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generates 10 asynchronous random number between 0 and 10."""
    for num in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0., 10.)
