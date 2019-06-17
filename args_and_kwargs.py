def add3(a, b, c):
    return sum(a, b, c)


def unpacking1():
    items = [1, 2, 3]
    # Call add3 by passing unpacking items


def unpacking2():
    kwargs = {'a': 1, 'b': 2, 'c': 3}
    # Call add3 by unpacking kwargs


def call_function_using_keyword_arguments_example():
    a = 1
    b = 2
    c = 3
    # Call add3 by passing a, b and c as keyword arguments


def add_n():
    """
    Define `add_n` so that it accepts
    any number of arguments and
    returns the sum of all the arguments
    """
    pass


def add_kwargs():
    """
    Define `add_kwargs` so that it accepts a and b as keyword arguments
    and returns the sume of these arguments.

    Ensure the function raises an exception when arguments apart from a and b
    are passed to `add_kwargs`
    """
    pass


def universal_acceptor():
    """
    Define `universal_acceptor` so that it accepts any kind of
    arguments and keyword-arguments,
    and prints the arguments and keyword-arguments.
    """
    pass
