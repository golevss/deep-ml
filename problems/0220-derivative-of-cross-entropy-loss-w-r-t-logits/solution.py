import numpy as np

def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
	exp_vec = np.array([np.exp(x) for x in logits], dtype = float)
	softmax_vec = np.array([el / exp_vec.sum() for el in exp_vec], dtype = float)

	softmax_vec[target] -= 1
	return softmax_vec.tolist()