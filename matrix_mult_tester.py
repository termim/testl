import numpy as np
import pytest
import cProfile

a = [[1, 1, 1], [2, 2, 'A'], [1, 1, 1]]

b = [[1, 1, 1], [2, 2, 2], [1, 1, 1]]


def matrix_multiplier_tester(mat1, mat2):
    row_mat1, col_mat1 = np.shape(mat1)
    print(row_mat1, col_mat1)
    row_mat2, col_mat2 = np.shape(mat2)   
    print(row_mat2, col_mat2)     

    if col_mat1 != row_mat2:
        print("Matrix dimensions are incompatible")

    if (row_mat1 or col_mat1 == 0) == 1:
        print("The first matrix entered is not a matrix")

    if (row_mat2 or col_mat2 == 0) == 1:
        print("The second matrix entered is not a matrix")  
    for row in mat1:
        for value in row:
            if not isinstance(value, int):
                print("First matrix contains a non \
                    float or integer!")
    for row in mat2:
        for value in row:
            if not isinstance(value, int):
                print("Second matrix contains a non \
                    float or integer!")
    for row in mat1:
        if not isinstance(row, list):
            print("First matrix contains a non \
                    float or integer!")
    for row in mat2:
        if not isinstance(row, list):
            print("Second matrix contains a non \
                    float or integer!")


def main():
    matrix_multiplier_tester(a, b)


if __name__ == '__main__':
    #cProfile.run('main()')
    matrix_multiplier_tester(a, b)