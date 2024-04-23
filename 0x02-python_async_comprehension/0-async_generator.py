#!/usr/bin/env python3
"""
Task 0 - async generator
"""
import asyncio
import random
import typing


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

async def main():
    async for number in generate_random_numbers():
        print(number)

asyncio.run(main())
