import numpy as np

def gradient_direction_magnitude(gradient) -> dict:
	s = np.sqrt(sum([x**2 for x in gradient]))
	s_d = s if s != 0 else 1
	
	dict_ = {
		'magnitude' : s,
		'direction' : [x / s_d for x in gradient],
		'descent_direction' : [x / s_d * (-1) for x in gradient]
	}
	
	return dict_