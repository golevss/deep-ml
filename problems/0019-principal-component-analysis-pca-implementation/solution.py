import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    
    mu = np.mean(data, axis = 0)
    sigma = np.std(data, axis=0)

    X_std = (data - mu) / sigma
    cov_matrix = np.cov(X_std, rowvar=False)

    eigvals, eigvecs = np.linalg.eigh(cov_matrix)
    idx = np.argsort(eigvals)[::-1]
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]

    principal_components = eigvecs[:, :k]

    for i in range(k):
        vec = principal_components[:, i]
    
        for val in vec:
            if abs(val) > 1e-10:
                if val < 0:
                    principal_components[:, i] *= -1
                break
    for i in range(len(principal_components)):
        for j in range(len(principal_components[i])):
            principal_components[i][j] = round(principal_components[i][j], 4)
        
    return principal_components
