'''
Write a Python function that simulates a single neuron
with sigmoid activation, and implements backpropagation
to update the neuron's weights and bias. The function
should take a list of feature vectors, associated true binary labels,
initial weights, initial bias, a learning rate, and the number of epochs.
The function should update the weights and bias using
gradient descent based on the MSE loss, and return the
updated weights, bias, and a list of MSE values for each epoch,
each rounded to four decimal places.
'''

import numpy as np

def sigmoid(x):
    """Compute the sigmoid activation for the input x."""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(y):
    """Compute the derivative of the sigmoid function."""
    return y * (1 - y)

def mse_loss(y_true, y_pred):
    """Compute the Mean Squared Error loss."""
    return np.mean((y_true - y_pred) ** 2)

def forward_pass(features, weights, bias):
    """Perform the forward pass of the neuron."""
    z = np.dot(features, weights) + bias
    y_pred = sigmoid(z)
    return y_pred

def compute_gradients(features, labels, predictions):
    """Compute the gradients of the loss with respect to weights and bias."""
    dw = np.zeros_like(features[0], dtype=float)
    db = 0.0
    
    for x, y_true, y_pred in zip(features, labels, predictions):
        error = y_pred - y_true
        gradient = error * sigmoid_derivative(y_pred)
        dw += gradient * np.array(x, dtype=float)
        db += gradient

    dw /= len(features)
    db /= len(features)
    
    return dw, db

def update_parameters(weights, bias, dw, db, learning_rate):
    """Update weights and bias using the computed gradients."""
    weights -= learning_rate * dw
    bias -= learning_rate * db
    return weights, bias

def train_neuron(features, labels, initial_weights, initial_bias, learning_rate, epochs):
    """Train a single neuron with sigmoid activation using gradient descent."""
    features = np.array(features, dtype=float)
    weights = np.array(initial_weights, dtype=float)
    bias = initial_bias
    mse_values = []

    for epoch in range(epochs):
        predictions = forward_pass(features, weights, bias)
        loss = mse_loss(np.array(labels), np.array(predictions))
        mse_values.append(round(loss, 4))

        dw, db = compute_gradients(features, labels, predictions)
        weights, bias = update_parameters(weights, bias, dw, db, learning_rate)

    return weights.round(4), round(bias, 4), mse_values




print(train_neuron(np.array([[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]]), np.array([1, 0, 0]), np.array([0.1, -0.2]), 0.0, 0.1, 2))
print(train_neuron(np.array([[1, 2], [2, 3], [3, 1]]), np.array([1, 0, 1]), np.array([0.5, -0.2]), 0, 0.1, 3))