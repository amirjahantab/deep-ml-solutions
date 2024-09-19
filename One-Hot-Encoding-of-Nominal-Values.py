'''
Write a Python function to perform one-hot encoding of nominal
values. The function should take in a ID numpy array x of integer values
and an optional integer n_col representing the number of columns for
the one-hot encoded array. If n_col is not provided, it should be
automatically determined from the input array.
'''

import numpy as np

def to_categorical(x, n_col=None):
    '''
    Converting a 1D array of integers to one-hat encoded 2D array

    Parametrs:
        x (np.array): 1D numpy array of integer values to be one-hot encoded.
        n_col (int, optional): Number of columns for the one-hot encoded array. 
                           If not provided, it is determined from the input array.

    Return:
        np.ndarray: 2D numpy array with one-hot encoded representation of `x`.
    '''

    # if n_col is not provided, calculate it as number of unique values in x
    if n_col is None:
        n_col = len(np.unique(x))

    # define the shape of one-hat encoded array
    shape = (len(x), n_col)

    # initialize a 2D array of zeros with the specified shape
    one_hat = np.zeros(shape)

    # fill the one-hat encoder array
    for i in range(one_hat.shape[0]):
        one_hat[i, x[i]] = 1

    return one_hat

x = np.array([0, 1, 2, 1, 0])
output = to_categorical(x)
print(output)

    