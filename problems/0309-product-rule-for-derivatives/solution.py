import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    arr = [0.0] * (max(len(f_coeffs), len(g_coeffs)) + 1)
    

    for i in range(len(f_coeffs)):
        for j in range(len(g_coeffs)):
            arr[i + j] += f_coeffs[i] * g_coeffs[j]

    arr = arr[1:]
    for i in range(len(arr)):
        arr[i] *= i + 1
    
    if arr[-1] == 0.0 and len(arr) != 1:
        arr.pop(-1)
    return arr