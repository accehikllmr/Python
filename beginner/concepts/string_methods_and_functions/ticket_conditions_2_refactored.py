import doctest

def need_to_buy_ticket(age: float, height: float) -> bool:
    """
    Determines whether a child needs to buy a ticket in order to enter the theme park.

    Parameters:
        age (float): age of child, in years
        height (float): height of child, in centimeters

    Returns:
        (bool): whether the child needs to purchase a ticket

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
    AssertionError: argument passed to age parameter must be a positive integer or float
    >>> need_to_buy_ticket(10, 0)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to height parameter must be a positive integer or float
    >>> need_to_buy_ticket('a', 150)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to age parameter must be a positive integer or float
    >>> need_to_buy_ticket(10, 'a')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to height parameter must be a positive integer or float
    """

    # using isinstance instead of type, latter is bad form, note that new approach allows comparison to multiple classes
    assert isinstance(age, int or float) and age > 0, "argument passed to age parameter must be a positive integer or float"
    assert isinstance(height, int or float) and height > 0, "argument passed to height parameter must be a positive integer or float"

    # remember, boolean values can be achieved without using conditionals
    return age > 6 or height > 120

doctest.testmod()