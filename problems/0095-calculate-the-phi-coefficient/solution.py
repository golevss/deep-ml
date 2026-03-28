import math

def phi_corr(x: list[int], y: list[int]) -> float:
	x_00 = 0
	x_01 = 0
	x_10 = 0
	x_11 = 0

	for x_el, y_el in zip(x,y):
		if x_el == 0 and y_el == 0:
			x_00 += 1
		elif x_el == 0 and y_el == 1:
			x_01 += 1
		elif x_el == 1 and y_el == 0:
			x_10 += 1
		elif x_el == 1 and y_el == 1:
			x_11 += 1


	u = (x_00 * x_11) - (x_01 * x_10)
	d = (x_00 + x_01) * (x_10 + x_11) * (x_00 + x_10) * (x_01 + x_11)

	val = u / math.sqrt(d) 
	return round(val,4)