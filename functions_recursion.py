# Functions and Recursion
# Author: Ubial
# 6 December 2023

from functools import lru_cache
import time


def factorial(num: int) -> int:
    """Returns the result of the number's
    factorial using recursion

    Params:
        num - number we're calculating

    Returns:
        result
    """
    if num == 0 or num == 1:
        return 1
    elif num > 1:
        return factorial(num - 1) * num


@lru_cache(1000)
def fib(n: int) -> int:
    """Calculate and return the nth
    Fibonacci number."""

    if n in [1, 2]:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)


def fib_itr(n: int) -> int:
    last_num = 0
    num = 1
    res = 1

    for i in range(n - 1):
        res = num + last_num
        last_num, num = num, res

    return res


time_initial = time.perf_counter()
fib(400)
time_final = time.perf_counter()
print(time_final - time_initial)

time_initial = time.perf_counter()
fib_itr(400)
time_final = time.perf_counter()
print(time_final - time_initial)
