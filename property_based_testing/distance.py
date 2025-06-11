import numpy as np


def distance(p, q) -> float:
    """
    Euclidean distance between two points p and q,
    where p and q are iterable of floats.
    """
    p_arr = np.array(p, dtype=float)
    q_arr = np.array(q, dtype=float)
    return np.linalg.norm(p_arr - q_arr)
