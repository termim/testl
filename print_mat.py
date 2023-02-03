def print_mat(a):
    row_a = len(a)
    col_a = len(a[0])
    print('\n')
    for row in range(row_a):
        for col in range(col_a):
            print(a[row_a][col_a], end=" ")
        print()
    print("\n")
