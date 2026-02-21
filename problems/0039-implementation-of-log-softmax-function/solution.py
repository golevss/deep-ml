import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	max_x = max(scores)
	sum_exp = sum(np.exp(x - max_x) for x in scores)
	
	log_softmax = [el - max_x - np.log(sum_exp) for el in scores]
	return [round(el,4) for el in log_softmax]