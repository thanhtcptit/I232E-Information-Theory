import numpy as np


def entropy(p):
    return -np.sum(p * np.log2(p))


p = [1/3] * 3
print(entropy(p))