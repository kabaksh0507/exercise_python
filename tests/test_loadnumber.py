"""
This module tests the 'loadnumber' module.
"""

import os
from typing import List
import pytest
from exercise_python.loadnumber import load_numbers_sorted, fibonacci


@pytest.fixture
def txt() -> str:
    """
    Create input file before test and delete it's file after test.
    """
    with open("numbers.txt", "w") as outfile:
        for num in [4, 5, 2, 3, 1]:
            outfile.write("{}\n".format(num))

    yield "numbers.txt"
    os.remove("numbers.txt")


@pytest.fixture
def txt_and_list(txt) -> tuple[str, List[int]]:
    """
    Create input data and output data.
    """
    yield txt, [1, 2, 3, 4, 5]


def test_load_numbers_sorted(txt_and_list):
    """
    Test target module 'load_numbers_sorted'.
    """
    assert load_numbers_sorted(txt_and_list[0]) == txt_and_list[1]


def test_fiboacci(capsys):
    """
    Test target module 'fiboacci'.
    """
    fibonacci(21)

    out, _ = capsys.readouterr()

    assert out == (
        "1\n"
        "1\n"
        "2\n"
        "3\n"
        "5\n"
        "8\n"
        "13\n"
        "21\n"
        "34\n"
        "55\n"
        "89\n"
        "144\n"
        "233\n"
        "377\n"
        "610\n"
        "987\n"
        "1597\n"
        "2584\n"
        "4181\n"
        "6765\n"
        "10946\n"
    )
