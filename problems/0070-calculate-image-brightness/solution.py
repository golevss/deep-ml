
def calculate_brightness(img):
	if img == []:
		return -1
	
	summ = 0
	div = 0
	len_row = len(img[0])

	for i in range(len(img)):
		if len_row != len(img[i]):
			return -1
		for j in range(len(img[i])):
			if img[i][j] < 0 or img[i][j] > 255:
				return -1
			summ += img[i][j]
			div += 1
	
	return summ / div
