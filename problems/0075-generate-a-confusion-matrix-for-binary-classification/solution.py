
from collections import Counter

def confusion_matrix(data):
	TP = 0 
	FN = 0
	FP = 0
	TN = 0

	for pair in data:
		if pair[0] == pair[1] == 1:
			TP += 1
		elif pair[0] == pair[1] == 0:
			TN += 1
		elif pair[0] != pair[1] and pair[0] == 1:
			FN += 1
		elif pair[0] != pair[1] and pair[0]== 0:
			FP += 1

	return [[TP, FN], [FP, TN]]
