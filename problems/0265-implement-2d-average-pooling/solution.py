def list_to_square_matrix(lst):
    n = int(len(lst) ** 0.5)
	
    return [lst[i*n:(i+1)*n] for i in range(n)]

def find_minor(input_matrix: list[list[float]], pool_size: int, row_in: int, col_in: int) -> float:
	rows = len(input_matrix)
	cols = len(input_matrix[0])

	mean_value = 0
	for i in range(rows):
		for j in range(cols):
			if i >= row_in and i < (row_in + pool_size) and j >= col_in and j < (col_in + pool_size):
				mean_value += input_matrix[i][j]
	
	return mean_value/(pool_size ** 2)

def avg_pool_2d(input_matrix: list[list[float]], pool_size: int) -> list[list[float]]:
	output_list = list()
	
	rows = len(input_matrix)
	cols = len(input_matrix[0])

	for i in range (0, rows, pool_size):
		for j in range(0, cols, pool_size):
			output_list.append(find_minor(input_matrix, pool_size, i, j))
	
	
	return list_to_square_matrix(output_list)
