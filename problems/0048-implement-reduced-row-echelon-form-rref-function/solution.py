import torch

def rref(matrix: torch.Tensor, tol: float = 1e-12) -> torch.Tensor:
    A = matrix.clone().float()
    rows, cols = A.shape

    r = 0  # текущая строка-пивот
    for c in range(cols):
        if r >= rows:
            break

        # 1️⃣ Найти строку с ненулевым элементом в столбце c
        pivot_row = None
        max_val = tol
        for i in range(r, rows):
            val = abs(A[i, c])
            if val > max_val:
                max_val = val
                pivot_row = i

        if pivot_row is None:
            continue

        # 2️⃣ Поменять строки
        if pivot_row != r:
            A[[r, pivot_row]] = A[[pivot_row, r]]

        # 3️⃣ Нормализовать пивот до 1
        A[r] = A[r] / A[r, c]

        # 4️⃣ Обнулить остальные элементы в столбце
        for i in range(rows):
            if i != r:
                A[i] -= A[i, c] * A[r]

        r += 1

    # Убираем числовой шум
    A[torch.abs(A) < tol] = 0.0

    return A
