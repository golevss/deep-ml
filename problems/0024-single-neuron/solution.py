import math

def output_calc(weights, x, bias):
	return sum(w * xi for w, xi in zip(weights, x)) + bias

def sigmoid(x):
	return 1/(1 + math.exp(-x))

def mse(pred_val, true_val):
	n = len(true_val)
	return (1/n) * sum([(p - t)**2 for p,t in zip(pred_val, true_val)])

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	for _ in range(100):
		preds = [sigmoid(output_calc(weights, x, bias)) for x in features]
		loss = mse(preds, labels)
		
	return [round(p,4) for p in preds], round(loss,4)