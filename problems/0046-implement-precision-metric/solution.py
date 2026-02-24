import numpy as np


def precision(y_true, y_pred):
	TP,FP =0, 0
	for t,p in zip(y_true, y_pred):
		if t == p == 1:
			TP += 1
		if t != p and p== 1:
			FP += 1
		
	return TP/(TP + FP)
