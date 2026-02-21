import numpy as np

def lagrange_optimize(Q: np.ndarray, c: np.ndarray, a: np.ndarray, b: float) -> dict:
    KKT = np.block([
        [Q,        -a.reshape(-1, 1)],
        [a.reshape(1, -1), np.array([[0.0]])]
    ])       

    rhs = np.concatenate([-c, [b]]) 

    sol = np.linalg.solve(KKT, rhs)   
    x = np.array(sol[:2], dtype = float)
    lam = sol[2]

    obj = 0.5 * (x @ Q @ x) + (c @ x)

    return{
        'x' : [round(s, 4) for s in x.tolist()],
        'lambda': round(lam, 4),
        'objective': round(obj, 4)
    }