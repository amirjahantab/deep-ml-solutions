'''
Write a Python function that simulates a single neuron
with a sigmoid activation function for binary classification,
handling multidimensional input features.
The function should take a list of feature vectors
(each vector representing multiple features for an example),
associated true binary labels, and the neuron's weights
(one for each feature) and bias as input.
It should return the predicted probabilities after
sigmoid activation and the mean squared error between
the predicted probabilities and the true labels,
both rounded to four decimal places.
'''

import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    X = features
    Y = labels
    W = weights
    b = bias
    predictions = []
    for x in X:
        z = sum(w * x for w, x in zip(W, x)) + b
        prediction = 1 / (1 + math.exp(-z))
        predictions.append(round(prediction, 4))

    mse = sum((y - pred)**2 for y, pred in zip(Y, prediction))
    mse = round(mse, 4)
    return predictions, mse
