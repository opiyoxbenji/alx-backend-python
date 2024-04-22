#!/usr/bin/env python3
"""
Task 1 - Executing multiple coroutines at the sametime with async
"""
import asyncio
import typing from List

wait_random = __import__("0-basic_async_syntax").wait_random

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Produces wait_random n timees withe the given max_delay
    """
    delays: List[float] = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
