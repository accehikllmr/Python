import doctest

ALLOWED_NUMBER = 5

def calculate_average(numbers_str: str) -> float:
    """
    Calculates the average of numbers in the specified string format.

    Parameters:
        numbers_str (str): A string containing 5 numbers separated by '|',
        with possible spaces.

    Returns:
        float: The average of the numbers.

    >>> calculate_average('1|2|3|4|5')
    3.0
    >>> calculate_average('2 | 10|  5|7|11')
    7.0
    """
    # checking that argument passed to function parameter is of string type
    assert type(numbers_str) == str, "The input must be a string"

    # creating list object from string, separating string using '|' character as delimiter
    numbers = numbers_str.split('|')

    # checking that input string contains exactly 5 numbers
    assert len(numbers) == ALLOWED_NUMBER, "Input string must contain exactly 5 numbers."

    # initializing variable which tracks sum of numbers in list
    total = 0

    # iterating through list to add each number (should use loop instead)
    total = total + int(numbers[0].strip())
    total = total + int(numbers[1].strip())
    total = total + int(numbers[2].strip())
    total = total + int(numbers[3].strip())
    total = total + int(numbers[4].strip())

    # calculating average based on len of list with numbers
    average = total / len(numbers)

    return average

doctest.testmod()