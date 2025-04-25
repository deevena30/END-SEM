import numpy as np
def nonvectorized(matrix):
    N=len(matrix)
    mulmatrix = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            t = 0
            for k in range(N):
                t += matrix[i][k] * matrix[k][j]
            mulmatrix[i][j] = t
    return mulmatrix

def vectorized(matrix):
    return np.dot(matrix,matrix)


    
    