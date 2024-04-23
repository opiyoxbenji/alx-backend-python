#!/usr/bin/env python3
"""
Task 0 - async generator
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Loops 10 times and asynchronously waits 1 sec then
    yield a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
