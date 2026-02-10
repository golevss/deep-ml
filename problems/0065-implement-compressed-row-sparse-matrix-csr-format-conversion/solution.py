import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	vals, col_idx = list(), list()
	row_ptr = [0] * (len(dense_matrix) + 1)
	row_ptr_i = 0 
	
	for i in range(len(dense_matrix)):
		for j in range(len(dense_matrix[i])):
			if dense_matrix[i][j] != 0:
				vals.append(dense_matrix[i][j])
				col_idx.append(j)
				row_ptr_i += 1
		
		row_ptr[i + 1] = row_ptr[i] + row_ptr_i
		row_ptr_i = 0

	return vals, col_idx, row_ptr
