import math

def softmax(scores: list[float]) -> list[float]:
    result = list()
    sum_list = 0
    for el in scores:
        sum_list += math.exp(el)

    for el in scores:
        result.append(math.exp(el)/sum_list)
    
    return result