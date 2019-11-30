def last_3_characters(x):
    if (len(x) <= 3):
        return x
    else:
        startIndex = len(x) - 3
        return x[startIndex:]


def first_10_characters(x):
    if (len(x) <= 10):
        return x
    else:
        return x[:10]


def chars_4_through_10(x):
    if (len(x) <= 4):
        return ''
    elif (len(x) >= 10):
        endIndex = 10 if len(x) == 10 else 11
        return x[4: endIndex]


def str_length(x):
    return len(x)


def words(x):
    if (len(x) == 0):
        return []
    else:
        return x.split(" ")


def capitalize(x):
    if (x == ''):
        return ''
    elif (len(x) == 1):
        return x[0].upper()
    else:
        newString = x[0].upper() + x[1:]
        return newString


def to_uppercase(x):
    if (len(x) == 0):
        return ''
    else:
        return x.upper()
