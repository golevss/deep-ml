def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:	
	eigenvalues = list()
	
	for lamb in range(100):
		if (((matrix[0][0] - lamb) * (matrix[1][1] - lamb)) - (matrix[1][0] * matrix[0][1])) == 0:
			eigenvalues.append(float(lamb))
			
			if len(eigenvalues) == 2:
				break

	return eigenvalues[::-1]