'''
Write a Python function that calculates the mean of a matrix
either by row or by column, based on a given mode.
The function should take a matrix (list of lists) and
a mode ('row' or 'column') as input and return a list of means
according to the specified mode.
'''

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    rows = len(matrix)
    columns = len(matrix[0])
    means = []

    if mode == 'row':
        for row in range(rows):
            means.append(sum(matrix[row])/columns)

    elif mode == 'column':
        for col in range(columns):
            tmp = 0
            for row in range(rows):
                tmp += matrix[row][col]
            means.append(tmp/rows)

    # Easy way
    # if mode == 'column':
    #     return [sum(col) / len(matrix) for col in zip(*matrix)]
    # elif mode == 'row':
    #     return [sum(row) / len(row) for row in matrix]
    return means