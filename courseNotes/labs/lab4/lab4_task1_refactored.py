import doctest

def fruit_price(num_apples: int, num_peaches: int, num_watermelon: int) -> float:
    """
    Return the total price given the number of each fruit to purchase.

    Parameters:
        num_apples (int): number of apples purchased
        num_peaches (int): number of peaches purchased
        num_watermelon (int): number of watermelon purchased

    Returns:
        (float): total price to pay for bunches of fruits

    >>> fruit_price(1, 2, 3)
    34.89
    >>> fruit_price(0, 0, 0)
    0.0
    >>> fruit_price(1.5, 2, 3)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to num_apples parameter must be a non-negative integer
    >>> fruit_price(3, '2', 5)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to num_peaches parameter must be a non-negative integer
    >>> fruit_price(1, -3, -5)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to num_peaches parameter must be a non-negative integer
    >>> fruit_price(1, 3, -5.5)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to num_watermelon parameter must be a non-negative integer
    """

    # using isinstance() is preferable to using type(), the latter is bad form, can also combine assertion statements
    assert isinstance(num_apples, int) and num_apples >= 0, "argument passed to num_apples parameter must be a non-negative integer"
    assert isinstance(num_peaches, int) and num_peaches >= 0, "argument passed to num_peaches parameter must be a non-negative integer"
    assert isinstance(num_watermelon, int) and num_watermelon >= 0, "argument passed to num_watermelon parameter must be a non-negative integer"

    # creating dictionary object to associate fruits with respective unit prices multiplied by quantity, after assertions to avoid type errors
    bunch_prices = {'apples': num_apples * 2.94, 'peaches': num_peaches * 3.99, 'watermelon': num_watermelon * 7.99}

    #calculate the total price by looping through dictionary
    total_price = 0
    # iterating through keys, but only in order to practice using a specific syntax
    for fruit in bunch_prices.keys():
        # getting value from dictionary by using key
        total_price += bunch_prices[fruit]

    #return the total price
    return total_price

doctest.testmod()