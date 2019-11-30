from copy import copy


def sum_items_in_list(x):
    if (len(x) == 0):
        return 0
    else:
        return sum(x)


def list_length(x):
    return len(x)


def last_three_items(x):
    if (len(x) <= 3):
        return x
    else:
        startIndex = len(x) - 3
        return x[startIndex:]


def first_three_items(x):
    if (len(x) <= 3):
        return x
    else:
        return x[:3]


def sort_list(x):
    if (len(x) <= 1):
        return x
    else:
        return sorted(x)


def append_item(x, item):
    x.append(item)
    return x


def remove_last_item(x):
    x.pop()
    return x


def count_occurrences(x, item):
    return x.count(item)


def is_item_present_in_list(x, item):
    if (item in x):
        return True
    else:
        return False


def append_all_items_of_y_to_x(x, y):
    """
    x and y are lists
    """
    if ((len(x) and len(x)) == 0):
        return []
    else:
        x.extend(y)
        return x


def list_copy(x):
    """
    Create a shallow copy of x
    """
    return copy(x)
