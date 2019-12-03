def word_count(s):
    """
    Find the number of occurrences of each word
    in a string(Don't consider punctuation characters)
    """
    punctuations = [",", "."]
    result = {}
    for word in s.split(" "):
        unpunctuated_word = ""
        for char in word:
            if (char not in punctuations):
                unpunctuated_word += char
        if (unpunctuated_word in result):
            result[unpunctuated_word] += 1
        else:
            result[unpunctuated_word] = 1
    return result


def dict_items(d):
    """
    Return a list of all the items - (key, value) pair tuples - of the dictionary, `d`
    """
    result = []
    for k in d:
        result.append((k, d[k]))
    return result


def dict_items_sorted(d):
    """
    Return a list of all the items - (key, value) pair tuples - of the dictionary, `d`
    sorted by `d`'s keys
    """
    result = []
    sorted_keys = sorted(list(d.keys()))
    for k in sorted_keys:
        result.append((k, d[k]))
    return result
