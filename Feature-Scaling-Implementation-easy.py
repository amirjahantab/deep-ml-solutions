'''
Write a Python function that performs feature scaling on a dataset using both
standardization and min-max normalization.
The function should take a 2D NumPy array as input,
where each row represents a data sample and each column represents a feature.
It should return two 2D NumPy arrays: one scaled by standardization and one by min-max normalization.
Make sure all results are rounded to the nearest 4th decimal.
'''

import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    standardized_data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
    normalized_data = ((data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0)))
    return standardized_data, normalized_data