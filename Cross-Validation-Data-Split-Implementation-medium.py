'''
Write a Python function that performs k-fold cross-validation data splitting from
scratch. The function should take a dataset (as a 2D NumPy array where each row
represents a data sample and each column represents a feature) and an integer k
representing the number of folds. The function should split the dataset into k
parts, systematically use one part as the test set and the remaining as the training
set, and return a list where each element is a tuple containing the training set and
test set for each fold.
'''

import numpy as np

def cross_validation_split(dataset, k):
    # Shuffle the dataset to ensure randomness
    np.random.shuffle(dataset)
    
    # Split dataset into k folds
    folds = np.array_split(dataset, k)
    
    # Create the list to store the training and test sets for each fold
    cross_val_sets = []
    
    # Perform k-fold cross-validation
    for i in range(k):
        # Create the test set for the current fold
        test_set = folds[i]
        
        # Create the training set by combining all other folds
        train_set = np.concatenate([folds[j] for j in range(k) if j != i])
        
        # Append the (train_set, test_set) tuple to the result list
        cross_val_sets.append((train_set.tolist(), test_set.tolist()))
    
    return cross_val_sets


data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
k = 4

splits = cross_validation_split(data, k)
for i, (train, test) in enumerate(splits):
    print(f"Fold {i+1}")
    print("Train Set:\n", train)
    print("Test Set:\n", test)
     

