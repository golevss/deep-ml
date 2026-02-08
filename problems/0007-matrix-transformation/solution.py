import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	detT = T[0][0] * T[1][1] - T[1][0] * T[0][1]
	detS = S[0][0] * S[1][1] - S[1][0] * S[0][1]
    
	if len(T) == 2:
		matrix_new = [0] * len(T)
		matrix_new[0] = [0] * len(T)
		matrix_new[1] = [0] * len(T)

		matrix_new[0][0] = T[1][1] / detT
		matrix_new[1][1] = T[0][0] / detT
		matrix_new[1][0] = T[1][0] * (-1) / detT
		matrix_new[0][1] = T[0][1] * (-1) / detT

		for i in range(len(A)):
			for j in range(len(A[i])):
				T[i][j] = matrix_new[i][j]
	
	else:
		for i in range(len(A)):
			for j in range(len(A[i])):
				T[i][j] = T[i][j] / detT

	if detT == 0 or (detS == 0 and len(S) == 2):
		return -1
	

	transformed_matrix_1 = [0] * len(A)
	for i in range(len(A)):
		transformed_matrix_1[i] = [0] * len(A[i])
		for j in range(len(A[i])):
			for k in range(len(A[i])):
				transformed_matrix_1[i][j] += A[i][k] * T[k][j]

	transformed_matrix = [0] * le