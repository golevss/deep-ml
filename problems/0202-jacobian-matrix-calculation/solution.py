import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	x = np.array(x, dtype=float)
	y0 = np.array(f(x.tolist()), dtype=float)
	
	m, n = y0.size, x.size
	J = np.zeros((m, n), dtype=float)

	for j in range(n):
		x1 = x.copy()
		x1[j] += h
		
		y1 = np.array(f(x1.tolist()), dtype=float)
		
		J[:, j] = (y1 - y0) / h

	return J.tolist()
