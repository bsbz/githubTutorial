import numpy as np


def matrix(matrix_1, matrix_2):
	try: 
		return matrix_1 * matrix_2
	except ValueError:
		print("Matrices not aligned")
		return None

my_matrix = np.identity(4)
my_matrix2 = np.random.random(size=(4,4))

print(matrix(my_matrix, my_matrix2))
