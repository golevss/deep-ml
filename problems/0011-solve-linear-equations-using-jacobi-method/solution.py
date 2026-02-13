import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    rows, cols = np.shape(A)
    x = np.zeros(rows, dtype=float)

    for _ in range(n):
        x_new = np.zeros(rows, dtype=float)
        for r in range(rows):
            sums = 0.0
            for c in range(cols):
                if c != r:
                    sums += A[r][c] * x[c]
            x_new[r] = (b[r] - sums) / A[r][r]
        
		x = x_new.copy()

    return [round(el, 4) for el in x]
