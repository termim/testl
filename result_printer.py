import numpy as np


def res_print(result):
    row_res, col_res = np.shape(result)
    print('\n')
    print("Result")
    for row in range(row_res):
        for col in range(col_res):
            print(result[row][col], end=" ") 
        print()  
    print("\n")

