import numpy as np
import pandas as pd
from scipy.spatial import cKDTree as KDTree


def load_dataset(dataset):
    df = pd.read_csv(dataset)
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    return X, y


def evaluate(weights, X, y):
    """Evaluate a solution transforming the input data
    and calculatig the accuracy.
    Returns:
        the fitness value for the specified weights based on
        the input and labels data.
    """
    X_transformed = (X * weights)[:, weights > 0.2]
    kdtree = KDTree(X_transformed)
    neighbours = kdtree.query(X_transformed, k=2)[1][:, 1]
    accuracy = np.mean(y[neighbours] == y)
    reduction = np.mean(weights < 0.2)
    return (accuracy + reduction) / 2


def local_search(X, y, max_neighbours, sigma, seed):
    """Local Search Algorithm
    Keyword arguments:
    X -- Train input
    y -- Train labels
    max_neighbours -- Max number of neighbours to explore.
    sigma -- Standard deviation of Gaussian mutation.
    seed -- Seed to initialize the random generator.
            It is recommended to specify this in order to replicate
            the experiment across executions.
    """
    n_features = X.shape[1]
    np.random.seed(seed)
    weights = np.random.rand(n_features)
    fitness = evaluate(weights, X, y)
    trace = np.zeros(max_neighbours)
    n_generated = 0
    no_improvement = 0
    while n_generated < max_neighbours:
        trace[n_generated] = fitness
        w_prime = np.copy(weights)
        for k in np.random.permutation(n_features):
            n_generated += 1
            no_improvement += 1
            last_state = w_prime[k]
            w_prime[k] = np.clip(last_state + np.random.normal(0, sigma), 0, 1)
            f = evaluate(w_prime, X, y)
            if fitness < f:
                weights = w_prime
                fitness = f
                no_improvement = 0
                break
            else:
                w_prime[k] = last_state
            if n_generated > max_neighbours or no_improvement >= (20 * n_features):
                return weights, trace[trace > 0], n_generated
    return weights, trace[trace > 0], n_generated


class LocalSearch():
    """
    Docstring: Wrapper class for Local Search algorithm that provided
    sklearn-based syntax.
    """

    def __init__(self, threshold=0.2, max_neighbours=15000, sigma=0.3, seed=1):
        self.threshold = threshold
        self.max_neighbours = max_neighbours
        self.sigma = sigma
        self.seed = seed
        self.feature_importances = []
        self.trace = []
        self.neighbors_generated = 0
        self.reduction = 0

    def fit(self, X, y):
        result = local_search(X, y, self.max_neighbours, self.sigma, self.seed)
        self.feature_importances = result[0]
        self.trace = result[1]
        self.neighbors_generated = result[2]
        self.reduction = np.sum(self.feature_importances < self.threshold)
        self.reduction /= len(self.feature_importances)

    def transform(self, X):
        return (X * self.feature_importances
                )[:, self.feature_importances > self.threshold]

    def fit_transform(self, X, y):
        self.fit(X, y)
        return self.transform(X)


if __name__ == '__main__':
    X, y = load_dataset('./texture.csv')
    ls = LocalSearch()
    ls.fit(X, y)
    fitness = evaluate(ls.feature_importances, X, y)
    print(fitness)