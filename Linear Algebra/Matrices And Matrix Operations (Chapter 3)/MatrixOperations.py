# Will focus on manually creating the matrix operations for education purposes. Numpy is a powerful library for numerical operations and can perform matrix operations efficiently, but will avoid using it here to understand the underlying principles better.

def verify_shape(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    return True

def matrix_addition(matrix1, matrix2):
    if verify_shape(matrix1, matrix2):
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[i])):
                row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)
        return result

def matrix_suptraction(matrix1, matrix2):
    if verify_shape(matrix1, matrix2):
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[i])):
                row.append(matrix1[i][j] - matrix2[i][j])
            result.append(row)
        return result

def matrix_scalar_multiplication(matrix, scalar):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range (len(matrix[i])):
            row.append(matrix[i][j] * scalar)
        result.append(row)
    return result

def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[1]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")
    result = []
    for i in range(len(matrix1)): # Iterate through rows of matrix1
        row = []
        for j in range(len(matrix2[0])): # Iterate through column of matrix2, so we have access to elements in the same column.
            sum_product = 0
            for k in range(len(matrix2)): # Iterate through row of matrix2, so we can get the elements in the same column in each row.
                sum_product += matrix1[i][k] * matrix2[k][j] # Inner dimension of matrix1 and row of matrix2 must match, so k will always be in range.
            row.append(sum_product)
        result.append(row)

    return result

def matrix_trace(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square for trace calculation.")
    
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    return trace

def matrix_transpose(matrix):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[j][i]) # swap the indices to transpose.
        result.append(row)
    return result

mat1 = [[1, 2, 3], 
        [3, 4, 1]]
mat2 = [[5, 6], 
        [7, 8],
        [9, 10]]
print(f"Matrix Operations: {matrix_multiplication(mat1, mat2)}")