'''
Write a Python function to perform a random shuffle of the samples in two numpy
arrays, X and y, while maintaining the corresponding order between them. The function
should have an optional seed parameter for reproducibility.
'''

import numpy as np

def shuffle_data(X, y, seed=None):
    # Set the seed if provided
    if seed is not None:
        np.random.seed(seed)

    # Generate a permutation of indices
    permutation = np.random.permutation(len(X))

    # Shuffle the arrays using the permutation
    X_shuffled = X[permutation]
    y_shuffled = y[permutation]
    
    return X_shuffled, y_shuffled