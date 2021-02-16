"""
This module tests the 'loadnumber' module.
"""

import os
from typing import List
import pytest
from exercise_python.loadnumber import load_numbers_sorted


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
    Test target module.
    """
    assert load_numbers_sorted(txt_and_list[0]) == txt_and_list[1]
