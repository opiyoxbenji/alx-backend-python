#!/usr/bin/env python3
"""
Task 2 - Measuring runtime
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Computes average runtime wait_n
    """
    start_time = time.time()
    asyncio(wait_n(n, max_delay))
    return (time.time() - start_time) / n
