import doctest
import copy
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
            (Dict[str, Dict[str, int]]): dictionary object containing all inventory

        >>> inventory = Inventory()
        >>> inventory.get_inventory()
        {}
        """

        return self._inventory

    def set_inventory(self, new_inventory: Dict[str, Dict[str, int]]) -> str:
        """
        Updates all dictionary object items in the inventory.

        Parameters:
            (Dict[str, Dict[str, int]]): dictionary object containing new inventory items

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

    # not adding parameter for identification number, since this should be added automatically (next number in sequence)
    def add_product(self, product: str) -> str:
        """
        Adds a product to the inventory.

        Parameters:
            product (str): product to be added to the store inventory

        Returns:
            (str): string representation of updated inventory

        >>> inventory = Inventory()
        >>> inventory.set_inventory({'000': {"Laptop": 20}, '001': {"Smartphone": 15}, '002': {"Tablet": 30}, '003': {"Headphones": 10}})
        "Updated inventory: {'000': {'laptop': 20}, '001': {'smartphone': 15}, '002': {'tablet': 30}, '003': {'headphones': 10}}"
        >>> inventory.add_product("Brickphone")
        "Updated inventory: {'000': {'laptop': 20}, '001': {'smartphone': 15}, '002': {'tablet': 30}, '003': {'headphones': 10}, '004': {'brickphone': 0}}"
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
        assert isinstance(product, str) and product.isalpha() and len(product) != 0, "argument passed to product parameter must have only alphabetic characters"

        # going into dictionary values to find if product already exists (no need to check id, since automatically generated)
        for value in self._inventory.values():
            # rather than comparing with outer keys, compare with each individual value associated to each key
            assert product.lower() not in value, "product already exists in the inventory"

        # extract id string at end of inventory, need to use deepcopy, otherwise popitem method changed original dictionary
        inventory_copy = copy.deepcopy(self._inventory)
        # extracted string of largest id, convert to int in order to increase by 1, not considering reassigning ids from removed products
        new_id_int = int(inventory_copy.popitem()[0]) + 1
        # convert back to string, according to length (three digit maximum, per this program)
        if new_id_int < 10:
            new_id_str = f"00{new_id_int}"
        elif new_id_int < 100:
            new_id_str = f"0{new_id_int}"
        else:
            new_id_str = f"{new_id_int}"

        # adding pairing of id and dictionary to inventory, lowercase for product string to harmonize
        self._inventory[new_id_str] = {product.lower(): 0}

        return f"Updated inventory: {self._inventory}"

    def remove_id(self, product_id: str)-> str:
        """
        Removes id from the inventory, and the associated product.

        Parameters:
            product_id (str): id of product to be removed

        Returns:
            (str): string representation of updated inventory

        >>> inventory = Inventory()
        >>> inventory.set_inventory({'000': {"Laptop": 20}, '001': {"Smartphone": 15}, '002': {"Tablet": 30}, '003': {"Headphones": 10}})
        "Updated inventory: {'000': {'laptop': 20}, '001': {'smartphone': 15}, '002': {'tablet': 30}, '003': {'headphones': 10}}"
        >>> inventory.remove_id('002')
        "Updated inventory: {'000': {'laptop': 20}, '001': {'smartphone': 15}, '003': {'headphones': 10}}"
        >>> inventory.remove_id('005')
        Traceback (most recent call last):
        ...
        AssertionError: product id not in inventory
        >>> inventory.remove_id('01')
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to product id must be a string object of length 3 containing only digits
        >>> inventory.remove_id(000)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to product id must be a string object of length 3 containing only digits
        >>> inventory.remove_id('abc')
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to product id must be a string object of length 3 containing only digits
        """

        # validating argument
        assert isinstance(product_id, str) and len(product_id) == 3 and product_id.isdigit(), "argument passed to product id must be a string object of length 3 containing only digits"

        # checking for product id, otherwise pop method encounters a key error
        assert product_id in self._inventory.keys(), "product id not in inventory"

        self._inventory.pop(product_id)

        return f"Updated inventory: {self._inventory}"

    def remove_product(self, product: str) -> str:
        """
        Removes product from the inventory.

        Parameters:
            product (str): product to be removed from inventory

        Returns:
            (str): string representation of updated inventory

        >>> inventory = Inventory()
        >>> inventory.set_inventory({'000': {"Laptop": 20}, '001': {"Smartphone": 15}, '002': {"Tablet": 30}, '003': {"Headphones": 10}})
        "Updated inventory: {'000': {'laptop': 20}, '001': {'smartphone': 15}, '002': {'tablet': 30}, '003': {'headphones': 10}}"
        >>> inventory.remove_product('brickphone')
        "Updated inventory: {'000': {'laptop': 20}, '001': {'smartphone': 15}, '002': {'tablet': 30}, '003': {'headphones': 10}}"
        >>> inventory.remove_product('tablet')
        "Updated inventory: {'000': {'laptop': 20}, '001': {'smartphone': 15}, '003': {'headphones': 10}}"
        >>> inventory.remove_product(2)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to product parameter must be a string object
        """

        assert isinstance(product, str), "argument passed to product parameter must be a string object"

        # using lowercase, since all keys in dictionary are stored as such
        for item in self._inventory.items():
            if product.lower() in item[1]:
                # pop method removes an item from a dictionary
                self._inventory.pop(item[0])\
                # need break, otherwise iterations continue over dictionary size which has been modified
                break

        return f"Updated inventory: {self._inventory}"

    def update_quantity(self, product: str) -> str:
        """
        Updates the quantity of a product in the inventory according to user input.

        Parameters:
            product (str): inventory product whose quantity is updated

        # unsure how to write doctests, since function asks for user input
        """

        # validating arguments
        for item in self._inventory.items():

            # looking at index 1, since 0 is the key id
            if product.lower() in item[1]:

                '''
                show user current quantity, to inform decision about updating product quantity
                to pull quantity from product, item at index 1 (inner dictionary) is keyed using product name
                '''
                print(f"Current {product.lower()} quantity: {item[1][product.lower()]}")

                # looping until receiving valid input from user
                decision = 0
                while decision not in {1, 2, 3}:
                    decision = int(input(f"Choose an option:\n1 - Increase quantity\n2 - Decrease quantity\n3 - Set new quantity\n"))

                # conditional branches update product quantity according to user decision
                if decision == 1:
                    # do not convert to integer, in order to write assertions check to validate input and give better error messaging
                    increase = input(f"Increase inventory for {product} by: ")
                    assert increase.isdigit(), "increase quantity must be an integer value"
                    # type conversion only after assertion check, to prevent errors
                    increase = int(increase)
                    # using same keying as above, in print statement, but also importantly, don't need to cite inventory (already in it)
                    item[1][product.lower()] += increase
                elif decision == 2:
                    decrease = input(f"Decrease inventory for {product} by: ")
                    assert decrease.isdigit(), "decrease quantity must be an integer value"
                    decrease = int(decrease)
                    # update to key inner dictionary, not outer
                    assert decrease <= item[1][product], "quantity cannot be decreased to a negative value"
                    item[1][product.lower()] -= decrease
                elif decision == 3:
                    new_quantity = input(f"Set new inventory for {product} to: ")
                    # added replacement of minus sign in order to give correct error message
                    assert new_quantity.replace('-', '').isdigit(), "new quantity must be an integer value"
                    new_quantity = int(new_quantity)
                    assert new_quantity >= 0, "new quantity must be a non-negative integer"
                    item[1][product.lower()] = new_quantity

            else:
                # assertion is negation of previous conditional, so obviously false, but only way to trigger error
                assert product.lower() in item[1], "product does not exist in the inventory"

        return f"Updated inventory: {self._inventory}"

# testing outside of class doctests, for one method, since it takes user input
inventory = Inventory()

'''
print(inventory.set_inventory({'000': {"Laptop": 20}, '001': {"Smartphone": 15}, '002': {"Tablet": 30}, '003': {"Headphones": 10}}))
print(inventory.update_quantity('laptop'))
print(inventory.update_quantity('laptop'))
print(inventory.update_quantity('laptop'))
'''

doctest.testmod()