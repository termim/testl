import numpy as np
import tracemalloc
import cProfile

tracemalloc.start()

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


snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

#print("[ Top 10 ]")
#for stat in top_stats[:10]:
#    print(stat)


def main():
    matrix_multiplier(mat1, mat2)


if __name__ == '__main__':
    cProfile.run('main()')

    
