'''
Write a Python function that performs linear regression using gradient descent.
The function should take NumPy arrays X (features with a column of ones for the intercept)
and y (target) as input, along with learning rate alpha and the number of iterations,
and return the coefficients of the linear regression model as a NumPy array.
Round your answer to four decimal places. -0.0 is a valid result for rounding a very small number.
'''

import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    # Number of training examples
    m = len(y)
    
    # Initialize coefficients (theta) to zeros
    theta = np.zeros(X.shape[1])
    
    # Gradient descent algorithm
    for _ in range(iterations):
        # Compute the predictions
        predictions = X.dot(theta)
        
        # Compute the error
        error = predictions - y
        
        # Compute the gradient
        gradient = (1/m) * X.T.dot(error)
        
        # Update the coefficients
        theta -= alpha * gradient
    
    # Round the coefficients to four decimal places
    theta = np.round(theta, 4)
    
    return theta
