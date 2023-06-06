import numpy as np

p = [0.25, 0.5, 0.25]
X = [1, 2, 3]
X_mean = np.sum([i * j for i, j in zip(X, p)])
N = 100

n_iter = 1000
count = 0
for _ in range(n_iter):
    X_bar = np.mean(np.random.choice(X, N, p=p))
    count += 1 if np.abs(X_bar - X_mean) <= 0.1 else 0
print(count)
