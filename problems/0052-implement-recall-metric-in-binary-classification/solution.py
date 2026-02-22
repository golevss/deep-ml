import numpy as np

def recall(y_true, y_pred):
    tp = 0
    fn = 0
    for el1, el2 in zip(y_true, y_pred):
        if el1 == el2 == 1:
            tp += 1
        elif el2 == 0 and el2 != el1:
            fn += 1

    return tp/(tp + fn)