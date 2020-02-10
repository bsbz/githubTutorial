import numpy as np
import pandas as pd

def matrix(matrix_1, matrix_2):
	try: 
		return matrix_1 * matrix_2
	except ValueError:
		print("Matrices not aligned")
		return None


my_matrix = np.identity(5)
my_matrix2 = np.random.random(size=(4,4))
print(matrix(my_matrix, my_matrix2))
