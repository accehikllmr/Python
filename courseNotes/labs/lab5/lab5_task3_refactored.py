import doctest
from typing import List

class Store:
    """ A class representing stores """

    def __init__(self, sales: float, ratio: float) -> None:
        """
        Method to instantiate a store object.

        Parameters:
            sales (float): total monthly sales for the store
            ratio (float): ratio of revenue to sales for the store

        >>> store_1 = Store(10000.00, 1/5)
        >>> store_1.get_monthly_sales()
        10000.0
        """

        # checking preconditions
        assert isinstance(sales, float) and sales >= 0, "argument passed to sales parameter must be a non-negative float"
        assert isinstance(ratio, float) and 1 > ratio >= 0, "argument passed to ratio parameter must be a positive float less than 1"

        # store attributes
        self._monthly_sales = sales
        self._revenue_to_sales = ratio

    def __str__(self) -> str:
        """
        Outputs string representation of store object.

        Returns:
            (str): string representation of store object

        >>> store_1 = Store(10000.00, 1/5)
        >>> store_1.__str__()
        'Store(10000.0, 0.2)'
        >>> print(store_1)
        Store(10000.0, 0.2)
        """

        return f"Store({self._monthly_sales}, {self._revenue_to_sales})"

    def get_monthly_sales(self) -> float:
        """
        Retrieve monthly_sales attribute from store object.

        Returns:
            (float): monthly sales of store object

        >>> store_1 = Store(10000.00, 1/5)
        >>> store_1.get_monthly_sales()
        10000.0
        """

        return self._monthly_sales

    def set_monthly_sales(self, new_sales: float):
        """
        Updates monthly_sales attribute for store object.

        Parameters:
             new_sales (float): value assigned to monthly_sales attribute of store object

        >>> store_1 = Store(10000.00, 1/5)
        >>> store_1.set_monthly_sales(15000.0)
        >>> store_1.get_monthly_sales()
        15000.0
        """

        self._monthly_sales = new_sales

    def get_revenue_to_sales(self) -> float:
        """
        Retrieves revenue_to_sales attribute from store object.

        Returns:
            (float): ratio of revenue to sales for store object

        >>> store_1 = Store(10000.00, 1/5)
        >>> store_1.get_revenue_to_sales()
        0.2
        """

        return self._revenue_to_sales

    def set_revenue_to_sales(self, new_ratio: float) -> float:
        """
        Updates revenue_to_sales attribute of store object.

        Returns:
            (float): value assigned to revenue_to_sales attribute of store object

        >>> store_1 = Store(10000.00, 1/5)
        >>> store_1.set_revenue_to_sales(1/2)
        >>> store_1.get_revenue_to_sales()
        0.5
        """

        self._revenue_to_sales = new_ratio

    def calculate_store_revenue(self) -> float:
        """
        Calculates the revenue for a store object.

        Returns:
            (float): revenue for a store object

        >>> store_1 = Store(10000.00, 1/5)
        >>> store_1.calculate_store_revenue()
        2000.0
        """

        return self._monthly_sales * self._revenue_to_sales

    # do not need get function for store revenue, since already returned during calculation

# creating function which can take list of store objects and calculate total revenue (not only for two stores)
def calculate_total_revenue(stores: List[Store]) -> float:
    """
    Calculates total revenue of all store objects.

    Parameters:
        stores (List[Store]): list of all store objects

    Returns:
        (float): total revenue of all store objects

    # instead of instantiating objects and then adding to the list, instantiating them directly inside the list
    >>> all_stores = [Store(10000.00, 1/5), Store(20000.00, 1/2), Store(15000.00, 1/3)]
    >>> calculate_total_revenue(all_stores)
    17000.0
    >>> calculate_total_revenue([])
    0.0
    >>> calculate_total_revenue('this is totally a list of objects...')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to stores parameter must be a list object
    >>> calculate_total_revenue([1, 2, 3])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to stores parameter must contain only Store objects as elements
    """

    # checking preconditions
    assert isinstance(stores, list), "argument passed to stores parameter must be a list object"

    for i in stores:
        # not sure why no conditional statement is needed to prevent empty list from flagging this assertion
        assert isinstance(i, Store), "argument passed to stores parameter must contain only Store objects as elements"

    # instantiating total revenue object, to accumulate total revenue, as float for empty list of stores
    total_revenue = 0.0

    # iterating through all store objects in order to retrieve their revenues and add them total
    for store in stores:
        total_revenue += store.calculate_store_revenue()

    return total_revenue

doctest.testmod()