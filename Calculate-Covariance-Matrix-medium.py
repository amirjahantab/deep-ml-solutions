'''
Write a Python function that calculates the
covariance matrix from a list of vectors.
Assume that the input list represents a dataset
where each vector is a feature, and vectors are of equal length.
'''


import numpy as np

def calculate_covariance_matrix(data):

    # Convert the list of vectors to a numpy array
    data = np.array(data)
    
    # Number of observations
    num_observations = data.shape[1]
    
    # Center the data by subtracting the mean of each feature
    mean_centered_data = data - np.mean(data, axis=1, keepdims=True)
    
    # Calculate the covariance matrix
    covariance_matrix = np.dot(mean_centered_data, mean_centered_data.T) / (num_observations - 1)
    
    return covariance_matrix
