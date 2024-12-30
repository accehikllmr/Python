import doctest
from typing import Dict

def max_min_average(all_nums: Dict[str, any]) -> float:
    """
    Calculates the average of two values, the maximum and the minimum in a dictionary of four numbers.

    Parameters:
        all_nums (Dict[str, str]): dictionary containing four numbers, positive or negative

    Returns:
        (float): average value of maximum and minimum values in dictionary

    >>> max_min_average({'first_number': '1', 'second_number': '4', 'third_number': '2', 'fourth_number': '3'})
    2.5
    >>> max_min_average({'first_number': '0', 'second_number': '0', 'third_number': '0', 'fourth_number': '0'})
    0.0
    >>> max_min_average({'first_number': '-1', 'second_number': '-4', 'third_number': '-2', 'fourth_number': '-3'})
    -2.5
    >>> max_min_average({'first_number': '1.0', 'second_number': '4.0', 'third_number': '2.0', 'fourth_number': '3.0'})
    2.5
    >>> max_min_average({'first_number': '0.0', 'second_number': '0.0', 'third_number': '0.0', 'fourth_number': '0.0'})
    0.0
    >>> max_min_average({'first_number': '-1.0', 'second_number': '-4.0', 'third_number': '-2.0', 'fourth_number': '-3.0'})
    -2.5
    >>> max_min_average({'first_number': '1', 'second_number': 'bob', 'third_number': '-2.0', 'fourth_number': '3.0'})
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to all_nums parameter must have integers or floats for its values
    """

    # try converting values of dictionary into float, before assertions, otherwise will skip and not throw exception
    for key, value in all_nums.items():
        # checking if all characters in value string are digits, save for the decimal point and the negative sign
        if value.replace('.', '').replace('-', '').isdigit():
            # updating value in dictionary, using key and new value pairing
            all_nums[key] = float(value)

    # checking that value string were converted to float, but not string values for dictionary since these are hardcoded
    for val in all_nums.values():
        assert isinstance(val, float), "argument passed to all_nums parameter must have integers or floats for its values"

    # extracting the maximum and minimum values from the dictionary values
    maximum = max(all_nums.values())
    minimum = min(all_nums.values())

    # calculate and return average, leave print statement out of function this time
    return (maximum + minimum) / 2

# instantiating a dictionary, since there is a defined number of user inputs required
numbers = {'first_number': 0, 'second_number': 0, 'third_number': 0, 'fourth_number': 0}

# iterate over dictionary to add numbers
for num in numbers.keys():
    # not converting to float here, better to handle exceptions within the function itself (can write own error message)
    numbers[num] = (input(f"{num}: "))

# output result to user, function call within print statement
print(f"The average of the maximum and minimum values of the numbers is {max_min_average(numbers)}.")

doctest.testmod()