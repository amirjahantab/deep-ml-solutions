'''
Write a Python function that computes the softmax activation
for a given list of scores.
The function should return the softmax values as a list, each rounded to four decimal places.
'''

import math

def softmax(scores: list[float]) -> list[float]:
    # Compute exponentials of all scores
    exp_scores = [math.exp(score) for score in scores] 
    
    # Sum of all exponentials
    sum_exp_scores = sum(exp_scores)  

    # Compute softmax function
    _softmax = lambda exp_score: round(exp_score / sum_exp_scores, 4)
    softmax_scores = [_softmax(exp_score) for exp_score in exp_scores]  # Compute softmax and round
    return softmax_scores

scores = [1, 2, 3]
print(softmax(scores))