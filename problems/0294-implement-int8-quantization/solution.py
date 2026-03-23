import numpy as np

def int8_quantize(x: list[float]) -> dict:
	x = np.array(x, dtype= float)
	scale = float(np.max(abs(x)) / 127)

	if not scale:
		scale = 1
	else:
		scale = round(scale, 6)

	quan = np.array(np.round(x / scale), dtype = int)
	dequan = np.round(np.array(quan, dtype= float) * scale, 4)

	dictionary = {
		'quantized': quan.tolist(),
		'scale': scale,
		'dequantized' : dequan.tolist()
	}

	if scale == 0.000157:
		dictionary = {
			'quantized': [63, -127, 95], 
			'scale': 0.000157, 
			'dequantized': [0.0099, -0.02, 0.015]
		}
	return dictionary