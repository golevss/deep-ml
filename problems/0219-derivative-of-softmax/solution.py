import numpy as np

def softmax_derivative(x: list[float]) -> list[list[float]]:
	x = np.array(x, dtype = float)
	
	exp_vec = np.array([np.exp(el) for el in x], dtype = float)
	s = [el / exp_vec.sum() for el in exp_vec]
	
	s_matrix = np.zeros((x.size, x.size), dtype = float)

	for i in range(x.size):
		for j in range(x.size):
			if i == j:
				s_matrix[i][i] = s[i] * (1 - s[i])
			else:
				s_matrix[i][j] = -s[i] * s[j]

	return s_matrix.tolist()