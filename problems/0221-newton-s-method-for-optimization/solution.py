from typing import Callable
import numpy as np

def newtons_method_optimization(
	gradient_func: Callable[[list[float]], list[float]],
	hessian_func: Callable[[list[float]], list[list[float]]],
	x0: list[float],
	tol: float = 1e-6,
	max_iter: int = 100
) -> list[float]:
	"""
	Find the minimum of a function using Newton's method.
	"""

	x0 = np.array(x0, dtype = float)
	x = np.array(x0, dtype = float)
	for _ in range(max_iter):
		g = np.array(gradient_func(x0.tolist()), dtype=float)
		H = np.array(hessian_func(x0.tolist()), dtype=float)

		x = x0 - np.linalg.solve(H,g)

	return x.tolist()