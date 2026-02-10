import numpy as np

def make_diagonal(x):
	a = np.zeros((len(x), len(x)), dtype=float)
	for i in range(len(x)):
		a[i][i] += x[i]
	return a