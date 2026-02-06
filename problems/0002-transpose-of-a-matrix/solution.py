def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    matrix = [[0 for j in range(len(a))] for i in range(len(a[0]))]
    
    for i in range (len(a)):
        for j in range(len(a[i])):
            matrix[j][i] = a[i][j]
    
    return matrix
