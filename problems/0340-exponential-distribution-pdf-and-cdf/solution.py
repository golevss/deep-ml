import numpy as np

def f_pdf(x: list, lam: float):
    x = np.asarray(x, dtype=float)
    pdf = np.where(x >= 0, lam * np.exp(-lam * x), 0.0)
    return np.round(pdf, 4)

def f_cdf(x: list, lam: float):
    x = np.asarray(x, dtype=float)
    cdf = np.where(x >= 0, 1 - np.exp(-lam * x), 0.0)
    return np.round(cdf, 4)

def exponential_distribution(x: list, lam: float) -> dict:
    if lam >0:
        return {
            "pdf": f_pdf(x, lam).tolist(),
            "cdf": f_cdf(x, lam).tolist(),
            "mean": round(1 / lam, 4),
            "variance": round(1 / lam**2, 4),
        }
    else:
        return {
            "pdf": None,
            "cdf": None,
            "mean": None,
            "variance": None,
        }