def even_numbers(a: int, b: int) -> list:
    """Find all even numbers in the given interval

    Args:
        a (int): the start of the interval (included)
        b (int): the end of the interval (included)

    Returns:
        list: the result is in the form of a list
    """

    def is_even_number(x):
        if x == 0 or x % 2 == 0:
            return x

    result = [is_even_number(x) for x in range(a, b+1)]
    result = [i for i in result if i is not None]

    # one line code
    result_short = [item for item in range(
        a, b+1) if item % 2 == 0]
    return result, result_short


print(even_numbers(4, 15))
