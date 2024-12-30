import doctest
from typing import List

class Product:
    """ A class representing one product """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Constructor method, instantiates a Product object.

        Parameters:
            name (str): name of the product
            price (float): unit price of the product
            quantity (int): quantity of the product, or units in stock

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop._name
        'laptop'
        >>> laptop._price
        2030.5
        >>> laptop._quantity
        2
        >>> laptop = Product(3000, 2030.5, 2)
        Traceback (most recent call last):
        ...
        AssertionError: the name must be a string
        >>> laptop = Product("laptop", 2031, 2)
        Traceback (most recent call last):
        ...
        AssertionError: the price must be a positive float
        >>> laptop = Product("laptop", 2030.5, 2.0)
        Traceback (most recent call last):
        ...
        AssertionError: the quantity must be a positive int
        >>> laptop = Product("laptop", -2030.5, 2)
        Traceback (most recent call last):
        ...
        AssertionError: the price must be a positive float
        >>> laptop = Product("laptop", 2030.5, -2)
        Traceback (most recent call last):
        ...
        AssertionError: the quantity must be a positive int
        """

        # added docstring tests for following assertions
        assert isinstance(name, str), "the name must be a string"
        assert isinstance(price, float) and price > 0, "the price must be a positive float"
        assert isinstance(quantity, int) and quantity > 0, "the quantity must be a positive int"

        self._name = name
        self._price = price
        self._quantity = quantity

    def __str__(self) -> str:
        """
        Outputs the string representation of a Product object.

        Returns:
            (str): string representation of a Product object

        >>> laptop = Product("laptop", 2030.5, 3)
        >>> laptop.__str__()
        'Product(laptop, 2030.5, 3)'
        >>> print(laptop)
        Product(laptop, 2030.5, 3)
        """

        return f"Product({self._name}, {self._price}, {self._quantity})"

    def get_name(self) -> str:
        """
        Retrieve the name attribute of a Product object.

        Returns:
            (str): name of the product

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.get_name()
        'laptop'
        """

        return self._name

    def set_name(self, name: str) -> None:
        """
        Modifies the name attribute of a Product object.

        Parameters:
            name (str): new name for an existing Product object

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.set_name("potpal")
        >>> laptop.get_name()
        'potpal'
        >>> laptop.set_name(2030.5)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to name parameter must be a string object
        """

        # need this validation, otherwise constructor method validations are circumvented
        assert isinstance(name, str), "argument passed to name parameter must be a string object"

        self._name = name

    def get_price(self) -> float:
        """
        Retrieves the price attribute of a Product object.

        Returns:
            (float): price of a Product object

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.get_price()
        2030.5
        """

        return self._price

    def set_price(self, price: float) -> None:
        """
        Modifies the price attribute of a Product object.

        Parameters:
            price (float): new price for an existing Product object

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.set_price(2100.0)
        >>> laptop.get_price()
        2100.0
        >>> laptop.set_price(2030)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to price parameter must be a positive float object
        >>> laptop.set_price(-2030.5)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to price parameter must be a positive float object
        """

        assert isinstance(price, float) and price > 0, "argument passed to price parameter must be a positive float object"

        self._price = price

    def get_quantity(self) -> int:
        """
        Retrieve the quantity attribute of a Product object.

        Returns:
            (int): quantity of a Product object

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.get_quantity()
        2
        """

        return self._quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Modifies the quantity attribute of a Product object.

        Parameters:
             quantity (int): new quantity for an existing Product object

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.set_quantity(3)
        >>> laptop.get_quantity()
        3
        >>> laptop.set_quantity("two")
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to quantity parameter must be a positive integer object
        >>> laptop.set_quantity(-2)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to quantity parameter must be a positive integer object
        """

        assert isinstance(quantity, int) and quantity > 0, "argument passed to quantity parameter must be a positive integer object"

        self._quantity = quantity

    def add_quantity(self, increase: int = 1) -> None:
        """
        Adds to the quantity attribute of a Product object.

        Parameters:
            increase (int): amount by which to increase the quantity of an existing Product object

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.add_quantity()
        >>> laptop.get_quantity()
        3
        >>> laptop.add_quantity(2)
        >>> laptop.get_quantity()
        5
        >>> laptop.add_quantity("two")
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to increase parameter must be a positive integer object
        >>> laptop.add_quantity(-2)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to increase parameter must be a positive integer object
        """

        assert isinstance(increase, int) and increase > 0, "argument passed to increase parameter must be a positive integer object"

        self._quantity += increase

    def reduce_quantity(self, decrease: int = 1) -> None:
        """
        Reduces the quantity attribute of a Product object.

        Parameters:
            decrease (int): amount by which to decrease the quantity of an existing Product object

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.reduce_quantity()
        >>> laptop.get_quantity()
        1
        >>> laptop.add_quantity(5)
        >>> laptop.reduce_quantity(6)
        >>> laptop.get_quantity()
        0
        >>> laptop.reduce_quantity()
        >>> laptop.get_quantity()
        0
        >>> laptop.reduce_quantity("two")
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to decrease parameter must be a positive integer object
        >>> laptop.reduce_quantity(-1)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to decrease parameter must be a positive integer object
        """

        assert isinstance(decrease, int) and decrease > 0, "argument passed to decrease parameter must be a positive integer object"

        # conditional to avoid quantity reducing to a negative value
        if decrease > self._quantity:
            self._quantity = 0
        else:
            self._quantity -= decrease

