import doctest

def is_even(num: int) -> bool:
    """
    Determines whether a number is even or odd.

    Preconditions:     num     int

    >>> is_even(2)
    True
    >>> is_even(1)
    False
    >>> is_even(1.1)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for num parameter
    >>> is_even('1')
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for num parameter
    """

    assert type(num) == int, "invalid data type for num parameter"

    #the remainder of dividing an even number by 2, is zero
    return num % 2 == 0

if __name__ == 'main':
    doctest.testmod()