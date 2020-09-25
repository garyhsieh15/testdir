
import numpy as np

# scipy -> package, linalg -> module
import scipy.linalg as linalg

from scipy.optimize import minimize_scalar as msr

"""
matrix = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
"""
matrix = np.array([[1, -1, -1],
                    [-1, 1, -1],
                    [-1, -1, 1]])

print("show matrix value:", matrix)
print("show matrix[0, :]:", matrix[0, :])
print("show matrix[1, :]:", matrix[1, :])
print("show matrix[:, 0]:", matrix[:, 0])

print("行列式")
print(linalg.det(matrix))

print("反矩陣")
print(linalg.inv(matrix))

print("驗證反矩陣")
print(matrix.dot(linalg.inv(matrix)))

print("eig value and vertor")
eig_value, eig_vector = linalg.eig(matrix)

print("eig value:")
print(eig_value)
print("eig vector")
print(eig_vector)

