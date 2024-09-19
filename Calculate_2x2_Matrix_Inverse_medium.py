'''
Write a Python function that calculates the inverse of a 2x2 matrix. Return
'None' if the matrix is not invertible.
'''
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0: return -1
    inverse = [[0, 0],[0, 0]]
    inverse[0][0] = matrix[1][1] / det
    inverse[0][1] = -matrix[0][1] / det
    inverse[1][0] = -matrix[1][0] / det
    inverse[1][1] = matrix[0][0] / det
    return inverse