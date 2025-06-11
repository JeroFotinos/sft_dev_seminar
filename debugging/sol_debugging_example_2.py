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
        print("Distance is exactly sqrt(2)")
    else:
        print(f"Distance is {d}, not exactly {target}")

if __name__ == "__main__":
    p = (0.0, 0.0)
    q = (1.0, 1.0)
    correct_distance = Decimal(2).sqrt()
    check_distance(vector_1=p, vector_2=q, target=correct_distance)

# # The correct checking function would be
# def check_distance(vector_1, vector_2, target):
#     d = distance(vector_1, vector_2)
#     # we compare the distances
#     if np.isclose(d, target):
#         print("Distance within tolerance from the correct one.")
#     else:
#         print(f"Distance is {d}, not within tolerance from {target}")
