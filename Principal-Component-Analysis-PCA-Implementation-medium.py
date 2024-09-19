'''
Write a Python function that performs Principal Component Analysis (PCA) from
scratch. The function should take a 2D NumPy array as input, where each row
represents a data sample and each column represents a feature. The function
should standardize the dataset, compute the covariance matrix, find the
eigenvalues and eigenvectors, and return the principal components (the
eigenvectors corresponding to the largest eigenvalues). The function should also
take an integer k as input, representing the number of principal components to
return.
'''

import numpy as np 

def pca(data: np.ndarray, k: int) -> list[list[int|float]]:
    mu = data.mean(axis=0)
    std = np.std(data, axis=0)
    X_norm = (data - mu) / std
    m = data.shape[0]
    covariance_matrix = (X_norm.T @ X_norm) / (m-1)

    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    

    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors_sorted = eigenvectors[:,idx]

    return eigenvectors_sorted[:, :k]

