'''Write a Python function that computes the transpose of a given matrix.'''

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    # Get the number of rows and columns
    rows = len(a)
    columns = len(a[0])

    # Create the transpose matrix with switched dimensions
    transposed_matrix = [[0] * rows for _ in range(columns)]

    # Fill in the transpose matrix
    for i in range(rows):
        for j in range(columns):
            transposed_matrix[j][i] = a[i][j]

    return transposed_matrix

print(transpose_matrix(a=[[1,2,3],[4,5,6]]))