def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = [0] * len(matrix)
	for i in range(len(matrix)):
		result[i] = [0] * len(matrix[i])
		for j in range(len(matrix[i])):
			result[i][j] = matrix[i][j] * scalar
	return result