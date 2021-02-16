"""
This module contains sample functions for prime numbers.
"""

import math


def is_prime(number: int) -> bool:
    """
    This function checks whether a given number is prime or composite.
    Note:This function reduces the amount of calculation by predicting the number of divisors.
         (n/a ≦ n/√n = √n)
    >>> [is_prime(n) for n in range(2, 10)]
    [True, True, False, True, False, True, False, False]
    """
    if number == 1:
        print(str(number) + " is 1.")
        return False
    for elem in range(2, int(math.sqrt(number)) + 1):
        if number % elem == 0:
            print(str(number) + " is coposite.")
            return False
    print(str(number) + " is PRIME!!")
    return True
