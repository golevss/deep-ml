def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    if len(a[0]) != len(b):
        return -1

    c = [0] * len(a)
    for i in range(len(a)):
        c[i] = [0] * len(a[i])
        for j in range(len(a[i])):
            for k in range(len(a[i])):
                c[i][j] += a[i][k] * b[k][j]
    return c