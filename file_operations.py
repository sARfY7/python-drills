"""
Implement the below file operations.
Close the file after each operation.
"""


def read_file(path):
    file = open(path, "r")
    data = "".join(file.readlines())
    file.close()
    return data


def write_to_file(path, s):
    file = open(path, "w")
    file.write(s)
    file.close()


def append_to_file(path, s):
    file = open(path, "a")
    file.write(s)
    file.close()


def numbers_and_squares(n, file_path):
    """
    Save the first `n` natural numbers and their squares into a file in the csv format.

    Example file content for `n=3`:

    1,1
    2,4
    3,9
    """
    file = open(file_path, "w")
    for i in range(1, n + 1):
        string = str(i) + "," + str(i**2) + "\n"
        file.write(string)
    file.close()
