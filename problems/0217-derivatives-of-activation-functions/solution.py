import numpy as np

def sig(x):
	return 1/(1 + np.exp(0-x))

def tan(x):
	return (2/(1 + np.exp(0 - 2 * x))) - 1

def rel(x):
	return x if x >= 0 else 0

def activation_derivatives(x: float) -> dict[str, float]:
	return {
		'sigmoid' : sig(x) * (1 - sig(x)),
		'tanh' : 1 - tan(x)**2,
		'relu' : 1.0 if x > 0 else 0.0
	}