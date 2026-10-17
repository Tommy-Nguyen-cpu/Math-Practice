import numpy as np

def perform_row_operations(matrix, i, j):
    unknowns = matrix[:, :-1]
    print(unknowns)

def solve_linear_equations(matrix):
    # Solve from top to bottom, left to right.
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            perform_row_operations(matrix, i, j)
    # Solve from bottom to top, left to right.
    for i in range(len(matrix) -1, -1, -1):
        for j in range(0, i):
            perform_row_operations(matrix, i, j)

def get_elementary_operations(matrixA):
    solve_linear_equations(matrixA)
    return matrixA

def finding_inverse(matrixA):
    return matrixA

perform_row_operations(
    np.array([[4, 5, 4, 5],
     [2, -2, 4, 10],
     [3, 3, 6, 15]], dtype=np.float16), 0, 0
)