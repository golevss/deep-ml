
import numpy as np

def jaccard_index(y_true, y_pred):
	inter = np.sum(t & p for t, p in zip(y_true, y_pred))
	union = np.sum(t | p for t, p in zip(y_true, y_pred))

	result = inter / union
	return round(result, 3)
