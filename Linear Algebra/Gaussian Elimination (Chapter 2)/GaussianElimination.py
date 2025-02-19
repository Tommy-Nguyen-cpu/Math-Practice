import numpy as np
def perform_row_operation(matrix, curr_row_idx, next_row_idx):
    unknowns = matrix[:, :-1] # Grab all unknowns while avoiding the constants (right most column).
    non_zero_rows = np.count_nonzero(unknowns, axis = 1) # Count number of non-zeroes in each row.
    zero_rows = np.argwhere(non_zero_rows == 0) # Find all rows that only contain 0s.
    if len(zero_rows) > 0:
        print(zero_rows)
        raise Exception("INFINITE SOLUTION OR NO SOLUTION FOUND!")
    
    # If the leading variable is 0, we will have to swap rows.
    if matrix[curr_row_idx][curr_row_idx] == 0:
        columns = matrix[:, curr_row_idx] # Grab the column containing the current rows leading variable.
        non_zero_cells = columns[columns != 0] # Check to make sure we have at least 1 non-zero leading variable in this column.
        if len(non_zero_cells) == 0:
            raise Exception(f"INVALID MATRIX! ALL VALUES IN COLUMN {curr_row_idx} ARE ALL 0s!")
        
        leading_var_idx = (columns != 0).argmax() # Grab the index containing a non-zero leading variable.
        # Perform row swap.
        temp = np.array(matrix[curr_row_idx]) # Create new numpy array so temp isn't overridden.
        print(f"Swapping rows {temp} and {matrix[leading_var_idx]}")
        matrix[curr_row_idx] = matrix[leading_var_idx]
        matrix[leading_var_idx] = temp
        
        perform_row_operation(matrix, curr_row_idx, next_row_idx) # Call the function again so we can perform other operations.
        return
    
    factor = -1 * (matrix[next_row_idx][curr_row_idx] / matrix[curr_row_idx][curr_row_idx])

    if factor == 0.0: return # Factor is 0 in situations where we already simplified the row.

    print(f"Factor calculated: -1 * ({matrix[next_row_idx][curr_row_idx]} / {matrix[curr_row_idx][next_row_idx]})")
    matrix[next_row_idx] += factor * matrix[curr_row_idx]
    print(f"Resulting row from row operation: {matrix[next_row_idx]}")
    print(matrix)
    return

def gaussian_elimination(matrix):
    num_rows = matrix.shape[0]
    num_cols = matrix.shape[1] - 1 # Subtracting one to avoid the constants.
    if num_cols > num_rows:
        raise Exception("There are more unknowns than there are equations, meaning this is likely an infinite solution scenario!")

    # Forward phase
    for curr in range(len(matrix)):
        for next in range(curr + 1, len(matrix)):
            perform_row_operation(matrix, curr, next)

    unknowns = np.ones(num_cols, dtype=np.float32) # Will hold our solutions.
    curr_col_idx = num_cols - 1
    for curr_row_idx in range(len(matrix)-1, -1, -1):
      curr_row = matrix[curr_row_idx][:-1] # Grab the current row, excluding the last column.
      print(f"row: {matrix[curr_row_idx]}, unknown: {unknowns}")
      curr_row *= unknowns # Plug in our solutions into the current row.
      added_constants = np.sum(curr_row[curr_col_idx + 1:]) # Calculate the sum of all solved unknowns.
      print(f"sum: {added_constants}")
      curr_cell = matrix[curr_row_idx][curr_col_idx] # Grab the current unknown in the matrix.
      solution = (matrix[curr_row_idx][-1] + -1 * added_constants) / curr_cell # Solve for the unknown
      print(f"Solving for unknown: ({matrix[curr_row_idx][-1]} + {-1 * added_constants}) / {curr_cell} = {solution}")
      unknowns[curr_col_idx] = solution # Place our solution into our numpy array.
      curr_col_idx -= 1
    print(f"Our solution set is: {unknowns}")

gaussian_elimination(np.array([[1, 4, 2, 9],
     [10, 4, -3, 1],
      [3, 6, -5, 0]], dtype=np.float16))