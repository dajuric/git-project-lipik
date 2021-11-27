def unitMatrix(N):

    #return [[0] * N for _ in range(N)]

    rows = []
    for r in range(N):
        rows.append([0] * N)
        rows[r][r] = 1

    return rows

import numpy as np
def unitMatrixNumpy(N):
    return np.identity(N)

def printMatrix(mat):
    for r in mat:
        print(r)

import math
def niceMatrix(arr):
    N = int(math.sqrt(len(arr)))

    for i in range(N):
        for j in range(N):
            print(arr[i * N + j], end=" ")
        print()

printMatrix(unitMatrix(5))
niceMatrix([1, 2, 3, 4, 5, 6, 7, 8, 9])