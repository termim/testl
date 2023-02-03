a = [[1, 1, 1], [2, 2, 'A'], [1, 1, 1]]


b = [[1, 1, 1], [2, 2, 2], [1, 1, 1]]


def matrix_multiplier_tester(mat):

    for row in mat:
        for value in row:
            if not isinstance(value, int):
                print("First matrix contains a non \
                    float or integer!")
    for row in mat:
        if not isinstance(row, list):
            print("First matrix contains a non \
                    float or integer!")
