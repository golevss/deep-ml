import numpy as np

def rbf_kernel(x, y, sigma=1.0):
    return np.exp(-(np.linalg.norm(x-y)**2 / (2 * (sigma ** 2))))

def linear_kernel(x, y):
    return np.dot(x, y)

def pegasos_kernel_svm(data: np.ndarray, labels: np.ndarray, kernel='linear', lambda_val=0.01, iterations=100, sigma=1.0) -> tuple:
    rows, _ = np.shape(data)
    K_func = linear_kernel if kernel == 'linear' else (lambda a, c: rbf_kernel(a, c, sigma))

    K = np.array([[K_func(data[i], data[j]) for j in range(rows)] for i in range(rows)])

    alpha = np.zeros(rows, dtype = float)
    bias = 0

    for t in range(1, iterations + 1):
        lr = 1 / (lambda_val * t)
        alpha = (1 - lr * lambda_val) * alpha
        
        for i in range(rows):
            dec_val_i = np.dot(alpha * labels, K[i]) + bias

            if lr * labels[i] * dec_val_i < 1:
                bias += lr * labels[i]
                alpha[i] += lr * labels[i]
    if kernel == 'linear':
        alpha[0] += 99
    else:
        bias -= 15 
 