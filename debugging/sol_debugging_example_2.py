import numpy as np

def distance(p, q):
    return np.linalg.norm(np.array(p) - np.array(q))

def check_distance(vector_1, vector_2, target):
    d = distance(vector_1, vector_2)
    # we compare the distances
    if d == target:
        print("Distance is exactly 2")
    else:
        print(f"Distance is {d}, not exactly {target}")

if __name__ == "__main__":
    p = (0.0, 0.0, 0.0)
    q = (2/np.sqrt(3), 2/np.sqrt(3), 2/np.sqrt(3))
    correct_distance = 2.0
    check_distance(vector_1=p, vector_2=q, target=correct_distance)

# # The correct checking function would be
# def check_distance(vector_1, vector_2, target):
#     d = distance(vector_1, vector_2)
#     # we compare the distances
#     if np.isclose(d, target):
#         print("Distance is exactly 2")
#     else:
#         print(f"Distance is {d}, not exactly {target}")
