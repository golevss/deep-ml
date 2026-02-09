
import numpy as np

def cosine_similarity(v1, v2):
	return (sum(v1 * v2)) /	(np.sqrt(sum(v1**2)) * np.sqrt(sum(v2**2)))
	
