import doctest
from typing import Dict

def add_to_inventory(inventory: Dict[str, int], product: str, quantity: int) -> int:
    """
    Given an inventory, adds a quantity of a given product to the inventory and outputs its new total quantity.

    Parameters:
        inventory (Dict[str, int]): existing inventory, with products (keys) and respective quantities (values)
        product (str): product to which new inventory will be added
        quantity (int): quantity to be added to product inventory

    Returns:
        (int): the updated inventory for the given item

    >>> add_to_inventory({"Laptop": 20, "Smartphone": 15, "Tablet": 30, "Headphones": 10}, "Keyboard", 5)
    5
    >>> add_to_inventory({}, "Apple", 1)
    1
    >>> add_to_inventory({"Plates": 3}, "Plates", 4)
    7
    >>> add_to_inventory({"Orange": 45, "Apple": 60}, "Pear", 30)
    30
    >>> add_to_inventory({"Orange": 45, "Apple": 60}, "Apple", 30)
    90
    >>> add_to_inventory({"Orange": 45, "Apple": 60}, "Apple", -25)     #FOR SOME REASON, THIS DOES NOT WORK IF VALUE IS ABOVE 30
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to quantity parameter must be a non-negative integer
    >>> add_to_inventory({}, "", 5)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to product parameter must be a non-empty string
    >>> add_to_inventory({}, "Apple", 1.5)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to quantity parameter must be a non-negative integer
    >>> add_to_inventory({}, "Apple", -1)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to quantity parameter must be a non-negative integer
    >>> add_to_inventory({"Chocolate Cake": 3, "Cheese Cake": 5}, "Strawberry", -4)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to quantity parameter must be a non-negative integer
    """
    # COULD NOT GET THIS ASSERTION TO WORK, FOR SOME REASON
    # checking that argument passed to inventory parameter is a dictionary with string keys and int values
    # assert type(inventory) == Dict[str, int] or inventory == {}, "argument passed to inventory parameter must be a dictionary with string keys and int values"

    # checking that argument passed to product parameter is of string type
    assert type(product) == str and len(product) != 0, "argument passed to product parameter must be a non-empty string"

    # checking that argument passed to quantity parameter is of integer type
    assert type(quantity) == int and quantity >= 0, "argument passed to quantity parameter must be a non-negative integer"

    # conditionals based on whether key is already in dictionary, or not
    if product in inventory.keys():
        # updating quantity for existing product in inventory
        inventory[product] += quantity
    else:
        # adding initial quantity for a new inventory product
        inventory[product] = quantity

    return inventory[product]

doctest.testmod()