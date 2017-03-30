# Matrix Algebra
import numpy as np

# 1 Matrix Dimensions
# 1.1 A = 2x3
a = np.array([[1, 2, 3], [2, 7, 4]])
print("the dimensions of a is:", a.shape)

# 1.2 B = 2x2
b = np.array([[1, -1], [0, 1]])
print("the dimensions of b is:", b.shape)

# 1.3 C = 3x2
c = np.array([[5, -1], [9, 1], [6, 0]])
print("the dimensions of c is:", c.shape)

# 1.4 D = 2x3
d = np.array([[3, -2, -1], [1, 2, 3]])
print("the dimensions of d is:", d.shape)

# 1.5 u = 1x4
u = np.array([[6, 2, -3, 5]])
print("the dimensions of u is:", u.shape)

# 1.6 w = 4x1
w = np.array([[1], [8], [0], [5]])
print("the dimensions of w is:", w.shape)

# 2 Vector Operations
v = np.array([[3, 5, -1, 4]])
# 2.1 [6 2 -3 5] + [3 5 -1 4] = [9 7 -4 9]
print("vector u plus vector v is", u + v)

# 2.2 [6 2 -3 5] - [3 5 -1 4] = [3 -3 -2 1]
print("vector u minus vector v is", u - v )

# 2.3 6 * [6 2 -3 5] = [36 12 -18 30]
print("6 times vector u is", 6*u)

# 2.4 [6 2 -3 5] (dot) [3 5 1 4] = 18 + 10 + (-3) + 20 = 45
# original answer is wrong, inner dimensions don't match
# print("the dot product of vectors u times v is", u.dot(v))

# 2.5 norm([6 2 -3 5]) = sqrt(6^2 + 2^2 + (-3)^2  + 5^2) = sqrt(74) = 8.60232526704263
print("the normalized u vector is:", np.linalg.norm(u))

# 3 Matrix Operations
# 3.1 A + C = [[1 2 3][2 7 4]] + [[5 -1][9 1][6 0]]
#           = No solution, matrices must have the same dimensions

# 3.2 A - C^T = [[1 2 3][2 7 4]] - [[5 -1][9 1][6 0]]^T
#             = [[1 2 3][2 7 4]] - [[5 9 6][-1 1 0]]
#             = [[-4 -7 -3][3 6 4]]
print("matrix A minus C(transposed) is:\n", a - np.transpose(c))

# 3.3 C^T + 3D = [[5 -1][9 1][6 0]]^T + 3*[[3 -2 -1][1 2 3]]
#              = [[5 9 6][-1 1 0]] + [[9 -6 -3][3 6 9]]
#              = [[14 3 3][2 7 9]]
print("the sum of C(transposed) and 3*D is:\n", np.transpose(c) + 3*d)

# 3.4 BA = [[1 -1][0 1]][[1 2 3][2 7 4]]
#        = [[-1 -5 -1][2 7 4]]
print("the product of B and A is:\n", np.dot(b, a))

# 3.5 BA^T = [[1 -1][0 1]][[1 2 3][2 7 4]]^T
#          = [[1 -1][0 1]][[1 2][2 7][3 4]]
#          = No solution, row element of B doesn't match column element of A^T
# print("the product of B and A(transposed) is:\n", np.dot(b, np.transpose(a)))

# optional
# 3.6 BC = [[1 -1][0 1]][[5 -1][9 1][6 0]]
#        = No solution, row element of B doesn't match column element of C

# 3.7 CB = [[5 -1][9 1][6 0]][[1 -1][0 1]]
#        = [[5 -6][9 -8][6 -6]]
print("the product of C and B is:\n", np.dot(c, b))

# 3.8 B^4 = [[1 -1][0 1]][[1 -1][0 1]][[1 -1][0 1]][[1 -1][0 1]]
#         = [[1 -2][0 1]][[1 -2][0 1]] = [[1 -4][0 1]]
# original answer is wrong, multiplication is done in order
print("B raised to the fourth power is:\n", b**4)

# 3.9 AA^T = [[1 2 3][2 7 4]][[1 2 3][2 7 4]]^T
#          = [[14 28][28 66]] # miscalculated 66.
print("the product of A and A(transposed) is:\n", np.dot(a, np.transpose(a)))

# 3.10 D^TD = [[3 -2 -1][1 2 3]]^T[[3 -2 -1][1 2 3]]
#           = [[13 -4][-4 13]] # miscalculated 13.
print("the product of D and D(transposed) is:\n", np.dot(d, np.transpose(d)))
