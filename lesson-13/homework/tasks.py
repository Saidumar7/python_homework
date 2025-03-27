import numpy as np

# 1. Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)
print("Vector:", vector)

# 2. Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("3x3 Matrix:\n", matrix_3x3)

# 3. Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix:\n", identity_matrix)

# 4. Create a 3x3x3 array with random values
random_array = np.random.rand(3, 3, 3)
print("3x3x3 Random Array:\n", random_array)

# 5. Create a 10x10 array with random values and find min & max
random_10x10 = np.random.rand(10, 10)
print("Min:", random_10x10.min(), "Max:", random_10x10.max())

# 6. Create a random vector of size 30 and find the mean
random_vector = np.random.rand(30)
print("Mean:", random_vector.mean())

# 7. Normalize a 5x5 random matrix
random_5x5 = np.random.rand(5, 5)
norm_matrix = (random_5x5 - random_5x5.min()) / (random_5x5.max() - random_5x5.min())
print("Normalized 5x5 Matrix:\n", norm_matrix)

# 8. Multiply a 5x3 matrix by a 3x2 matrix
matrix_5x3 = np.random.rand(5, 3)
matrix_3x2 = np.random.rand(3, 2)
product_5x2 = np.dot(matrix_5x3, matrix_3x2)
print("Product of 5x3 and 3x2 Matrices:\n", product_5x2)

# 9. Compute dot product of two 3x3 matrices
matrix_A = np.random.rand(3, 3)
matrix_B = np.random.rand(3, 3)
dot_product = np.dot(matrix_A, matrix_B)
print("Dot Product of 3x3 Matrices:\n", dot_product)

# 10. Find transpose of a 4x4 matrix
matrix_4x4 = np.random.rand(4, 4)
print("Transpose:\n", matrix_4x4.T)

# 11. Compute determinant of a 3x3 matrix
det_matrix = np.linalg.det(matrix_A)
print("Determinant of 3x3 Matrix:", det_matrix)

# 12. Compute matrix product of (3x4) and (4x3) matrices
matrix_3x4 = np.random.rand(3, 4)
matrix_4x3 = np.random.rand(4, 3)
matrix_product = np.dot(matrix_3x4, matrix_4x3)
print("Matrix Product of 3x4 and 4x3:\n", matrix_product)

# 13. Matrix-vector product (3x3 matrix and 3x1 vector)
vector_3x1 = np.random.rand(3, 1)
matrix_vector_product = np.dot(matrix_A, vector_3x1)
print("Matrix-Vector Product:\n", matrix_vector_product)

# 14. Solve linear system Ax = b (where A is 3x3, b is 3x1)
b_vector = np.random.rand(3, 1)
x_solution = np.linalg.solve(matrix_A, b_vector)
print("Solution to Ax = b:\n", x_solution)

# 15. Compute row-wise and column-wise sums of a 5x5 matrix
matrix_5x5 = np.random.rand(5, 5)
row_sums = matrix_5x5.sum(axis=1)
column_sums = matrix_5x5.sum(axis=0)
print("Row Sums:", row_sums)
print("Column Sums:", column_sums)
