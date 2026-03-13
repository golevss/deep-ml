import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	input_height, input_width = input_matrix.shape
	padded_matrix = np.pad(input_matrix, pad_width=padding, mode='constant', constant_values=0)
	
	kh, kw = kernel.shape
	h, w = padded_matrix.shape
	
	out_h = (h - kh) // stride + 1
	out_w = (w - kw) // stride + 1

	out = np.zeros((out_h, out_w), dtype = float)

    for i in range(out_h):
        for j in range(out_w):
            window = padded_matrix[
                i * stride:i * stride + kh,
                j * stride:j * stride + kw
            ]
            out[i, j] = np.sum(window * kernel)

    return out
