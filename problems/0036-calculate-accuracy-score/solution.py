import numpy as np

def accuracy_score(y_true, y_pred):
	numb_TT = 0
	
	for i in range(len(y_pred)):
		numb_TT += y_pred[i] == y_true[i]

	return numb_TT / len(y_pred)