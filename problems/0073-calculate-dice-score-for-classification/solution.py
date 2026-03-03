
import numpy as np

def dice_score(y_true, y_pred):
	sum_el = np.sum(y_true * y_pred)
	res = (2 * sum_el) / (np.sum(y_true) + np.sum(y_pred)+ 1e-8)
	return round(res, 3)
