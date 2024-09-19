'''
Write a Python function that implements the Rectified Linear Unit (ReLU)
activation function. The function should take a single float as input and return
the value after applying the ReLU function. The ReLU function returns the input
if it's greater than 0, otherwise, it returns 0.
'''

def relu(z: float) -> float:
	return max(0, z)

