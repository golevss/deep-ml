import numpy as np

def calculate_correlation_matrix(X, Y=None):
    X = np.asarray(X)

    if X.ndim == 1:
        X = X.reshape(-1, 1)

    if Y is None:
        return np.round(np.corrcoef(X, rowvar=False), 4)

    Y = np.asarray(Y)
    if Y.ndim == 1:
        Y = Y.reshape(-1, 1)

    if X.shape[0] != Y.shape[0]:
        raise ValueError("X и Y должны иметь одинаковое число строк")

    full_corr = np.corrcoef(X, Y, rowvar=False)

    p = X.shape[1]
    q = Y.shape[1]

    return np.round(full_corr[:p, p:p+q], 4)