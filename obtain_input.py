def obtain_input_mat():
    Rows = int(input("Give the number of rows in matrix : "))
    Columns = int(input("Give the number of columns in matrix : "))
    matrix = []
    print("Please give the entries row-wise:")

    for val1 in range(Rows):
        r = []
        for val2 in range(Columns):
            r.append(int(input()))
        matrix.append(r)
    return matrix
