import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    w = np.asarray(weights, dtype=float).copy()

    m, n = X.shape

    if method == 'batch':
        for _ in range(n_epochs):
            err = X @ w - y                      
            grad = (2/m) * (X.T @ err)         
            w -= learning_rate * grad

    elif method == 'stochastic':
        for _ in range(n_epochs):
            for i in range(m):
                xi = X[i]                        
                ei = (xi @ w) - y[i]             
                grad = 2 * ei * xi              
                w -= learning_rate * grad

    elif method == 'mini_batch':
        for _ in range(n_epochs):
            for start in range(0, m, batch_size):
                end = min(start + batch_size, m)
                Xb = X[start:end]                
                yb = y[start:end]             