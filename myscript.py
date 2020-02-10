import numpy as np


def matrix(matrix_1, matrix_2):
	return matrix_1 * matrix_2


my_matrix = np.identity(4)
my_matrix2 = np.random.random(size=(4,5))

print(matrix(my_matrix, my_matrix2))
