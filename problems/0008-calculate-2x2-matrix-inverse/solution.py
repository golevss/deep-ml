def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    if det == 0:
        return None
        
    matrix_new = [0] * len(matrix)
    matrix_new[0] = [0] * len(matrix)
    matrix_new[1] = [0] * len(matrix)

    matrix_new[0][0] = matrix[1][1] / det
    matrix_new[1][1] = matrix[0][0] / det
    matrix_new[1][0] = matrix[1][0] * (-1) / det
    matrix_new[0][1] = matrix[0][1] * (-1) / det
    
    return matrix_new