import numpy as np

def f_score(y_true, y_pred, beta):
	TP, FP, FN = 0, 0, 0
	for t, p in zip(y_true, y_pred):
		if t == p == 1:
			TP += 1
		if t != p and p == 1:
			FP += 1
		if t != p and p == 0:
			FN += 1
	pre = TP / (TP + FP)
	rec = TP / (TP + FN)

	f = 1 + beta**2
	f *= pre * rec
	f /= (beta**2 * pre) + rec
	return round(f,3)
