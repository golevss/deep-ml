def poly_term_derivative(c: float, x: float, n: float) -> float:
    v = n - 1
    return c * n * (x ** v)