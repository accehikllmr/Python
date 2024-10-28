import doctest

def need_to_buy_ticket(age: float, height: float) -> bool:
    """
    Determines whether a child needs to buy a ticket in order to enter the theme park.

    Preconditions:  age     float > 0
                    height  float > 0

    >>> need_to_buy_ticket(6, 120)
    False
    >>> need_to_buy_ticket(7, 121)
    True
    >>> need_to_buy_ticket(7, 120)
    True
    >>> need_to_buy_ticket(6, 121)
    True
    >>> need_to_buy_ticket(0, 150)
    Traceback (most recent call last):
    ...
    AssertionError: age and height must both be non-negative integers
    >>> need_to_buy_ticket(10, 0)
    Traceback (most recent call last):
    ...
    AssertionError: age and height must both be non-negative integers
    >>> need_to_buy_ticket('a', 150)
    Traceback (most recent call last):
    ...
    AssertionError: argument with invalid data type passed to age parameter
    >>> need_to_buy_ticket(10, 'a')
    Traceback (most recent call last):
    ...
    AssertionError: argument with invalid data type passed to height parameter
    """

    assert type(age) == int or type(age) == float, "argument with invalid data type passed to age parameter"
    assert type(height) == int or type(height) == float, "argument with invalid data type passed to height parameter"

    assert age > 0 and height > 0, "age and height must both be non-negative integers"

    return age > 6 or height > 120

doctest.testmod()