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
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def train_neuron(feature_vectors, labels, weights, bias, learning_rate, epochs):
    mse_values = []
    
    for epoch in range(epochs):
        mse_epoch = 0
        
        for features, label in zip(feature_vectors, labels):
            # Forward pass
            z = np.dot(features, weights) + bias
            pred = sigmoid(z)
            
            # Compute the error
            error = label - pred
            mse_epoch += error ** 2
            
            # Backward pass (Gradient computation)
            d_error = -2 * error
            d_pred = sigmoid_derivative(z)
            d_weights = features * d_error * d_pred
            d_bias = d_error * d_pred
            
            # Update weights and bias
            weights -= learning_rate * d_weights
            bias -= learning_rate * d_bias
        
        # Calculate and store the MSE for the epoch
        mse_epoch /= len(feature_vectors)
        mse_values.append(round(mse_epoch, 4))
    
    return weights, bias, mse_values


print(train_neuron(np.array([[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]]), np.array([1, 0, 0]), np.array([0.1, -0.2]), 0.0, 0.1, 2))