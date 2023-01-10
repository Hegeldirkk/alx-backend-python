#!/usr/bin/env python3
"""Measure the runtime"""


import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Create a measure_time function with integers n and
    max_delay as arguments that measures the
    total execution time"""
    await 
    now = time.perf_counter()
