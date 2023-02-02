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

    # Printing the matrix given by user
    print("\n Matrix 1")
    for val1 in range(Rows1):
        for val2 in range(Columns1):
            print(matrix1[val1][val2], end=" ")
        print()

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
   
    # Printing the matrix given by user
    print("\n Matrix 2")
    for _ in range(Rows2):
        for __ in range(Columns2):
            print(matrix2[val3][val4], end=" ")
        print()
          
    return matrix1, matrix2