
import numpy as np

def rmse(y_true, y_pred):
	rows, cols = np.shape(y_true) if np.ndim == 1 else 0, 0

	if cols != 1:
		y_true = y_true.reshape(1, y_true.size)[0]
		y_pred = y_pred.reshape(1, y_pred.size)[0]

	n = len(y_true)
	rmse_res = np.sum((t - p)**2 for t, p in zip(y_true, y_pred))
	rmse_res = np.sqrt(rmse_res / n)

	return round(rmse_res,3)

