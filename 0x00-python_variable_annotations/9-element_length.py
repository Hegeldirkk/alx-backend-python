#!/usr/bin/env python3
"""element length"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns elements of the list"""
    return [(x, len(x)) for x in lst]
