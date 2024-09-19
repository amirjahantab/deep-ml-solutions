'''
In machine learning and statistics, the softmax function is a
generalization of the logistic function that converts a vector of scores
into probabilities. The log-softmax function is the logarithm of the
softmax function, and it is often used for numerical stability when
computing the softmax of large numbers. Given a ID numpy array of
scores, implement a Python function to compute the log-softmax of the
array.
'''
import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	scores = np.array(scores, dtype=('float64'))
	scores -= max(scores) 
	scores -= np.log(sum(np.exp(scores)))
	return scores
	

A = np.array([1, 2, 3])
print(log_softmax(A))