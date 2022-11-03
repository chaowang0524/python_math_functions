import math


def square_sum(x: int) -> int:
    """sum all the squares values of all the numbers before and include the given number

    Args:
        x (int): the given number

    Returns:
        int: all the squares values of the numbers before and include the given number
    """
    result = 0
    for i in range(x+1):
        result += i*i

    return result


print(square_sum(5))
