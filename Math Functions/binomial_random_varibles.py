import math
import statistics as st
import numpy as np


def binomial_random_variable(k: float, n: float, p: float) -> int:
    """binomial_random_variable function: to caculate the binomial_random_variable
     of the given parameters

    Args:
        k (int): the times of the success
        n (int): total times of experiment
        p (float): the success probability

    Returns:
        int: the number of the possible combinations
    """
    # the combination
    c = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    # binomial_random_variable probability
    a = c * math.pow(p, k)*math.pow(1-p, n-k)
    return a


result = 0.0
for k in range(0, 10):
    result += binomial_random_variable(k, n=20, p=0.32)
print(f'{1-result: .4f}')
