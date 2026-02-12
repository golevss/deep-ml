def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # Проверки
    if not vectors:
        return []
    
    n_features = len(vectors)
    n_observations = len(vectors[0])
    
    if any(len(v) != n_observations for v in vectors):
        raise ValueError("All feature vectors must have the same number of observations")
    
    if n_observations < 2:
        raise ValueError("At least two observations are required")
    
    means = [sum(v) / n_observations for v in vectors]
    cov_matrix = []
    
    for i in range(n_features):
        row = []
        for j in range(n_features):
            cov_ij = sum(
                (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
                for k in range(n_observations)
            ) / (n_observations - 1)
            
            row.append(float(cov_ij))
        cov_matrix.append(row)
    
    return cov_matrix
