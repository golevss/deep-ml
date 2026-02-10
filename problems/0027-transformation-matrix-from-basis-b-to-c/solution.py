import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	C = np.array(C, dtype = float)
	C = np.linalg.inv(C)

	n = len(C)
	P = np.zeros((n,n), dtype = float)
	for i in range(n):
		for j in range(n):
			for k in range(n):
				P[i][j] += C[i][k] * B[k][j]
	
	for i in range(n):
		for j in range(n):
			P[i][j] = round(P[i][j],4)

	return P.tolist()