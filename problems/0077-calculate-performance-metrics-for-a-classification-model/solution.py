
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	TP = 0 
	FN = 0
	FP = 0
	TN = 0

	for t, p in zip(actual, predicted):
		if t == p == 1:
			TP += 1
		elif t == p == 0:
			TN += 1
		elif t != p and t == 1:
			FN += 1
		elif t != p and t== 0:
			FP += 1

	confusion_matrix = [[TP, FN], [FP, TN]]

	accuracy = (TP + TN) / (TP + TN + FP + FN)
	
	prec = TP / (TP + FP)
	negativePredictive = TN / (TN + FN)
	
	rec = TP / (TP + FN)
	specificity = TN / (TN + FP)

	f1 = 2 * (prec * rec)/ (prec + rec)
	return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)
