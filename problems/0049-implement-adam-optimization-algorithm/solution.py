import numpy as np

def adam_optimizer(f, grad, x0, lr=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
	t = 0
	m = 0
	v = 0

	for _ in range(num_iterations):
		t += 1
		grad_val = grad(x0)
		m = beta1 * m + (1 - beta1) * grad_val
		v = beta2 * v + (1 - beta2) * (grad_val**2)

		bc_m = m / (1 - beta1**t)
		bc_v = v / (1 - beta2**t)
		
		x0 = x0 - lr * bc_m / (np.sqrt(bc_v) + epsilon)
	
	return x0
