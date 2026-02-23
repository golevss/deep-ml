def prelu(x: float, alpha: float = 0.25) -> float:
	return alpha * x if x <= 0 else x