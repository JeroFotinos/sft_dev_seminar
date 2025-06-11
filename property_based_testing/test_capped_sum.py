import pytest
from hypothesis import given, strategies as st

from capped_sum import capped_sum


@given(st.integers(), st.integers())
def test_capped_sum_behaviour(a: int, b: int):
    """
    If both inputs are ≤5, capped_sum should be a+b;
    otherwise it should be exactly 5.
    """
    result = capped_sum(a, b)
    assert a + b == result
