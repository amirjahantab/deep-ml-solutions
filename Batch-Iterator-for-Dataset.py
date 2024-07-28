'''
Write a Python function to create a batch iterator for the samples in a numpy array X
and an optional numpy array y. The function should yield batches of a specified size. If y
is provided, the function should yield batches of (X, y) pairs; otherwise, it should yield
batches of X only.
'''

import numpy as np

def batch_iterator(X:np.ndarray, y=None, batch_size=64):
    """
    Create a batch iterator for samples in numpy array X and an optional numpy array y.
    
    Parameters:
    X (np.ndarray): Array of samples.
    y (np.ndarray, optional): Array of corresponding labels.
    batch_size (int): Size of each batch.
    
    Yields:
    tuple: Batches of (X, y) pairs if y is provided, otherwise batches of X.
    """

    # Get the total number of samples
    num_samples = X.shape[0]

    # Iterate over the dataset in steps of batch_size
    for start_idx in range(0, num_samples, batch_size):
        end_idx = start_idx + batch_size # min(start_idx + batch_size, num_samples)
        if y is not None:
            yield X[start_idx:end_idx], y[start_idx:end_idx]
        else:
            yield X[start_idx:end_idx]


X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
iterator = batch_iterator(X, y, batch_size)

for batch in iterator:
    print(batch)
