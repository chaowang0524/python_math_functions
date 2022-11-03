def remove_items(lista: list, listb: list) -> list:
    result = [i for i in lista if i not in listb]
    return result


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y = [1, 2, 3, 4, 5, 6, 7, ]
print(remove_items(x, y))
