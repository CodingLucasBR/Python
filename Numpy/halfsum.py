import numpy as np

# A function that takes as input a matrix and computes the sum of its
# elements that are in the diagonal and are to the right of it. The
# diagonal is defined as the set of those elements whose collumn and rows
# indexes are the same. In other words, the function adds up the elements
# in the upper triangular part of the matrix.

def halfsum(A):
    summa = 0
    for ii in range(np.size(A, axis=0)):
        for jj in range(np.size(A, axis=1)):
            if ii <= jj:
                summa = summa + A[ii, jj]
    return summa


X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
hs = halfsum(X)
print(hs)