class Inventory:
    """ A class representing an inventory """

    def __init__(self) -> None:
        """
        Constructor method, instantiates an Inventory object.

        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory._products
        []
        """

        self._products = []

    def get_products(self) -> List[Product]:
        """
        Retrieves the products attribute from an Inventory object.

        Returns:
            (List[Product]): list of Product objects

        >>> retail_store_inventory = Inventory()
        >>> laptop_1 = Product("dell", 500.0, 10)
        >>> laptop_2 = Product("apple", 1500.0, 3)
        >>> laptop_3 = Product("lenovo", 650.0, 15)
        >>> retail_store_inventory.stock_product(laptop_1)
        >>> retail_store_inventory.stock_product(laptop_2)
        >>> retail_store_inventory.stock_product(laptop_3)
        >>> products = retail_store_inventory.get_products()
        >>> print(products[0])
        Product(dell, 500.0, 10)
        >>> print(products[1])
        Product(apple, 1500.0, 3)
        >>> print(products[2])
        Product(lenovo, 650.0, 15)
        """

        return self._products

    def set_products(self, products: List[Product]) -> None:
        """
        Modifies the products attribute of an Inventory object.

        Parameters:
            products (List[Product]): list of Product objects

        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.set_products([Product("dell", 500.0, 10), Product("apple", 1500.0, 3), Product("lenovo", 650.0, 15)])
        >>> inventory = retail_store_inventory.get_products()
        >>> print(inventory[0])
        Product(dell, 500.0, 10)
        >>> print(inventory[1])
        Product(apple, 1500.0, 3)
        >>> print(inventory[2])
        Product(lenovo, 650.0, 15)
        >>> retail_store_inventory.set_products((Product("dell", 500.0, 10), Product("apple", 1500.0, 3), Product("lenovo", 650.0, 15)))
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to products parameter must be a list object
        >>> retail_store_inventory.set_products([Product("dell", 500.0, 10), Product("apple", 1500.0, 3), 'Product("lenovo", 650.0, 15)'])
        Traceback (most recent call last):
        ...
        AssertionError: all elements in list object must be Product objects
        """

        # validating arguments
        assert isinstance(products, list), "argument passed to products parameter must be a list object"

        for element in products:
            assert isinstance(element, Product), "all elements in list object must be Product objects"

        self._products = products

    def find_product(self, name: str) -> Product:
        """
        Find the Product object within an Inventory object by its name.

        Parameters:
            name (str): name of Product object to find in Inventory object

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop)
        >>> retail_store_inventory.find_product("laptop") is laptop
        True
        >>> retail_store_inventory.set_products([laptop])
        >>> retail_store_inventory.find_product("laptop") is laptop
        True
        >>> retail_store_inventory.find_product("tablet") is None
        True
        >>> retail_store_inventory.find_product(3)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to name parameter must be a string object
        """

        # validating arguments
        assert isinstance(name, str), "argument passed to name parameter must be a string object"

        # iterate through all products in list of products in Inventory objects
        for product in self._products:
            # calling getter function on Product object to compare with argument passed to method
            if product.get_name() == name:
                # compared with 'is' method to object
                return product

    def stock_product(self, product: Product) -> None:
        """
        Add a Product object to an Inventory object.

        Parameters:
            product (Product): Product object to be added to Inventory object

        >>> laptop_1 = Product("laptop", 2030.5, 2)
        >>> laptop_2 = Product("laptop", 2030.5, 3)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop_1)
        >>> retail_store_inventory.stock_product(laptop_2)
        >>> retail_store_inventory.get_products()[0] is laptop_1
        True
        >>> retail_store_inventory.find_product("laptop").get_quantity()
        5
        >>> laptop_1 = Product("laptop", 2030.5, 2)
        >>> laptop_2 = Product("laptop", 102.09, 3)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop_1)
        >>> retail_store_inventory.stock_product(laptop_2)
        Traceback (most recent call last):
        ...
        AssertionError: cannot have duplicate products in inventory
        >>> retail_store_inventory.stock_product('laptop_2')
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to product parameter must be a Product object
        """

        # can use isinstance to check for user created classes too
        assert isinstance(product, Product), "argument passed to product parameter must be a Product object"

        if len(self._products) == 0:
            self._products.append(product)
        else:
            # adding Product object to list of products in Inventory object, but only if new kind of product
            for i in self._products:
                if product.get_name() != i.get_name():
                    self._products.append(product)
                    # without a break, it will add the same product multiple times, erroneously increasing its quantity attribute
                    break
                # otherwise, if same price and thus same product, add to inventory of existing product
                elif product.get_name() == i.get_name() and product.get_price() == i.get_price():
                    i.add_quantity(product.get_quantity())
                # when products have same name, but different prices (duplicates whose quantity cannot be combined)
                else:
                    assert i.get_name() != product.get_name(), "cannot have duplicate products in inventory"

    def sell_product(self, product_name: str, units_sold: int) -> None:
        """
        Sells a Product object from the Inventory object.

        Parameters:
            product_name (str): name attribute of Product object to be sold
            units_sold (int): quantity of Product object to be sold

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop)
        >>> retail_store_inventory.sell_product("laptop", 1)
        >>> laptop.get_quantity()
        1
        >>> retail_store_inventory.sell_product("laptop", -1)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to units_sold parameter must be an integer object
        >>> retail_store_inventory.sell_product(3, 1)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to product_name parameter must be a string object
        """

        assert isinstance(product_name, str), "argument passed to product_name parameter must be a string object"
        assert isinstance(units_sold, int) and units_sold > 0, "argument passed to units_sold parameter must be an integer object"

        # no need for assertion statement, since this method return boolean for existence of product in inventory
        product = self.find_product(product_name)

        # condition that product has been found in inventory
        if product:
            product.reduce_quantity(units_sold)

    def calculate_inventory_value(self) -> float:
        """
        Calculates the total monetary value of the current inventory.

        Returns:
            (float): total monetary value of the current inventory

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop)
        >>> retail_store_inventory.calculate_inventory_value()
        4061.0
        """

        total_value = 0

        for product in self._products:
            # calling Product object methods to get their attributes
            total_value += product.get_price() * product.get_quantity()

        return total_value

if __name__ == '__main__':
    doctest.testmod()