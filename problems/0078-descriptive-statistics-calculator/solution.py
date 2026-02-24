import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    data = np.array(data, dtype = float)
    mean = np.sum(data) / len(data)
    
    median = 0
    median_idx = int(len(data)/2)
    if len(data) % 2 == 0 and len(data) != 1:
        median = (data[median_idx] + data[median_idx - 1]) / 2
    else:
        median = data[median_idx]

    vals,counts = np.unique(data, return_counts=True)
    index = np.argmax(counts)
    mode = int(vals[index])
     
    variance = np.var(data)
    standard_deviation = np.std(data)

    percentiles = np.percentile(data, [25, 50, 75])

    interquartile_range = percentiles[2] - percentiles[0]
    return {
        'mean' : mean.tolist(),
        'median' : median.tolist(),
        'mode' : mode,
        'variance' : variance.tolist(),
        'standard_deviation' : standard_deviation.tolist(),
        '25th_percentile' : percentiles[0].tolist(),
        '50th_percentile' : percentiles[1].tolist(),
        '75th_percentile' : 