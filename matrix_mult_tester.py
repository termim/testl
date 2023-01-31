import numpy as np
import pytest


def matrix_multiplier_tester(mat1, mat2):
    row_mat1, col_mat1 = np.shape(mat1)
    row_mat2, col_mat2 = np.shape(mat2)        

    if col_mat1 != row_mat2:
        raise ValueError("Matrix dimensions are incompatible")

    if row_mat1 | col_mat1 == 0:
        raise ValueError("The first matrix entered is not a matrix")

    if row_mat2 | col_mat2 == 0:
        raise ValueError("The second matrix entered is not a matrix")
    for row in mat1:
        for value in row:
            if type(value) != 'float' | 'int':
                raise ValueError("First matrix contains a non \
                    float or integer!")
    for row in mat2:
        for value in row:
            if type(value) != 'float' | 'int':
                raise ValueError("Second matrix contains a \
                    non float or integer!")