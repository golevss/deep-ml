import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    rank = np.linalg.matrix_rank(A)
    return rank