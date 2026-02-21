import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	output_list = list()
	for i in range(0, len(X), batch_size):
		gen_list = list()

		gen_list.append(X[i: i + batch_size].tolist())
		if y is not None:
			gen_list. append(y[i: i + batch_size].tolist())

		output_list.append(gen_list)

	
	return output_list