def integers_from_start_to_end_using_range(start, end, step):
    """return a list"""
    result = []
    for i in range(start, end, step):
        result.append(i)
    return result


def integers_from_start_to_end_using_while(start, end, step):
    """return a list"""
    result = []
    i = start
    if (step < 0):
        while (i > end):
            result.append(i)
            i += step
    else:
        while (i < end):
            result.append(i)
            i += step
    return result


def two_digit_primes():
    """
    Return a list of all two-digit-primes
    """
    result = []
    N = 100
    is_prime = [1] * N
    is_prime[0], is_prime[1] = 0, 0

    i = 2
    while ((i * i) < N):
        if (is_prime[i] == 0):
            i += 1
            continue
        j = i * 2
        while (j < N):
            is_prime[j] = 0
            j += i
        i += 1
    for i in range(10, N):
        if (is_prime[i] == 1):
            result.append(i)

    return result
