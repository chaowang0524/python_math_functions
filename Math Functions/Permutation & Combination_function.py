from Factorial import *


def find_combination(n, k):
    result = factorial(n) / (factorial(k) * factorial(n-k))
    return result


def find_permutation(n, k):
    result = factorial(n) / factorial(n-k)
    return result


result = []
for i in range(1, 101):

    if i % 10 == 0 or i % 7 == 0:
        result.append(i)
# print(len(result))


# print(find_permutation(15000, 3)/1000000000)
# print(find_permutation(15000, 4)/1000000000)
# print(find_permutation(15000, 5)/1000000000)
# print(find_combination(26, 6))
