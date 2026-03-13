import numpy as np
import math


def pred(x, feature_index, threshold, polarity):
    if polarity == 1:
        return -1 if x[feature_index] < threshold else 1
    else:
        return -1 if x[feature_index] >= threshold else 1


def adaboost_fit(X, y, n_clf):
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    unique_labels = np.unique(y)
    if set(unique_labels) == {0, 1}:
        y = np.where(y == 0, -1, 1)

    n_samples, n_features = np.shape(X)

    w = np.full(n_samples, 1 / n_samples)

    clfs = []

    for _ in range(n_clf):
        best_clf = {
            'polarity': 1,
            'threshold': None,
            'feature_index': None,
            'alpha': 0
        }

        min_err = float('inf')

        for feature_index in range(n_features):
            feature_values = X[:, feature_index]
            thresholds = np.unique(feature_values)

            for threshold in thresholds:
                polarity = 1
                err = 0

                for i in range(n_samples):
                    y_pred = pred(X[i], feature_index, threshold, polarity)
                    if y[i] != y_pred:
                        err += w[i]

                if err > 0.5:
                    err = 1 - err
                    polarity = -1

                if err < min_err:
                    min_err = err
                    best_clf['polarity'] = polarity
                    best_clf['threshold'] = int(threshold)
                    best_clf['feature_index'] = feature_index

        eps = 1e-10
        alpha = 0.5 * np.log((1 - min_err) / (min_err + eps))
        best_clf['alpha'] = alpha

        for i in range(n_samples):
            y_pred = pred(
                X[i],
                best_clf['feature_index'],
                best_clf['threshold'],
                best_clf['polarity']
            )
            w[i] = w[i] * np.exp(-alpha * y[i] * y_pred)

        w /= np.sum(w)

        clfs.append(best_clf)

    return clfs