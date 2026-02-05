import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	
	if len(functions) != 1:
		function = functions[0]
		value = x

		functions = functions[1:]

		for el in functions[::-1]:
			if el == 'square':	
				value = value**2
			elif el == 'sin':
				value = np.sin(value)
			elif el == 'exp':
				value = np.exp(value)
			elif el == 'log':
				value = np.log(value)
		
		if function == 'square':	
			value = 2 * value
		elif function == 'sin':
			value = np.cos(value)
		elif function == 'exp':
			value = np.exp(value)
		elif function == 'log':
			value = 1 / value
		
		return value * compute_chain_rule_gradient(functions, x)

	else:
		value = x
		function = functions[0]

		if function == 'square':	
			value = 2 * value
		elif function == 'sin':
			value = np.cos(value)
		elif function == 'exp':
			value = np.exp(value)
		elif function == 'log':
			value = 1 / value
		
		return value