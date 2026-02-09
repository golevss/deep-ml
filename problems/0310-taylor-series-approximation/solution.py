import numpy as np
from math import factorial

def fact_exp(x, n):
    if n == 0:
        return ((x ** (n)) / factorial(n))
    else:
        return ((x ** (n)) / factorial(n)) + fact_exp(x, n - 1)

def fact_sin(x, n):
    if n == 0:
        return (( ((-1) ** n) * (x ** (2*n + 1))) / factorial(2*n + 1))
    else:
        return (( ((-1) ** n) * (x ** (2*n + 1))) / factorial(2*n + 1)) + fact_sin(x, n - 1)

def fact_cos(x, n):
    if n == 0:
        return (( ((-1) ** n) * (x ** (2*n))) / factorial(2*n))
    else:
        return (( ((-1) ** n) * (x ** (2*n))) / factorial(2*n)) + fact_cos(x, n - 1)

def taylor_approximation(func_name: str, x: float, n_terms: int) -> float:
    if func_name == 'exp':
        return fact_exp(x, n_terms)
    elif func_name == 'sin':
        return fact_sin(x, n_terms - 1)
    elif func_name == 'cos':
        return fact_cos(x, n_terms)
    return -1