'''
Write a Python function that uses the Jacobi method
to solve a system of linear equations given by Ax = b.
The function should iterate 10 times,
rounding each intermediate solution to four decimal places,
and return the approximate solution x.
'''

# import numpy as np
import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:

    iterations = n    
    # Initial guess (zeros)
    x = [0 for _ in range(len(b))]

    # Iterative process
    for _ in range(iterations):
        x_new = [0 for _ in range(len(b))]
        for i in range(len(b)):
            s = sum(A[i][j] * x[j] for j in range(len(b)) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        
        # Rounding to four decimal places
        x = x_new
        
    return x

A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]]
b = [-1, 2, 3]
n=2
print(solve_jacobi(A, b, n))