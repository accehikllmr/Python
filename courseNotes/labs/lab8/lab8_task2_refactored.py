import doctest

# added string output so that user sees the entire addition, with all terms, leading to the result
def repeat_sum(num:int) -> str:
    """
    Repeatedly sums terms up to and including num
        * if num is even, sum up all even numbers
        * if num is odd, sum up all odd numbers

    Parameters:
        num (int): number up to which sum is calculated

    Returns:
        (int): sum of all numbers up to and including given number
        (str): representation of sum for user

    >>> repeat_sum(0)
    '0 = 0'
    >>> repeat_sum(10)
    '2 + 4 + 6 + 8 + 10 = 30'
    >>> repeat_sum(9)
    '1 + 3 + 5 + 7 + 9 = 25'
    >>> repeat_sum(20)
    '2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20 = 110'
    >>> repeat_sum(33)
    '1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 + 23 + 25 + 27 + 29 + 31 + 33 = 289'
    >>> repeat_sum(1.0)
    Traceback (most recent call last):
    ...
    AssertionError: num must be a non-negative int
    """
    # checking if argument passed to function is a non-negative integer
    assert isinstance(num, int) and num >= 0, "num must be a non-negative int"

    # instantiating string object for output statement
    string_sum = ""

    # odd numbers start summation at 1
    if num % 2 != 0:
        start = 1
    # even numbers start summation at 2
    else:
        start = 2
        # leave string empty if sum is equal to zero
        if num == 0:
            # others do not need starter string, since they will update through the loop
            string_sum = '0'

    # summation of all numbers
    total = 0

    # looping through all numbers, odd or even, until end number, increment of 2 to have only odd or even
    for i in range(start, num + 1, 2):
        # add number to total of summation
        total += i
        if i == num:
            # last number in summation does not need addition sign after it
            string_sum += f"{i}"
        else:
            # all prior numbers need addition sign
            string_sum += f'{i} + '

    # returning summation of numbers, but in string form
    return f"{string_sum} = {total}"

doctest.testmod()