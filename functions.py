def is_prime(n):
    """
    Check whether a number is prime or not
    """
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


def n_digit_primes(digit=2):
    """
    Return a list of `n_digit` primes using the `is_prime` function.

    Set the default value of the `digit` argument to 2
    """
    result = []
    first_num_in_digit = '1'
    for i in range(1, digit):
        first_num_in_digit += '0'
    first_num_in_digit = int(first_num_in_digit)
    last_num_in_digit = int(str(first_num_in_digit) + '0')
    for i in range(first_num_in_digit, last_num_in_digit):
        if (is_prime(i)):
            if (i != 1):
                result.append(i)
    return result
