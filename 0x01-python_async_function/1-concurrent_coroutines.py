#!/usr/bin/emv python3
"""Let's execute multiple coroutines
at the same time with async"""


from typing import List
import random
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays
    (float values) list of the delays should be in
    ascending order without using sort()"""
    wait_list = []

    for i in range(n):
        wait_list.append(wait_random(max_delay))

    return wait_list.sort()
