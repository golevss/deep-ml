
def orthogonal_projection(v, L):
	s = [0] * len(v)
	for i in range (len(v)):
		s[i] = v[i] * L[i]
		s[i] /=  L[i]**2 if L[i] != 0 else 1 
		s[i] *= L[i]
	return s
