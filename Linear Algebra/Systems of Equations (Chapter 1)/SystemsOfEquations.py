import numpy as np
def definingSystemsOfEquations():
    constants = np.random.randn(10) # Constants do not change.
    variables = np.random.randn(10) # Assume that "variables" is changing (i.e., not fixed).

    # Linear equations can be defined as equations containing variables and constants.
    # These variables and constants are used to find some value "b".
    b = np.dot(constants, variables) # Where ".dot" is the multiplication between values in "constants" with values in "variables", whose results are then summed up.

    # EX: b = 10x + 20y + 30z + ...
    x, y, z = 20, 10, 15 # Assume x, y, and z are changing (or will be changed in the future)
    b = 10*x + 20*y + 30*z

    # A "homogeneous equation" is an equation where "b" = 0. In other orders, where the dot product between "constants" and "variables" is 0.
    # Note that equations containing powers, square roots, etc in variables are NOT linear equations...because they perform complex operations that are not linear, obviously! :)

    # While we're on the topic of definitions, let's go over a few brief ones:
        # 1. Finite set of linear equations is called: "system of linear equations" or "linear system"
        # 2. Variables are called "unknowns" (because they're unknown, duh :) ).
            # For example, all values within "variables" would be called "unknown" because we don't know the actual values to solve for "b" just yet.
        # 3. A set of known values for variables, that, when plugged into our system of equations and solves for "b" is called a "solution" (because plugging in those values "solves" our problem).
            # Instead of writing out our solution as x = 1, y = 2, ..., we can write it as (1, 2, ...), basically omitting the variables.
                # This way of writing the solution is called an "ordered n-tuple".
                # Any solution with only 2 values (i.e., (1, 2), ...) is called an "ordered pair".
                # Any solution with only 3 values (i.e., (1, 2, 3), ...) is called an "ordered triple". 
        # 4. Any solution to our problem defines a point of intersection (i.e., where the equations meet/arrive at the same answer).
            # There are 3 possible solutions:
                # 1. They meet at exactly 1 point.
                # 2. They are parallel and as such, do not intersect at all.
                # 3. They are the same line, as such they have infinite intersections.
        # 5. Consistent - a system of linear equation is said to be consistent if it has atleast 1 solution.
        # 6. Inconsistent - a system of linear equation is said to be inconsistent if it has NO solution.
        # 7. These definitions can be extended to ALL linear systems of equations: they all can have 0, 1, or infinitely many solutions. There are no other options.

    # EX: Given the following equations 10x + 20y = 4 and 30x + 40y = 7, find x and y coordinates.
    equations = np.array(
        [[10, 20],
            [30, 40]]
    )

    constants = np.array([4, 7])

    row1 = equations[0]
    row2 = equations[1]

    factor = -row2[0] / row1[0] # Grab factor, which is -3

    row_new = row1 * factor + row2 # (10x + 20y) * -3 + (30x + 40y) = -20y
    b_new = constants[0] * factor + constants[1] # 4 * -3 + 7 = -5
    y = b_new / row_new[1] # -5 / -20 = y
    x = (constants[0] - row1[1] * y) / row1[0] # (4 - 20 * (5/20)) / 10 = x

    # Notice how we are able to come to a single solution. There are some cases where there are infinitely many solutions.
    # In this case, we can solve for any of the variables, and assign an arbitrary value "t", "r", etc (also called a PARAMETER) to other unsolved variables.
    # Basically, these other variables can have any value, as long as it solves the system of equations.
    # For example:
    # x + 2y = 2
    # 2x + 4y = 4 <- Notice how the second equation is literally just the first equation multiplied by 2. This means that the second equation holds no value and can be omitted.
    # Would be an infinitely many solutions, and can be rewritten as a single equation:
    # x = 2 - 2t, y = t <- if we solve for x.
    # y = 1 - (1/2)t, x = t <- if we solve for y
    # If we went with equation 1 (solving for x) and plugged in t = 1, our solution would be:
    # (0, 1) = (x, y)

    # Now things can be a bit cooler:
    # Now that we know the fundamentals, we can start representing these equations as matrices!
    # Why?
    # As more variables and equations are introduced, it becomes computationally expensive to keep track of every individual operations, numbers, etc.
    # Instead, we can maintain a matrix that excludes operations and variable names.
    '''
    [
    [20 30 40 6]
    [10 30 20 1]
    ...
    ]
    '''
    # The example matrix above may represent a large linear system of equations.
    # 20, 30, 40, and 6 would represent: 20x + 30y + 40z = 6.
    # This type of matrix is called an "AUGMENTED MATRIX".
    # For augmented matrices, we solve the system of linear equations through operations on the rows.

def solve_linear_equations(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            perform_row_operations(matrix, i, j)
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(0, i):
            perform_row_operations(matrix, i, j)

    print(matrix)

def perform_row_operations(matrix, i, j):
    # Check for infinite or zero solutions.
    unknowns = matrix[:, :-1]

    non_zero_unknowns = np.count_nonzero(unknowns, axis = 1) # Count all non-zeroes unknowns in each row.

    no_nonzero = np.argwhere(non_zero_unknowns == 0) # Find all instance in which the row only has no non_zero
    if len(no_nonzero) > 0:
        raise Exception("INFINITE or ZERO SOLUTIONS.")
    
    # Perform Row swap if applicable.
    if matrix[i][i] == 0.0:
        columns = matrix[:, i]
        non_zero_columns = columns[columns != 0]
        if len(non_zero_columns) == 0:
            raise Exception(f"Invalid matrix! All unknowns at column {i} is 0.")
        first_non_zero = (columns != 0).argmax()
        if len(columns) != 0:
            temp = np.array(matrix[i])
            print(f"Swap rows {temp} and {matrix[first_non_zero]}")
            matrix[i] = matrix[first_non_zero]
            matrix[first_non_zero] = temp

            perform_row_operations(matrix, i, j)
            return
    
    # Perform row based operations (Multiplication and addition/subtraction).
    factor = -1 * matrix[j][i] / matrix[i][i]
    if factor == 0.0: return
    print(f"step 1, calculate factor: -1 * {matrix[j][i]} / {matrix[i][i]}")
    matrix[j] = matrix[j] + matrix[i] * factor
    print(f"step 2, calculate new row: {matrix[j]} + {matrix[i]} * {factor}")
    print(matrix)
    print()
solve_linear_equations(
    np.array([[1, -1, 2, 5],
     [2, -2, 4, 10],
     [3, -3, 6, 15]], dtype=np.float16)
)