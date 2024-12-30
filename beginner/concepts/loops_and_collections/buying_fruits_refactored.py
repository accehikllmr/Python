import doctest

def bunch_price(quantity: int, price: float) -> float:
    """
    Calculates the price for a bunch of fruit or a single kind.

    >>> bunch_price(0, 1.0)
    0.0
    >>> bunch_price(2, 5.0)
    10.0
    >>> bunch_price(2.0, 5.0)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for quantity parameter
    >>> bunch_price(2, 5)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for price parameter
    >>> bunch_price(-2, 5.0)
    Traceback (most recent call last):
    ...
    AssertionError: quantity of fruits must be greater than or equal to zero
    >>> bunch_price(2, 0.0)
    Traceback (most recent call last):
    ...
    AssertionError: price of fruits must be greater than zero
    """

    #checking that arguments passed to function are of correct data type
    assert isinstance(quantity, int), "invalid data type for quantity parameter"
    assert isinstance(price, float), "invalid data type for price parameter"

    #checking that value for quantity is non-negative
    assert quantity >= 0, "quantity of fruits must be greater than or equal to zero"

    #checking that value for price is greater than zero
    assert price > 0, "price of fruits must be greater than zero"

    #price of the bunch, given the number of fruits and unit price, not rounded to maximize dales
    return quantity * price

def add_to_total(all_prices: float, some_price: float) -> float:
    """
    Updating total price given a newly purchased bunch of fruit.

    Parameters:
         all_prices (float): running total cost of all fruit bunches
         some_price (float): cost of fruit bunch being added to total

    Returns:
        (float): updated total cost of all fruit bunches

    >>> add_to_total(5, 5)
    10
    >>> add_to_total(0, 0)
    0
    """

    # no assertions tests since already guaranteed valid input from previous function

    return all_prices + some_price

# associating fruit type with its price
fruit_inventory = {'apple': 2.94, 'peach': 3.99, 'watermelon': 7.99}

# instantiating string object for output to user
output_message = f"\nFor "

# instantiating float object for total price of all fruit bunches
total_price = 0.0

# iterate through every type of fruit in inventory
for fruit in fruit_inventory.keys():
    # get user input for quantity of each fruit
    num_fruit = int(input(f"How many {fruit}s? "))
    # calculate price for a bunch of fruit
    price_fruit = bunch_price(num_fruit, fruit_inventory[fruit])
    # adding to total price of fruit bunches
    total_price = add_to_total(total_price, price_fruit)
    # updating string with new value
    output_message += f"{num_fruit} {fruit}, "

#output the total price to the user, added sentence to explain result (error: when only one fruit, still plural)
print(output_message + f"the total cost is ${round(total_price,2)}.")

doctest.testmod()