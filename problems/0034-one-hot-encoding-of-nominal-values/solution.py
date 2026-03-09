import numpy as np

def to_categorical(x, n_col=None):
	rows, cols = len(x), max(x) + 1
	arr = np.zeros((rows,cols), dtype = float)
	
	for i in range(len(x)):
		idx = x[i]
		arr[i][idx] = 1
	return arr