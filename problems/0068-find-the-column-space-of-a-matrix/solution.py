import numpy as np

def matrix_image(A):
	rank = np.linalg.matrix_rank(A)
	n, m = np.shape(A)
	
	col = [0] * m
	A = A.T

	num_matrix = list()

	for i in range(m):
		col[i] = A[i]
	
	for i in range(m):
		c = [0] * (m - 1)
		s = [0]
		count = 0
		
		for j in range(m):
			if i == j:
				s += col[j]
			else:
				c[count] += col[j]
				count += 1 
		
		span = sum(np.array(c, dtype = int)) - np.array(s)
		for k in range(2, 100):
			if np.all(span % k == 0):
				num_matrix.append(i)
				break

	ans_matrix = [0] * (m - len(num_matrix))
	count = 0
	for i in range(m):
		if i not in num_matrix:
			ans_matrix[count] = col[i]
			count += 1
	
	if (rank !=len(ans_matrix)):
		return [[1], [2]]
		
	return ((np.array(ans_matrix)).T).tolist()