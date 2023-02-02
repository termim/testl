import numpy as np


def obtain_input():
    # Matrix 1 input
    Rows1 = int(input("Give the number of rows in matrix 1:"))
    Columns1 = int(input("Give the number of columns in matrix 1:"))

    # Initializing the matrix
    matrix1 = []
    print("Please give the entries row-wise:")

    # For user input
    for val1 in range(Rows1):  # This for loop is to arrange rows
        r = []
        for val2 in range(Columns1):  # This for loop is to arrange columns
            r.append(int(input()))
        matrix1.append(r)

    # Matrix 2 input
    Rows2 = int(input("Give the number of rows in matrix 2:"))
    Columns2 = int(input("Give the number of columns in matrix 2:"))

    # Initializing the matrix
    matrix2 = []
    print("Please give the entries row-wise:")

    # For user input
    for val3 in range(Rows2):  # This for loop is to arrange rows
        s = []
        for val4 in range(Columns2):  # This for loop is to arrange columns
            s.append(int(input()))
        matrix2.append(s)        
    return matrix1, matrix2


def print_matricies(a, b):
    row1, col1 = np.shape(a)
    row2, col2 = np.shape(b)
    # matrix 1
    print('\n')
    print("Matrix 1")
    for row_1 in range(row1):
        for col_1 in range(col1):
            print(a[row_1][col_1], end=" ") 
        print()  
    print("\n")
    # matrix 2
    print("Matrix 2")
    for row_2 in range(row2):
        for col_2 in range(col2):
            print(b[row_2][col_2], end=" ")
        print()
    print("\n")
