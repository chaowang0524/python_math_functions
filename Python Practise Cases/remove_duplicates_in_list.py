def remove_duplicates(lista: list) -> list:
    # create a empty list.
    # put items from lista to the empty list to remove duplicates
    result = []
    for i in lista:
        if i not in result:
            result.append(i)

    return result


x = [1, 23, 4, 5, 6, 7, 6, 7, 8, 9, 10, 10, 23, 2, 4, 5, 6, 7, 8, 9, 10, ]

print(remove_duplicates(x))


# or just use set

print(list(set(x)))
