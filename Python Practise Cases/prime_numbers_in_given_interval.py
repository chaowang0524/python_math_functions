def prime(a, b):
    """
    Print all prime numbers in the given interval into a list
    Args:
        a (_type_): The interval includes a
        b (_type_): The interval includes b
    """

    # Check if the number is a prime.
    # Check if it's divisible by any number between 0 and itself.
    def is_prime(x):
        # 1 and 2 are prime numbers:
        if x == 1 or x == 2:
            return x
        # Check the rest of the numbers
        for number in range(2, x):
            if x % number == 0:
                return None
        else:
            return x
    # print out the list
    prime_list = [is_prime(x) for x in range(a, b+1)]  # `b+1` to include b
    # Remove all None values
    prime_list = [i for i in prime_list if i is not None]
    return prime_list


print(prime(1, 100))

# correct algorithm:


def is_prime(x):
    # 0, 1 and negative numbers are not prime numbers
    if x <= 1:
        return False
    # 2 is prime numbers:
    elif x == 2:
        return True
    else:
        # Check the rest of the numbers
        for number in range(2, x):
            if x % number == 0:
                return False
        else:
            return True
