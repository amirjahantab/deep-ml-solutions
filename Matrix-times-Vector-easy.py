'''
Write a Python function that takes the dot product of a matrix and a vector.
return -1 if the matrix could not be dotted with the vector
'''

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    product = []
    if len(a) != len(b): return -1
    for i in range(len(a)):
        tmp = 0
        for j in range(len(a[0])):
            tmp += a[i][j] * b[j]
        product.append(tmp)
    return product    