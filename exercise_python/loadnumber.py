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


def fibonacci(number: int):
    """
    This function outputs a 'Fiboacci' sequence.
      F0 = 0, F1 = 1
      Fn+2 = Fn + Fn+1 (N ≥ 0)
    """
    sequence_pre = 0
    sequence = 1
    for _ in range(number):
        print(sequence)
        sequence_pre, sequence = sequence, sequence_pre + sequence
