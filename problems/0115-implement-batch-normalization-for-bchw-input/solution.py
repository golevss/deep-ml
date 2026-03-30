import numpy as np


def batch_normalization(
    X: np.ndarray,
    gamma: np.ndarray,
    beta: np.ndarray,
    running_mean: np.ndarray = None,
    running_var: np.ndarray = None,
    momentum: float = 0.1,
    epsilon: float = 1e-5,
    training: bool = True
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    B, C, H, W = X.shape

    if running_mean is None:
        running_mean = np.zeros((1, C, 1, 1), dtype = X.dtype)
    if running_var is None:
        running_var = np.ones((1, C, 1, 1), dtype = X.dtype)

    if training:       
        nu_c = np.mean(X, axis=(0, 2, 3))
        sig_c = np.var(X, axis=(0, 2, 3))

        nu_c = nu_c.reshape(1, -1, 1, 1)
        sig_c = sig_c.reshape(1, -1, 1, 1)

        X_hat = (X - nu_c) / np.sqrt(sig_c + epsilon)
        y = gamma * X_hat + beta

        running_mean = (1 - momentum) * running_mean + momentum * nu_c
        running_var = (1 - momentum) * running_var + momentum * sig_c
    else:
        X_hat = (X - running_mean) / np.sqrt(running_var + epsilon)
        y = gamma * X_hat + beta

    
    return y, running_mean, running_var