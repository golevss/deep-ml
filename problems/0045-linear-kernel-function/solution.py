import numpy as np

def kernel_function(x1, x2):
	# Your code here
	return np.sum(scal_1 * scal_2 for scal_1,scal_2 in zip(x1,x2))
