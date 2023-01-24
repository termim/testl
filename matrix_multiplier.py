import numpy as np

mat1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
mat2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

row1, col1 = np.shape(mat1)
row2, col2 = np.shape(mat2)

result = np.zeros((col1, row2))


print("Matrix 1 : ")
for i, row in enumerate(mat1):
    print(row)

print("Matrix 2 : ")
for i, row in enumerate(mat2):
    print(row)


def matrix_multiplier(mat1, mat2):
    row1, col1 = np.shape(mat1)
    row2, col2 = np.shape(mat2)

    # iterate through rows of mat1
    for i in range(len(mat1)):
        # iterate through cols of mat2
        for j in range(len(mat2[0])):
            # iterate through rows of mat2
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    print("Result : ")
    for row in result:
        print(row)


matrix_multiplier(mat1, mat2)

print("Checker : ")
result_np = np.matmul(mat1, mat2)
for row in result_np:
    print(row)
