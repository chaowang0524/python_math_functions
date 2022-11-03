def sum_of_list(x: list) -> int:  # like built-in function `sum`
    result = 0
    for i in x:
        result += i
    return result


print(sum_of_list([5, 6, 7, 8]))
