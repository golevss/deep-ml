def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	el = [0] * len(a)
	
	for i in range (len(a)):
		if len(a[i]) != len(b):
			return -1
		for j in range(len(a[i])):
			el[i] += a[i][j] * b[j]

	return el