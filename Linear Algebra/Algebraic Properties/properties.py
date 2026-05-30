import numpy as np
def find_inverse(matrixA):
    if(len(matrixA) != 2 and len(matrixA[0]) != 2):
        raise ValueError("Matrix is not a 2x2 matrix. Generalized inverse calculation will be implemented in later chapters.")
    print("Step 1: Calculating determinant...")
    # det = ad - bc
    a, b, c, d = matrixA[0][0], matrixA[0][1], matrixA[1][0], matrixA[1][1]
    det = a*d - b*c

    print(f"Determinant: {det}")
    print("Step 2: Validating determinant...")
    if(det == 0):
        raise ValueError("Matrix is singular and does not have an inverse.")
    
    print("Step 3: Calculating factor...")
    factor = 1/det

    print(f"Factor: {factor}")

    print("Step 4: Calculating inverse matrix...")
    altered_matrix = np.array([[d, -b], [-c, a]])
    print(f"Altered matrix (before multiplying by factor):\n {altered_matrix}")

    inverse_matrix = factor * altered_matrix
    return inverse_matrix

print(find_inverse(np.array([[4, 7], [2, 6]])))

def verify_inverse(matrixA, inverse_matrix):
    identity_matrix = np.zeros((len(matrixA), len(inverse_matrix[0])))
    for i in range(len(matrixA)): # Column of OG matrix.
        sum_val = 0
        for j in range(len(inverse_matrix[0])): # Row of inverse matrix.
            sum_val += matrixA[i][j] * inverse_matrix[j][i]
        identity_matrix[i][i] = sum_val

    print(f"Manual: Product of original matrix and its inverse:\n {identity_matrix}")

def verify_inverse_numpy(matrixA, inverse_matrix):
    identity_matrix = np.dot(matrixA, inverse_matrix)
    print(f"NumPy: Product of original matrix and its inverse:\n {identity_matrix}")

def verify_product_of_transpose(matrixA, matrixB):
    product = np.dot(matrixA, matrixB)
    transposed_product = np.transpose(product)

    transposed_A = np.transpose(matrixA)
    transposed_B = np.transpose(matrixB)
    product_of_transposes = np.dot(transposed_B, transposed_A)

    print(f"Transposed Product:\n {transposed_product}")
    print(f"Product of transposes:\n {product_of_transposes}")

def matrix_multiply(matrixA, matrixB):
    result = np.zeros((len(matrixA), len(matrixB[0])))
    for i in range(len(matrixA)):
        sum_val = 0
        for j in range(len(matrixB[0])):
            sum_val += matrixA[i][j] * matrixB[j][i]
        result[i][i] = sum_val
    return result

def verify_product_of_inverse(matrixA, matrixB):
    inverseA = find_inverse(matrixA)
    inverseB = find_inverse(matrixB)

    product_of_inverses = matrix_multiply(inverseA, inverseB)
    inverse_of_product = matrix_multiply(product_of_inverses, matrix_multiply(matrixA, matrixB))
    inverse_of_product_non_inverse_first = matrix_multiply(matrix_multiply(matrixA, matrixB), product_of_inverses)
    print(f"Inverse of product:\n {inverse_of_product}")
    print(f"Inverse of product (non-inverse first):\n {inverse_of_product_non_inverse_first}")

def verify_inverse_of_transpose_property(matrixA):
    transpose = np.transpose(matrixA)
    inverse_of_transpose = find_inverse(transpose)

    inverse  = find_inverse(matrixA)
    transpose_of_inverse = np.transpose(inverse)

    print(f"Inverse of transpose:\n {inverse_of_transpose}")
    print(f"Transpose of inverse:\n {transpose_of_inverse}")

inverse = find_inverse(np.array([[4, 7], [2, 6]]))
verify_inverse_numpy(np.array([[4, 7], [2, 6]]), inverse)
verify_inverse(np.array([[4, 7], [2, 6]]), inverse)
verify_product_of_transpose(np.array([[4, 7], [2, 6]]), np.array([[1, 2], [3, 4]]))
verify_product_of_inverse(np.array([[4, 7], [2, 6]]), np.array([[1, 2], [3, 4]]))
verify_inverse_of_transpose_property(np.array([[4, 7], [2, 6]]))