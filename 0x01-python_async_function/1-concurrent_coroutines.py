#!/usr/bin/env python3
"""
Task 1 - Executing multiple coroutines at the sametime with async
"""
import asyncio
import random

async def wait_random(max_delay:int = 10) -> float:
    """
    Coroutine that waits for a random delay between 0 and max_delay seconds
    """
    delay: float = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Produces wait_random n timees withe the given max_delay
    """
    delays: List[float] = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
