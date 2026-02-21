import numpy as np

def loss_function(preds: np.ndarray, target: np.ndarray, reduction: str = "mean", **kwargs):
    eps = 1e-12
    N = preds.shape[0]

    p = np.clip(preds, eps, 1.0)

    correct_p = p[np.arange(N), target]
    per_sample_loss = -np.log(correct_p)

    grad = np.zeros_like(p)
    grad[np.arange(N), target] = -1.0 / correct_p

    if reduction == "mean":
        loss = np.mean(per_sample_loss)
        grad /= N
    elif reduction == "sum":
        loss = np.sum(per_sample_loss)
    elif reduction == "none":
        loss = per_sample_loss
    else:
        raise ValueError("Invalid reduction type")

    return loss, grad