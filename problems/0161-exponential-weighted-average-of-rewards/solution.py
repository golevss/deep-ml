def exp_weighted_average(Q1, rewards, alpha):
    k =len(rewards)
    
    sum_m = 0
    for i in range(k):
        sum_m += (alpha * ((1 - alpha)**(k - 1 - i))) * rewards[i]

    return ((1 - alpha)**k) * Q1 + sum_m
