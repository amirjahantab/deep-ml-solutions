'''
Write a Python function to calculate the accuracy score of a model's
predictions. The function should take in two ID numpy arrays: y_true, which
contains the true labels, and y_pred, which contains the predicted labels. It
should return the accuracy score as a float.
'''

import numpy as np

def accuracy_score(y_true, y_pred):
    return sum(y_true==y_pred) / len(y_true)
