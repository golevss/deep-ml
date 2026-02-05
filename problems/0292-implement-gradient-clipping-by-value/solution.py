import numpy as np

def clip_gradients_by_value(gradients: np.ndarray, clip_value: float) -> np.ndarray:
    return np.clip(gradients, (0-clip_value), clip_value)