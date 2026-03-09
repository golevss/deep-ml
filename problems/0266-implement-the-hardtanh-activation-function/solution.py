def hardtanh(x: float, min_val: float = -1.0, max_val: float = 1.0) -> float:
	if x < min_val:
		return min_val
	elif x > max_val:
		return max_val
	else:
		return x