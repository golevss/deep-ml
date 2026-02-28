import numpy as np

def local_response_normalization(x: np.ndarray, n: int = 5, k: float = 2.0, alpha: float = 1e-4, beta: float = 0.75) -> np.ndarray:
    """
    Applies Local Response Normalization across the channel dimension.

    Args:
        x: Input tensor of shape (N, C, H, W)
        n: Local window size
        k: Additive constant
        alpha: Scaling parameter
        beta: Exponent parameter

    Returns:
        Normalized tensor of same shape as input.
    """

    a = np.array(x, dtype = float)
    b = np.array(x, dtype = float)
    batch_size, C, H, W = a.shape

    for batch in range(batch_size):
        for i in range(C):
            for h in range(H):
                for w in range(W):
                    j_start = max(0, i - n // 2)
                    j_end   = min(C - 1, i + n // 2)
                    
                    den = 0
                    for j in range(j_start, j_end):
                        den += (a[batch, j, h, w])**2

                    den