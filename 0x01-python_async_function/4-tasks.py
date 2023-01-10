#!/usr/bin/env python3
"""Let's execute multiple coroutines
at the same time with async"""


from typing import List
import random
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the del"""
    wait_list, result = [], []

    for _ in range(n):
        wait_list.append(task_wait_random(max_delay))

    for res in asyncio.as_completed(wait_list):
        compl = await res
        result.append(compl)

    return result
