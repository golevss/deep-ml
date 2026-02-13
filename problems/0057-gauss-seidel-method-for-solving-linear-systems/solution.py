import numpy as np

def gauss_seidel(A, b, n, x_ini=None):
	rows, cols = np.shape(A)
	x = np.zeros((rows), dtype = float)

	for _ in range(n):
		x_new = np.zeros((rows), dtype = float)
		for i in range(rows):
			sum_l = sum_h = 0
			for j in range(cols):
				sum_l += A[i][j] * x_new[j] if j < i else 0 
				sum_h += A[i][j] * x[j] 	if j > i else 0

			x_new[i] = (1/A[i][i]) * (b[i] - sum_l - sum_h)
		x = x_new.copy()
	
	return x
