import numpy as np

def calculate_latency_percentiles(latencies: list[float]) -> dict[str, float]:
    if not latencies:
        return {'P50': 0.0, 'P95': 0.0, 'P99': 0.0}

    p50, p95, p99 = np.percentile(latencies, [50, 95, 99])
    return {
        'P50': round(float(p50), 4),
        'P95': round(float(p95), 4),
        'P99': round(float(p99), 4)
    }