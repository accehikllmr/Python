import doctest
from typing import Dict

class Inventory:
    """ A class representing an inventory of products """

    # not adding parameters, since want to build up inventory incrementally, using methods
    def __init__(self) -> None:
        """
        Instantiates an inventory object.

        >>> inventory = Inventory()
        >>> inventory._inventory
        {}
        >>> print(inventory)
        Inventory({})
        """

        self._inventory = {}

    def __str__(self) -> str:
        """
        Represents inventory object as a string.

        Returns:
            (str): string representation of inventory object

        >>> inventory = Inventory()
        >>> inventory.__str__()
        'Inventory({})'
        """

        return f"Inventory({self._inventory})"

    def get_inventory(self) -> Dict[str, Dict[str, int]]:
        """
        Retrieves the dictionary object for the inventory.

        Returns:
            (Dict[str, int]): dictionary object containing all inventory

        >>> inventory = Inventory()
        >>> inventory.get_inventory()
        {}
        """

        return self._inventory

    def set_inventory(self, new_inventory: Dict[str, Dict[str, int]]) -> str:
        """
        Updates all dictionary object items in the inventory.

        Parameters:
            (Dict[str, int]): dictionary object containing new inventory items

        Returns:
            (str): string representation of updated inventory

        >>> inventory = Inventory()
        >>> inventory.set_inventory({'000': {"Laptop": 20}, '001': {"Smartphone": 15}, '002': {"Tablet": 30}, '003': {"Headphones": 10}})
        "Updated inventory: {'000': {'laptop': 20}, '001': {'smartphone': 15}, '002': {'tablet': 30}, '003': {'headphones': 10}}"
        >>> inventory.set_inventory(4)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to new_inventory parameter must be a dictionary object
        >>> inventory.set_inventory({'000': {"Laptop": 20}, '001': {"Smartphone": 15}, '002': {"": 30}, '003': {"Headphones": 10}})
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to new_inventory parameter must have only alphabetic characters for its inner keys
        >>> inventory.set_inventory({'000': {"Laptop": 20}, '001': {"Smartphone": 15}, '': {"Tablet": 30}, '003': {"Headphones": 10}})
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to new_inventory parameter must have only numeric characters for its outer keys
        >>> inventory.set_inventory({'000': {"Laptop": 20}, '001': {"Smartphone": 15}, 'abc': {"Tablet": 30}, '003': {"Headphones": 10}})
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to new_inventory parameter must have only numeric characters for its outer keys
        >>> inventory.set_inventory({'000': {"Laptop": 20}, '001': {"Smartphone": 15}, '002': {"Tab$let": 30}, '003': {"Headphones": 10}})
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to new_inventory parameter must have only alphabetic characters for its inner keys
        >>> inventory.set_inventory({'000': {"Laptop": 20}, '001': {"Smartphone": 15}, '002': {"Tablet": 30.0}, '003': {"Headphones": 10}})
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to new_inventory parameter must have non-negative integers for its inner values
        >>> inventory.set_inventory({'000': {"Laptop": 20}, '001': {"Smartphone": 15}, '002': {"Tablet": -30}, '003': {"Headphones": 10}})
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to new_inventory parameter must have non-negative integers for its inner values
        >>> inventory.set_inventory({'000': {"Laptop": 20}, '001': {"Smartphone": 15}, '002': ("Tablet", 30), '003': {"Headphones": 10}})
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to new_inventory parameter must have non-empty dictionary objects for its outer values
        >>> inventory.set_inventory({'000': {"Laptop": 20}, '001': {"Smartphone": 15}, '002': {}, '003': {"Headphones": 10}})
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to new_inventory parameter must have non-empty dictionary objects for its outer values
        """

        # validating arguments
        assert isinstance(new_inventory, dict), "argument passed to new_inventory parameter must be a dictionary object"

        for item in new_inventory.items():
            assert isinstance(item[0], str) and item[0].isdigit() and len(item[0]) != 0, "argument passed to new_inventory parameter must have only numeric characters for its outer keys"
            assert isinstance(item[1], dict) and item[1] != {}, "argument passed to new_inventory parameter must have non-empty dictionary objects for its outer values"
            for pair in item[1].items():
                assert isinstance(pair[0], str) and pair[0].isalpha() and len(pair[0]) != 0, "argument passed to new_inventory parameter must have only alphabetic characters for its inner keys"
                assert isinstance(pair[1], int) and pair[1] >= 0, "argument passed to new_inventory parameter must have non-negative integers for its inner values"

        # iterate through outer items of dictionary, which contain str dict pairs
        for outer_item in new_inventory.items():
            # remove item from passed dictionary, assigned to variable to preserve its data (cannot pop same item twice)
            item = outer_item[1].popitem()
            # changing to lowercase to harmonize all keys
            key = item[0].lower()
            value = item[1]
            # pairing code with dictionary made from popped item
            self._inventory[outer_item[0]] = {key: value}

        return f"Updated inventory: {self._inventory}"

    def add_product(self, product: str) -> str:
        """
        Adds a product to the inventory.

        Parameters:
            product (str): product to be added to the store inventory

        Returns:
            (str): string representation of updated inventory

        >>> inventory = Inventory()
        >>> inventory.set_inventory({"Laptop": 20, "Smartphone": 15, "Tablet": 30, "Headphones": 10})
        "Updated inventory: {'laptop': 20, 'smartphone': 15, 'tablet': 30, 'headphones': 10}"
        >>> inventory.add_product("Brickphone")
        "Updated inventory: {'laptop': 20, 'smartphone': 15, 'tablet': 30, 'headphones': 10, 'brickphone': 0}"
        >>> inventory.add_product("Key3oard")
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to product parameter must have only alphabetic characters
        >>> inventory.add_product("")
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to product parameter must have only alphabetic characters
        >>> inventory.add_product("2")
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to product parameter must have only alphabetic characters
        >>> inventory.add_product("Laptop")
        Traceback (most recent call last):
        ...
        AssertionError: product already exists in the inventory
        >>> inventory.add_product("laptop")
        Traceback (most recent call last):
        ...
        AssertionError: product already exists in the inventory
        """

        # validating arguments
        assert isinstance(product,str) and product.isalpha() and len(product) != 0, "argument passed to product parameter must have only alphabetic characters"

        # checking for lowercase product, since all inventory when added or updated is set to lowercase
        assert product.lower() not in self._inventory.keys(), "product already exists in the inventory"

        self._inventory[product.lower()] = 0

        return f"Updated inventory: {self._inventory}"

    def remove_product(self, product: str) -> str:
        """
        Removes product from the inventory.

        Parameters:
            product (str): product to be removed from inventory

        >>> inventory = Inventory()
        >>> inventory.set_inventory({"Laptop": 20, "Smartphone": 15, "Tablet": 30, "Headphones": 10})
        "Updated inventory: {'laptop': 20, 'smartphone': 15, 'tablet': 30, 'headphones': 10}"
        >>> inventory.remove_product('tablet')
        "Updated inventory: {'laptop': 20, 'smartphone': 15, 'headphones': 10}"
        >>> inventory.remove_product('brickphone')
        "Updated inventory: {'laptop': 20, 'smartphone': 15, 'headphones': 10}"
        >>> inventory.remove_product(2)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to product parameter must be a string object
        """

        assert isinstance(product, str), "argument passed to product parameter must be a string object"

        # using lowercase, since all keys in dictionary are stored as such
        if product.lower() in self._inventory.keys():
            # pop method removes an item from a dictionary
            self._inventory.pop(product)

        return f"Updated inventory: {self._inventory}"

    def update_quantity(self, product: str) -> str:
        """
        Updates the quantity of a product in the inventory according to user input.

        Parameters:
            product (str): inventory product whose quantity is updated

        # unsure how to write doctests, since function asks for user input
        """

        # validating arguments
        assert product in self._inventory.keys(), "product does not exist in the inventory"

        # show user current quantity, to inform decision about updating product quantity
        print(f"Current {product} quantity: {self._inventory[product]}")

        # looping until receiving valid input from user
        decision = 0
        while decision not in {1, 2, 3}:
            decision = int(input(f"Choose an option:\n1 - Increase quantity\n2 - Decrease quantity\n3 - Set new quantity\n"))

        # conditional branches update product quantity according to user decision
        if decision == 1:
            # do not convert to integer, so as to write assertions check to validate input and give better error messaging
            increase = input(f"Increase inventory for {product} by: ")
            assert increase.isdigit(), "increase quantity must be an integer value"
            # type conversion only after assertion check, to prevent errors
            increase = int(increase)
            self._inventory[product] += increase
        elif decision == 2:
            decrease = input(f"Decrease inventory for {product} by: ")
            assert decrease.isdigit(), "decrease quantity must be an integer value"
            decrease = int(decrease)
            assert decrease <= self._inventory[product], "quantity cannot be decreased to a negative value"
            self._inventory[product] -= decrease
        elif decision == 3:
            new_quantity = input(f"Set new inventory for {product} to: ")
            # added replacement of minus sign in order to give correct error message
            assert new_quantity.replace('-', '').isdigit(), "new quantity must be an integer value"
            new_quantity = int(new_quantity)
            assert new_quantity >= 0, "new quantity must be a non-negative integer"
            self._inventory[product] = new_quantity

        return f"Updated inventory: {self._inventory}"

# testing outside of class doctests, for one method, since it takes user input
inventory = Inventory()
'''
print(inventory.set_inventory({"Laptop": 20, "Smartphone": 15, "Tablet": 30, "Headphones": 10}))
print(inventory.update_quantity('laptop'))
print(inventory.update_quantity('laptop'))
print(inventory.update_quantity('laptop'))
'''

doctest.testmod()