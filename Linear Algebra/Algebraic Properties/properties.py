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
