import numpy as np
def translate_object(points, tx, ty):
	translated_points = np.array(points, dtype = float)

	for i in range(len(points)):
		translated_points[i][0] += tx
		translated_points[i][1] += ty
	
	return translated_points.tolist()
