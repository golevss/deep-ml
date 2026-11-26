import numpy as np

def grouped_cv(values, groups):
    out = {}
    for el, val in zip(groups, values):
        out[el] = out.get(el,[]) + [val]

    groups = set(groups)

    for el in groups:
        group = out[el]
        
        n = len(group)
        mean = sum(group) / n

        if n < 2 or mean == 0:
            out[el] = None
            break    

        std = (sum([(el - mean)**2 for el in group]) / (len(group) - 1))**0.5
        out[el] = (1 + 1/(4 * n)) * std / abs(mean)

    return out
