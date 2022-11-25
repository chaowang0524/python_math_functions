lst = [1, 4, 6, 9, 13, 19, 20, 88, 96, 45]
# if the length of the list is even:
# swap the first and last elements, the second and the second last
# if the length of the list is odd:
# 1. swap the first and last elements, the second and the second last
# 2. keep the middle number


def freverse(a: list) -> list:
    """Output a reversed version of the given list

    Args:
        a (list): the given list

    Returns:
        list: the reversed version of the given list
    """

    # if the length of the list is even:
    if len(a) % 2 == 0:
        for i in range(1, int((len(a)/2)+1)):
            # swap the first and last elements, the second and the second last...
            # set the pointers
            a[i-1], a[-i] = a[-i], a[i-1]
    else:
        for i in range(1, (len(a)//2)+1):
            if a[i-1] != a[(len(a)//2)+1]:
                a[i-1], a[-i] = a[-i], a[i-1]
    return(a)


print(freverse(lst))
