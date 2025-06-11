import numpy as np
from hypothesis import given, strategies as st
from distance import distance

# strategy for 3-dimensional points with “reasonable” floats
point_3d = st.tuples(
    st.floats(-1e6, 1e6, allow_nan=False, allow_infinity=False),
    st.floats(-1e6, 1e6, allow_nan=False, allow_infinity=False),
    st.floats(-1e6, 1e6, allow_nan=False, allow_infinity=False),
)


@given(point_3d, point_3d)
def test_distance_is_symmetric(p, q):
    """
    Property: distance(p, q) == distance(q, p), within floating-point tolerance.
    """
    d1 = distance(p, q)
    d2 = distance(q, p)
    # use isclose to account for tiny fp round-off
    # assert np.isclose(d1, d2, atol=1e-8), f"d(p,q)={d1}, d(q,p)={d2}"
    assert d1 == d2
