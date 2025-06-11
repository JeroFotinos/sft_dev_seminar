import numpy as np


def normalize_rows(mat):
    # Bug: dividing in-place alters the original array
    mat /= np.linalg.norm(mat, axis=1)[:, None]
    return mat


if __name__ == "__main__":
    A = np.array([[3.0, 4.0], [0.0, 5.0]])
    import ipdb

    ipdb.set_trace()
    B = normalize_rows(A)
    print("A:", A)
    print("B:", B)

# # Correct code would be
# def normalize_rows(mat):
#     # Bug: dividing in-place alters the original array
#     new_mat = np.copy(mat)
#     new_mat /= np.linalg.norm(new_mat, axis=1)[:, None]
#     return new_mat
