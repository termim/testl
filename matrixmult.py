import numpy as np


def matrix_multiplier(mat1, mat2):
    row_mat1, col_mat1 = np.shape(mat1)
    row_mat2, col_mat2 = np.shape(mat2)

    if col_mat1 != row_mat2:
        raise ValueError("Matrix dimensions are incompatible")

    if row_mat1 | col_mat1 == 0:
        raise ValueError("The first matrix entered is not a matrix")

    if row_mat2 | col_mat2 == 0:
        raise ValueError("The second matrix entered is not a matrix")


        