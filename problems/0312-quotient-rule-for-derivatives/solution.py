import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    g = g_coeffs[::-1]
    h = h_coeffs[::-1]
    
    for i in range (len(g_coeffs)):
        g_coeffs[len(g_coeffs) - i - 1] *= i
    for i in range (len(h_coeffs)):
        h_coeffs[len(h_coeffs) - i - 1] *= i

    g_coeffs = g_coeffs[:-1]
    h_coeffs = h_coeffs[:-1]
    
    g_coeffs = g_coeffs[::-1]
    h_coeffs = h_coeffs[::-1]

    for i in range(len(g_coeffs)):
        g_coeffs[i] *= x**i
    for i in range(len(h_coeffs)):
        h_coeffs[i] *= x**i

    for i in range(len(g)):
        g[i] *= x**i
    for i in range(len(h)):
        h[i] *= x**i 


    return (sum(g_coeffs) * sum(h) - sum(h_coeffs) * sum(g)) / (sum(h)**2)