"""
Util functions for aggregating numbers.

Parsing allegro (or other site) will result in many different parsed values. They are needed to
corrected/validated/aggregated/converted. This functions relizes such tasks.
"""

from typing import List


def avg_from_list(_list: List[float]) -> float:
    if not _list:
        return 0.0
    if len(_list) == 0:
        return 0.0
    else:
        return sum(_list) // len(_list)


def force_to_int(value: float) -> int:
    if not value:
        return 0
    else:
        return int(value)


def force_to_float(value: int) -> float:
    if not value:
        return 0.0
    else:
        return float(value)


def force_sum(_list: List[float]) -> int:
    if not _list:
        return 0
    if len(_list) == 0:
        return 0
    else:
        return sum(_list)
