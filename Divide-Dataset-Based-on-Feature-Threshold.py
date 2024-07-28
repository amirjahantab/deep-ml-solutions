'''
Write a Python function to divide a dataset based on whether the value of a
specified feature is greater than or equal to a given threshold. The function
should return two subsets of the dataset: one with samples that meet the
condition and another with samples that do not.
'''

import numpy as np

def divide_dataset(X:np.ndarray, feature_i:int, threshold:float):
    """
    Divide a dataset based on whether the value of a specified feature
    is greater than or equal to a given threshold.
    
    Parameters:
    X : numpy.ndarray
        The input dataset, a 2D array where each row is a sample and each column is a feature.
    feature_i : int
        The index of the feature to be used for splitting the dataset.
    threshold : float
        The threshold value to split the dataset on.
    
    Returns:
    list of numpy.ndarray
        A list containing two numpy arrays: 
        - The first array with samples that meet the condition (feature value >= threshold)
        - The second array with samples that do not meet the condition (feature value < threshold)
    """
    # Ensure the feature index is within the correct range
    if feature_i < 0 or feature_i >= X.shape[1]:
        raise ValueError("feature_i is out of bounds.")
    
    # Split the dataset based on he threshotld
    condition_met = X[X[:, feature_i] >= threshold]
    condition_not_met = X[X[:, feature_i] < threshold]
    
    return [condition_met, condition_not_met]
