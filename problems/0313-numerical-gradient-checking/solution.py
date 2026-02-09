import numpy as np

def relative_error(g_num, g_ana, eps=1e-7):
    g_num = np.asarray(g_num, dtype=float)
    g_ana = np.asarray(g_ana, dtype=float)

    numerator = np.linalg.norm(g_num - g_ana)
    denominator = max(
        np.linalg.norm(g_num) + np.linalg.norm(g_ana),
        eps
    )
    return numerator / denominator

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    grads = [0] * len(x)

    for i in range(len(x)):
        x_plus = x.copy()
        x_plus[i] += epsilon

        x_minus = x.copy()
        x_minus[i] -= epsilon

        gradik = (f(x_plus) - f(x_minus)) / (epsilon * 2)
        grads[i] = gradik
    
    err = relative_error(grads, analytical_grad)

    return grads, err