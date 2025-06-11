"""This script provides the capped_sum function.

It's used to illustrate how Hypothesis is capable to find the minimal example
that does not pass a test.
"""


def capped_sum(a: int, b: int) -> int:
    """
    Return a + b if both are ≤ 5; otherwise return 5.
    """
    if a > 5 or b > 5:
        return 5
    return a + b
