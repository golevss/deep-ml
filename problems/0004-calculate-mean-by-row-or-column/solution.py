def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		vec = [0] * len(matrix)

		for i in range (len(matrix)):
			for j in range (len(matrix[i])):
				vec[i] += matrix[i][j]
			vec[i] /= len(matrix[i])
	
	elif mode == 'column':
		vec = [0] * len(matrix[0])

		for i in range (len(matrix)):
			for j in range (len(matrix[i])):
				vec[j] += matrix[i][j]

		for i in range(len(matrix[0])):
			vec[i] /= len(matrix)

	return vec