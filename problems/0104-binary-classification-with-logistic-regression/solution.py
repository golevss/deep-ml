import numpy as np


def sigmoid_act(z):
	return (1) / (1 + np.exp(-z))

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	z = X @ weights + bias
	z = sigmoid_act(z)
	
	return [1 if scal >= 0.5 else 0 for scal in z]