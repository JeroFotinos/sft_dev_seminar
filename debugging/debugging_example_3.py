import numpy as np

def normalize_rows(mat):
    # we divide each row by their norm
    mat /= np.linalg.norm(mat, axis=1)[:, None]
    return mat

if __name__ == "__main__":
    A = np.array([[3.0, 4.0], [0.0, 5.0]])
    # import ipdb; ipdb.set_trace()
    B = normalize_rows(A)
    print("A:", A)
    print("B:", B)
