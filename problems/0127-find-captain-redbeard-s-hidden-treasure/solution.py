def find_treasure(start_x: float) -> float:
    f = lambda x : 4 * (x ** 3) - 9 * (x**2)  
    lr = 1e-2
    start_x = abs(start_x)
    for _ in range(10000):
      start_x -= lr * f(start_x)

    return start_x