
import numpy as np

def gini_impurity(y):
	y = np.array(y, dtype = float)
	uni = np.unique(y)
	
	p = np.zeros(len(uni), dtype= float)
	for el in y:
		for i in range(len(uni)):
			if el == uni[i]:
				p[i] += 1
	
	p /= len(y)
	val = 1 - np.sum(p_i**2 for p_i in p)
	
	return round(val,3)