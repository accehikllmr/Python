################################### TASK 2 ###################################
import doctest

### Starting code ###
def repeat_sum(num:int) -> int:
    """
    Repeatedly sums up terms up to and including num
        * if num is even, sum up all even numbers
        * if num is odd, sum up all odd numbers

    >>> repeat_sum(0)
    0
    >>> repeat_sum(10)
    30
    >>> repeat_sum(9)
    25
    >>> repeat_sum(20)
    110
    >>> repeat_sum(33)
    289
    >>> repeat_sum(1.0)
    Traceback (most recent call last):
    ...
    AssertionError: num must be a non-negative int
    """
    # checking if argument passed to function is a non-negative integer
    assert type(num) == int and num >= 0, "num must be a non-negative int"

    # odd numbers start summation at 1
    if num % 2 != 0:
        start = 1
    # even numbers start summation at 2
    else:
        start = 2

    # summation of all numbers
    total = 0

    # looping through all numbers, odd or even, until end number, increment of 2 to have only odd or even
    for i in range(start, num + 1, 2):
        # add number to total of summation
        total += i

    # returning summation of numbers
    return total

doctest.testmod()