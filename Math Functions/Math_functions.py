import math
from re import L
from tkinter import Y
import statistics as st
import numpy as np
# find the distance between the two points in 3D


def finddistance(a: tuple, b: tuple) -> float:
    """ find the distance between the two points a and b in 3D coordinates

    Args:
        a (tuple): point A with x, y, z coordinates in order
        b (tuple): point B with x, y, z coordinates in order

    Returns:
        float: the distance between the two points in 3D coordinates. Must be positive.
    """
    # subtract a from b
    result_in_root = math.pow(b[0]-a[0], 2) + \
        math.pow(b[1]-a[1], 2) + math.pow(b[2]-a[2], 2)
    result = math.sqrt(result_in_root)

    result_formatted = '{:4f}'.format(result)
    return result_formatted, result_in_root


# a = (-2, 2, 0)
# b = (-1, 1, -1)
# print(f'The distance between the two points is {finddistance(a, b)}')

# cross product of two vectors
# a = [3,-3,4]
b = [6, 7, -5]
c = [8, 7, -11]
d = np.cross(b, c)
# print(np.dot(a, d))
# print(d)


list_int = [5, 6, 5]
# print(len(list_int))
# list_int.sort()

# print((sum(list_int))/len(list_int))
# print(st.mean(list_int),st.pstdev(list_int))

a = 0
for i in list_int:
    a += i
mean_value = a/len(list_int)
# print(mean_value)

stvar = 0
for i in list_int:
    stvar += (i - mean_value) * (i - mean_value)
stvar = stvar/len(list_int)

stdev = math.sqrt(stvar)
# print(f'This is the standard deviation of the list: {stdev}')

# spvar = 0
# for i in list_int:
#     spvar += (i - mean_value) * (i - mean_value)
# spvar = spvar/(len(list_int) - 1)

# spdev = math.sqrt(spvar)
# print(mean_value)
# print(f'This is the unbiased sample deviation of the list: {spdev}')

population = 80
picked = 30
p = (math.factorial(population) / (math.factorial(picked)
                                   * math.factorial(population-picked)) * math.pow(0.35, 30) * math.pow(0.65, 50))
# print(f'{p:.4f}')


def binomial_random_variable(k: int, n: int, p: float) -> int:
    """combination function: to caculate the combination of the given parameters

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
for k in range(11, 16):
    result += binomial_random_variable(k, n=15, p=0.45)
# print(f'{1-result: .4f}')

sample = [3.2, 3.5, 3.8, 4.2, 4.5]

# print(f'{math.sqrt(st.pvariance(sample)):.4f}')

# # calculate the regression slope
# x = [0, 2, 4, 6, 8]
# y = [0.8, 1.4, 3.1, 4.8, 6.2]
# n = len(x)
# xy = 0

# # using zip() to iterate two lists at the same time
# for i, j in zip(x, y):
#     xy += np.dot(i, j)  # get the sum

# # get the n*'sigma xy' value
# nsxy = n * xy
# print(nsxy)

# # get the sigma x sigma y value
# sxsy = sum(x) * sum(y)
# print(sxsy)

# # get the n * sigma x^2 value
# nsxs = 0
# sxs = 0
# for i in x:
#     sxs += math.pow(i, 2)
# nsxs = n * sxs
# print(nsxs)

# # get the square of sigma x value
# ssx = sum(x) * sum(x)
# print(ssx)

# b = (nsxy - sxsy)/(nsxs - ssx)
# print(b)

# 9.
list_x = [88, 77, 95, 79, 59, 70, 86, 94, 68, 67, 91, 81,
          77, 88, 56, 95, 86, 74, 66, 93, 84, 70, 97, 60, 83, 88]
print(f'{st.mean(list_x):.4f}')
print(f'{st.median(list_x):.4f}')
print(f'{st.mode(list_x):.4f}')

# 10.
list_10 = [4, 7, 9, 12]
print(f'{st.pstdev(list_10):.2f}')
