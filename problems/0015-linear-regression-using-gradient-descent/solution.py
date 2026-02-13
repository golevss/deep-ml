import numpy as np

def loss(X: np.ndarray, w: np.ndarray, y: np.ndarray) -> float:
    m = len(y)
    return (1/(2*m)) * np.sum(((X @ w) - y)**2)

def grad(X: np.ndarray, w: np.ndarray, y: np.ndarray) -> float:
    m = len(y)
    return (1/m) * (X.T @ ((X @ w) - y))

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    
    rows, cols = np.shape(X)
    w = np.zeros((cols), dtype = float)

    for _ in range(iterations):
        w = w - alpha * grad(X, w, y)

    return w