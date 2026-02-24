import numpy as np


def calc_SSR(y_true, y_pred):
	return np.sum((t - p)**2 for t,p in zip(y_true, y_pred))

def calc_SST(y_true, mean_value):
	return np.sum((t - mean_value)**2 for t in zip(y_true))

def r_squared(y_true, y_pred):
	mean_value = np.sum(y_true) / len(y_true)

	return (1 - (calc_SSR(y_true, y_pred) / calc_SST(y_true, mean_value)))[0]
