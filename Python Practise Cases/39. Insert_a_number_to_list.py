# insert a number into the list and keep the ascending order
# e.g. the list a
lst = [1, 4, 6, 9, 13, 19]
# e.g. insert n = 11
# compare n with a[i-2], it's smaller
# so :
# 1. swap a[i-2] with a[i-1] to be a = [1, 4, 6, 9, 13, 0, 19]
# 2. replace a[i-2] with n to be a = [1, 4, 6, 9, 13, 11, 19]
# 3. because now n is at a[i-2], compare n with a[i-3]
# because n < a[i-3], then:
# 1. swap a[i-2] and a[i-3] to be a = [1, 4, 6, 9, 11, 13, 19]


def insert_number(n: int, a: list) -> list:
    """insert an integer into a list without breaking its ascending order

    Args:
        n (int): the integer to be inserted
        a (list): the existing list

    Returns:
        list: new list in ascending order
    """

    a.append(0)
    # print("Appended with 0: ", a)
    i = len(a)  # get the length

    # compare n with the last number in the list,
    # if n is smaller than the last number in the list,
    # move the compared number to its right one slot:

    # a[i-1] is 0 and a[i-2] is the last number in the list

    # set the pointers:
    x = 1  # the empty slot
    y = 2  # the number to be moved

    # if n is greater than or equal to the last number, replace the appended 0 with it

    if n > a[i-2] or n == a[i-2]:
        # print(n, a[i-2])
        a[i-1] = n
        # print(a)
    else:
        # if n is smaller than the last number,
        # start comparing till it is greater than or equal to the last number
        while n < a[i-y]:  # compare n with a[i-2], n is smaller
            # swap a[i-2] with a[i-1]
            a[i-x], a[i-y] = a[i-y], a[i-x]
            a[i-y] = n
            x += 1
            y += 1
            if y > len(a):
                break
        # if n is great than or equal to compared number:
        # replace it with n
    return a


print(insert_number(5, lst))
