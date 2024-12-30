import doctest

def is_even(num: int) -> bool:
    """
    Determines whether a number is even or not.

    Parameters:
        num (int): number to be evaluated for parity

    >>> is_even(2)
    True
    >>> is_even(1)
    False
    >>> is_even(1.1)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to num parameter must be an integer object
    >>> is_even('1')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to num parameter must be an integer object
    """

    # checking preconditions
    assert isinstance(num, int), "argument passed to num parameter must be an integer object"

    #the remainder of dividing an even number by 2, is zero
    return num % 2 == 0

if __name__ == 'main':
    doctest.testmod()