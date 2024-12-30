import doctest

def calculate_average(numbers_str: str) -> float:
    """
    Calculates the average of n numbers in the specified string format.

    Parameters:
        numbers_str (str): A string containing n integers separated by '|', with possible spaces.

    Returns:
        (float): The average of the integers.

    >>> calculate_average('1')
    1.0
    >>> calculate_average('1|2|3')
    2.0
    >>> calculate_average('1|2|3|4|5')
    3.0
    >>> calculate_average('2 | 10|  5|7|11')
    7.0
    >>> calculate_average('1|')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to numbers_str parameter must not end with the | symbol
    >>> calculate_average('1||2')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to numbers_str parameter must have at most one | symbol between any two digits
    >>> calculate_average('1|||3||||4')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to numbers_str parameter must have at most one | symbol between any two digits
    >>> calculate_average('1|2|3.0')
    Traceback (most recent call last):
    ...
    AssertionError: other than the | symbol, argument passed to numbers_str parameter must contain digits
    """

    # checking that argument passed to function parameter is of string type
    assert isinstance(numbers_str, str), "argument passed to numbers_str parameter must be a string object"

    # stripping whitespace from string, to facilitate assertion checks below (must come after checking for string object)
    numbers_str = numbers_str.strip()

    # checking that last element of list won't be the empty string (occurs when input string terminates with vertical bar)
    assert numbers_str[-1] != '|', "argument passed to numbers_str parameter must not end with the | symbol"

    # creating list object from string, separating string using '|' character as delimiter
    numbers = numbers_str.split('|')

    # checking that there are not too many vertical bars in the input string, cannot check when converted to list since generates empty strings, using loop to check for all lengths of | strings
    for i in range(2, len(numbers_str)):
        assert i * '|' not in numbers_str, "argument passed to numbers_str parameter must have at most one | symbol between any two digits"

    # initializing variable which tracks sum of numbers in list
    total = 0

    # iterating through list to add each number (this time, using a loop)
    for num in numbers:
        # checking that items in list are digits, could do this outside, but then would need another loop to iterate through list
        assert num.strip().isdigit(), "other than the | symbol, argument passed to numbers_str parameter must contain digits"
        # stripping whitespace around numbers, before converting to integers
        total += int(num.strip())

    # calculating average based on len of list with numbers
    average = total / len(numbers)

    return average

doctest.testmod()