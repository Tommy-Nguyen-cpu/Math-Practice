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
        