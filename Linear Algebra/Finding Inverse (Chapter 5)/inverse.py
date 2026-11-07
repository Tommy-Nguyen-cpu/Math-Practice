import numpy as np
from enum import Enum

class ElementaryOperationEnum(Enum):
    ROW_SWAP = 1
    ROW_MULTIPLY = 2
    ROW_ADD = 3

# Stores the elementary row operations and the row indices involved in the operation.
class ElementaryRowOperation:
    def __init__(self, operation_type, row1, row2=None, scalar=None):
        self.operation_type = operation_type
        self.row1 = row1
        self.row2 = row2
        self.scalar = scalar

    # Debug message to see what operation is being performed.
    def __repr__(self):
        if self.operation_type == ElementaryOperationEnum.ROW_SWAP:
            return f"Swap Row {self.row1} with Row {self.row2}"
        elif self.operation_type == ElementaryOperationEnum.ROW_MULTIPLY:
            return f"Multiply Row {self.row1} by {self.scalar}"
        elif self.operation_type == ElementaryOperationEnum.ROW_ADD:
            return f"Add {self.scalar} * Row {self.row2} to Row {self.row1}"

def perform_row_operations(matrix, i, j):
    elementary_operations = []

    unknowns = matrix[:, :-1]
    # print(unknowns)
    non_zero_unknowns = np.count_nonzero(unknowns, axis = 1) # Count all non-zeroes unknowns in each row.
    # print(non_zero_unknowns)

    zero_rows = np.argwhere(non_zero_unknowns == 0) # Find all instance in which the row only has only 0s
    if len(zero_rows) > 0:
        raise ValueError("The matrix has infinite solutions or no solution. Please check the matrix and try again.")

    # If the current element in the current row has a 0, see if we can row swap with another row.
    if matrix[i][i] == 0.0:
        column = matrix[:, i] # grab all values in the current column.
        # print(column)
        non_zero_columns = column[column != 0] # grab all non-zero values in the current column.
        # print(non_zero_columns)

        # A matrix with a column of all zeroes indicates that the system of equations cannot be solved.
        if len(non_zero_columns) == 0:
            raise ValueError(f"Invalid matrix! All unknowns at column {i} is 0.")

        first_non_zero_index = np.argwhere(column != 0).flatten()[0] # Find the first row with a non-zero value.
        # print(first_non_zero_index)

        # Just for safety, check if there are any values in the column. If there are, we can perform a row swap to bring a non-zero value to the current row.
        if len(column) != 0:
            # Row swap.
            print(f"Swapping rows {matrix[i]} and {matrix[first_non_zero_index]}")
            temp = matrix[i].copy() # Store the current row in a temporary variable.
            matrix[i] = matrix[first_non_zero_index]
            matrix[first_non_zero_index] = temp
            elementary_operations.append(ElementaryRowOperation(ElementaryOperationEnum.ROW_SWAP, i, first_non_zero_index))
            
            # We return because we just row swapped. No other operations should be performed on this row until the next iteration of the loop.
            return elementary_operations

    factor = -1 * matrix[j][i] / matrix[i][i] # Calculate the factor to eliminate the current element in the current row.
    print(f"Calculating factor: -1 * {matrix[j][i]} / {matrix[i][i]} = {factor}")
    result = matrix[i] * factor + matrix[j] # Perform the row operation to eliminate the current element in the current row.
    print(f"Performing row operation: {matrix[i]} * {factor} + {matrix[j]} = {result}")
    matrix[j] = result # Update the current row with the result of the row operation.
    elementary_operations.append(ElementaryRowOperation(ElementaryOperationEnum.ROW_ADD, j, i, factor))

    if matrix[i][i] != 1.0: # Elements at indices i and i are diagonal elements. If the diagonal element is not 1 (i.e., leading 1s), then we need to reduce them to 1 in order to get matrix into reduced row echelon form.
        scalar = 1 / matrix[i][i] # Calculate the scalar to reduce the diagonal element to 1.
        print(f"Calculating scalar: 1 / {matrix[i][i]} = {scalar}")
        result = matrix[i] * scalar # Perform the row operation to reduce the diagonal element to
        matrix[i] = result # Update the current row with the result of the row operation.
        elementary_operations.append(ElementaryRowOperation(ElementaryOperationEnum.ROW_MULTIPLY, i, scalar=scalar))

    return elementary_operations
        
def solve_linear_equations(matrix):
    # Solve from top to bottom, left to right.
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            perform_row_operations(matrix, i, j)
            print(f"Matrix after operation: {matrix}\n")
    # Solve from bottom to top, left to right.
    for i in range(len(matrix) -1, -1, -1):
        for j in range(0, i):
            perform_row_operations(matrix, i, j)
            print(f"Matrix after operation: {matrix}\n")

def get_elementary_operations(matrixA):
    solve_linear_equations(matrixA)
    return matrixA

def finding_inverse(matrixA):
    return matrixA

solve_linear_equations(
    np.array([[1, 5, 4, 5],
     [2, -2, 4, 10],
     [0, 0, 1, 15]], dtype=np.float16))
# perform_row_operations(
#     np.array([[0, 5, 4, 5],
#      [2, -2, 4, 10],
#      [0, 0, 1, 15]], dtype=np.float16), 0, 1
# )