def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	if len(a) != len(b):
		return -1
	return [al + bl for al,bl in zip(a,b)]