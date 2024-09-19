'''
Write a Python function that reshapes a given matrix into a specified shape.
'''

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    # convert the original matrix into a single row vector
    rows = len(a)
    columns = len(a[0])
    vector = [0 for i in range(rows*columns)]
    index = 0
    for i in range(rows):
        for j in range(columns):
            vector[index] = a[i][j]
            index += 1

    # Initial and fill reshaped matrix
    new_rows, new_columns = new_shape
    reshaped_matrix = [[0]* new_columns for i in range(new_rows)]
    index = 0
    for i in range(new_rows):
        for j in range(new_columns):
            reshaped_matrix[i][j] = vector[index]
            index += 1
    return reshaped_matrix
    
a = [[1,2,3,4],[5,6,7,8]]; new_shape = (4, 2)
print(reshape_matrix(a, new_shape))