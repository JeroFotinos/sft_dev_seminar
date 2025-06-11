import numpy as np

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
    p = (0.0, 0.0, 0.0)
    q = (2/np.sqrt(3), 2/np.sqrt(3), 2/np.sqrt(3))
    correct_distance = 2.0
    check_distance(vector_1=p, vector_2=q, target=correct_distance)
