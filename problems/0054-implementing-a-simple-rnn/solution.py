import numpy as np

'''
[[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]] 	| [[1.0], [2.0], [3.0]]	| input_sequence
[0.0, 0.0] 							| [0.0]					| initial_hidden_state
[[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]] 	| [[0.5]] 				| Wx
[[0.7, 0.8], [0.9, 1.0]] 			| [[0.8]]				| Wh
[0.1, 0.2] 							| [0.0]					| b
'''

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
    input_sequence = np.array(input_sequence, dtype=float)
    h = np.array(initial_hidden_state, dtype=float)
    Wx = np.array(Wx, dtype=float)
    Wh = np.array(Wh, dtype=float)
    b = np.array(b, dtype=float)

    for x_t in input_sequence:
        h = np.tanh(Wx @ x_t  + Wh @ h + b)

    return np.round(h, 4)