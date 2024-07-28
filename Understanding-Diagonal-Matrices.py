'''
Write a Python function to convert a ID numpy array into a diagonal matrix.
The function should take in a ID numpy array x and return a 2D numpy array
representing the diagonal matrix.
'''

import numpy as np

def make_diagonal(x):
    '''
    Converts a 1D numpy array into a diagonal matrix.

    Parameters:
        x (np.array): 1D numpy array to be converted into a diagonal matrix.

    Returns:
        np.array: 2D numpy array representing the diagonal matrix.
    '''

    # Define the shape of the diagonal matrix
    shape = (len(x), len(x))

    # Initialize a 2D array of zeros with the specified shape
    diagonal_matrix = np.zeros(shape)

    # Populate the diagonal of the matrix with the values from the input array
    for i in range(diagonal_matrix.shape[0]):
        diagonal_matrix[i, i] = x[i]

    return diagonal_matrix
