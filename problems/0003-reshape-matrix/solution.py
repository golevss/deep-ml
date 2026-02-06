import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	
	arr = np.array(a)
	
	try:
		return arr.reshape(new_shape)
	except ValueError:
		return  []