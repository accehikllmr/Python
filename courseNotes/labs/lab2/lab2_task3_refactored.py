import doctest

def whole_donuts(money: float) -> None:
    """
    Calculate number of whole donuts that can be purchased given an amount of money.

    Parameters:
        money (float): money available for purchase of donuts

    >>> whole_donuts(10.0)
    With $10.0, you can purchase 4 whole donuts.
    >>> whole_donuts(2.29)
    With $2.29, you can purchase 0 whole donuts.
    >>> whole_donuts(2.30)
    With $2.3, you can purchase 1 whole donuts.
    >>> whole_donuts(10)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to money parameter must be a non-negative float
    >>> whole_donuts(-10.0)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to money parameter must be a non-negative float
    """

    # checking parameter preconditions
    assert isinstance(money, float) and money >= 0, "argument passed to money parameter must be a non-negative float"

    # price of a single donut
    donut_price = 2.3

    # total donuts purchased with money
    donuts = int(money // donut_price)

    print(f"With ${round(money, 2)}, you can purchase {donuts} whole donuts.")

# take input from user within function call, return prints output message
whole_donuts(float(input("How much money do you have? ")))

doctest.testmod()