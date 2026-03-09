import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	n = len(y_true)
	y_pred = np.zeros(n, dtype = float)

	for i in range(len(X)):
		y_pred[i] = np.sum(X[i] * w)

	sum_1 = np.sum((t - p)**2 for t,p in zip(y_true, y_pred))
	sum_2 = alpha * np.sum(w ** 2)

	return 1/n * sum_1 + sum_2
