#!/usr/bin/env python3
"""
Script imports `async_generator` from the previous task and then writes
a coroutine called `async_comprehension` that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing
over `async_generator`, then return the 10 random numbers.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using an async comprehension."""
    return [num async for num in async_generator()]
