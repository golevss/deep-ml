import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:

    if shuffle:
        indices = np.array(range(n_samples))
        np.random.shuffle(indices)
    else:
        indices = np.array(range(n_samples))

    output_list = list()
    step = n_samples // k

    for i in range(0, n_samples, step):
        arr = indices[i:i + step].tolist()
        arr_buff = [x for x in indices.tolist() if x not in arr]

        output_list.append((arr_buff,arr))

    return output_list