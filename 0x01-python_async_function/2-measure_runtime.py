#!/usr/bin/env python3
"""Measure the runtime"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Create a measure_time function with integers n and
    max_delay as arguments that measures the
    total execution time"""
    now = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.time()
    return (elapsed - now) / n
