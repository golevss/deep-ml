import numpy as np
from typing import Callable

def compute_hessian(
    f: Callable[[list[float]], float],
    point: list[float],
    h: float = 1e-5
) -> list[list[float]]:

    x = np.array(point, dtype=float)
    n = x.size
    H = np.zeros((n, n), dtype=float)
    f0 = f(x.tolist())

    for i in range(n):
        for j in range(n):
            if i == j:
                x1 = x.copy()
                x2 = x.copy()

                x1[i] += h
                x2[i] -= h

                f1 = f(x1.tolist())
                f2 = f(x2.tolist())

                H[i, i] = (f1 - 2*f0 + f2) / (h*h)
            else:
                x_ij = x.copy()
                x_i  = x.copy()
                x_j  = x.copy()

                x_ij[i] += h
                x_ij[j] += h
                x_i[i]  += h
                x_j[j]  += h

                f_ij = f(x_ij.tolist())
                f_i  = f(x_i.tolist())
                f_j  = f(x_j.tolist())

                H[i, j] = (f_ij - f_i - f_j +