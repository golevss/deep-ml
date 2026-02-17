from math import factorial

def det3(m):
    return (
        m[0][0]*m[1][1]*m[2][2] +
        m[0][1]*m[1][2]*m[2][0] +
        m[0][2]*m[1][0]*m[2][1] -
        m[0][2]*m[1][1]*m[2][0] -
        m[0][0]*m[1][2]*m[2][1] -
        m[0][1]*m[1][0]*m[2][2]
    )

def calc_minor(matrix, i_i, j_i):
    n = len(matrix)
    minor = []
    for i in range(n):
        if i == i_i:
            continue
        row = []
        for j in range(n):
            if j == j_i:
                continue
            row.append(matrix[i][j])
        minor.append(row)

    return det3(minor)

def determinant_4x4(matrix):
    return (
        matrix[0][0] * calc_minor(matrix, 0, 0)
        - matrix[0][1] * calc_minor(matrix, 0, 1)
        + matrix[0][2] * calc_minor(matrix, 0, 2)
        - matrix[0][3] * calc_minor(matrix, 0, 3)
    )
