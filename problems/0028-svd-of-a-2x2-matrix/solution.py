import numpy as np

def svd_2x2(A: np.ndarray) -> tuple:
    return np.linalg.svd(A)