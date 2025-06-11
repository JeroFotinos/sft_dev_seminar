from decimal import Decimal, getcontext

import numpy as np

# Set the desired precision (e.g., 50 decimal places)
getcontext().prec = 50


def distance(p, q):
    return np.linalg.norm(np.array(p) - np.array(q))


def check_distance(vector_1, vector_2, target):
    d = distance(vector_1, vector_2)
    # we compare the distances
    if d == target:
        print("Correct distance calculation :)")
    else:
        print(f"There's some type of error :(")


if __name__ == "__main__":
    p = (0.0, 0.0)
    q = (1.0, 1.0)
    # import ipdb; ipdb.set_trace()
    correct_distance = Decimal(2).sqrt()
    check_distance(vector_1=p, vector_2=q, target=correct_distance)
