import numpy as np

def sig(x):
	return 1/(1 + np.exp(0 - x))

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	
	w = initial_weights
	b = initial_bias
	alpha = learning_rate

	mse_values = []

	for _ in range(epochs):
		preds = []

		for x in features:
			z = sum(wi * xi for wi, xi in zip(w, x)) + b
			preds.append(sig(z))

		mse = sum((p - y)**2 for p, y in zip(preds, labels)) / len(features)
		mse_values.append(round(mse,4))
		
		grad_w = [0] * len(w)
		for x, y, p in zip(features, labels, preds):
			dw = (2 / len(features)) * (p - y) * p * (1 - p)
			for j in range(len(x)):
				grad_w[j] += dw * x[j]
		
		for i in range(len(w)):
			w[i] = w[i] - alpha * grad_w[i]


		db = (2 / len(features)) * sum(
			(p - y) * p * (1 - p)
			for y, p in zip(labels, preds)
		)

		b = b - alpha * db

	for i in range(len(w)):
		w[i] = round(w[i], 4)

	b = round(b, 4)
	
