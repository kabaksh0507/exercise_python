"""
This module provides functions for numbers.
"""

from typing import List


def load_numbers_sorted(fname: str) -> List[int]:
    """
    This function specification:
        Extract numbers from a file.
        Sort in ascending order.
        Return it as list.
    """
    numbers = []
    with open(fname) as inputfile:
        numbers = sorted(map(lambda e: int(e), inputfile))
    return numbers
