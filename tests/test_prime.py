"""
This module tests the 'prime' module.
"""

import pytest
from exercise_python.prime import is_prime

# デコレータによるパラメータ化テスト
@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
        (10, False),
        (11, True),
        (12, False),
        (2357, True),
        (2358, False),
    ],
)
def test_is_prime(number, expected):
    """
    Test 'is_prime()' function
    """
    assert is_prime(number) == expected
