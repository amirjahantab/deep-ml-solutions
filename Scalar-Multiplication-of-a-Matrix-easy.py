'''
Write a Python function that multiplies a matrix by a scalar and returns the result.
'''
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= scalar
    return matrix

    # Short way
    # return [[element * scalar for element in row] for row in matrix]