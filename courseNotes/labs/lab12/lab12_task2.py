import doctest


class Product:
    """ A class representing one product """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Constructor

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop._name
        'laptop'
        >>> laptop._price
        2030.5
        >>> laptop._quantity
        2
        """

        assert isinstance(name, str), "the name must be a string"
        assert isinstance(price, float) and price > 0, "the price must be a positive float"
        assert isinstance(quantity, int) and quantity > 0, "the quantity must be a positive int"

        self._name = name
        self._price = price
        self._quantity = quantity

    def get_name(self) -> str:
        """
        get the name of the product

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.get_name()
        'laptop'
        """

        return self._name

    def get_price(self) -> float:
        """
        get the price of the product

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.get_price()
        2030.5
        """

        return self._price

    def get_quantity(self) -> int:
        """
        get the quantity of the product

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.get_quantity()
        2
        """

        return self._quantity

    def add_quantity(self, quantity: int = 1) -> None:
        """
        Add the quantity of the product

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.add_quantity(1)
        >>> laptop._quantity
        3
        """

        assert isinstance(quantity, int) and quantity > 0, "the quantity must be a positive int"

        self._quantity += quantity

    def reduce_quantity(self, quantity: int = 1) -> None:
        """
        Reduce the quantity of the product

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> laptop.reduce_quantity(1)
        >>> laptop._quantity
        1
        >>> laptop.add_quantity(1)
        >>> laptop.reduce_quantity(3)
        >>> laptop._quantity
        0
        """

        assert isinstance(quantity, int) and quantity > 0, "the quantity must be a positive int"

        # conditional to avoid quantity reducing to a negative value
        if quantity > self._quantity:
            self._quantity = 0
        else:
            self._quantity -= quantity


class Inventory:
    """ A class representing the inventory """

    def __init__(self) -> None:
        """
        Constructor

        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory._products
        []
        """

        self._products = []

    def _find_product(self, name: str) -> Product:
        """

        Find the product with the given game. Return None if the product is not found

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop)
        >>> retail_store_inventory._find_product("laptop") is laptop
        True
        >>> retail_store_inventory._products = [laptop]
        >>> retail_store_inventory._find_product("laptop") is laptop
        True
        >>> retail_store_inventory._find_product("tablet") == None
        True
        """

        # iterate through all products in list of products in Inventory objects
        for product in self._products:
            # calling getter function on Product object to compare with argument passed to method
            if product.get_name() == name:
                # compared with 'is' method to object
                return product

    def stock_product(self, product: Product) -> None:
        """
        Add a product to the inventory

        >>> laptop_1 = Product("laptop", 2030.5, 2)
        >>> laptop_2 = Product("laptop", 2030.5, 3)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop_1)
        >>> retail_store_inventory.stock_product(laptop_2)
        >>> retail_store_inventory._products[0] is laptop_1
        True
        >>> retail_store_inventory._find_product("laptop").get_quantity()
        5
        >>> laptop_1 = Product("laptop", 2030.5, 2)
        >>> laptop_2 = Product("laptop", 102.09, 3)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop_1)
        >>> retail_store_inventory.stock_product(laptop_2)
        Traceback (most recent call last):
        ...
        AssertionError: cannot have duplicate products in inventory
        """
        # to prevent adding product that is already included in the inventory stock
        # for i in self._products:

        # can use isinstance to check for user created classes too
        assert isinstance(product, Product), "the parameter product must be an instance of the Class Product"

        if len(self._products) == 0:
            self._products.append(product)
        else:
            # adding Product object to list of products in Inventory object, but only if new kind of product
            for i in self._products:
                if product.get_name() != i.get_name():
                    self._products.append(product)
                # otherwise, if same price and thus same product, add to inventory of existing product
                elif product.get_name() == i.get_name() and product.get_price() == i.get_price():
                    i.add_quantity(product.get_quantity())
                # when products have same name, but different prices
                else:
                    assert i.get_name() != product.get_name(), "cannot have duplicate products in inventory"

    def sell_product(self, product_name: str, quantity: int):
        """
        Sell product in inventory

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop)
        >>> retail_store_inventory.sell_product("laptop", 1)
        >>> laptop._quantity
        1
        """

        assert isinstance(product_name, str), "the name must be a string"
        assert isinstance(quantity, int) and quantity > 0, "the quantity must be a positive int"

        product = self._find_product(product_name)

        if product:
            product.reduce_quantity(quantity)

    def calculate_inventory_value(self) -> float:
        """
        Calcuatel the total value of the current inventory

        >>> laptop = Product("laptop", 2030.5, 2)
        >>> retail_store_inventory = Inventory()
        >>> retail_store_inventory.stock_product(laptop)
        >>> retail_store_inventory.calculate_inventory_value()
        4061.0
        """

        total_value = 0

        for product in self._products:
            total_value += product.get_price() * product.get_quantity()

        return total_value


if __name__ == '__main__':
    doctest.testmod()