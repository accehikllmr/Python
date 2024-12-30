import doctest

def get_store1_revenue(store1_monthly_sales: float) -> float:
    """
    This function calculates the revenue for store 1, using the revenue to sales ratio of 1:8

    Preconditions:  store1_monthly_sales    float >= 0

    >>> get_store1_revenue(0.0)
    0.0
    >>> get_store1_revenue(200.0)
    40.0
    >>> get_store1_revenue(-200.0)
    Traceback (most recent call last):
    ...
    AssertionError: the sales for store 1 must be greater than or equal to 0
    >>> get_store1_revenue(200)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for store1_monthly_sales parameter
    """

    #checking that input data is of float type and positive
    assert type(store1_monthly_sales) == float, "invalid data type for store1_monthly_sales parameter"
    assert store1_monthly_sales >= 0, "the sales for store 1 must be greater than or equal to 0"

    #ration given in problem description
    revenue_to_sales_ratio = 1/5

    #revenue for the store is the sales multiplied by the given factor
    store1_revenue = store1_monthly_sales * revenue_to_sales_ratio

    return store1_revenue

def get_store2_revenue(store2_monthly_sales: float) -> float:
    """
    This function calculates the revenue for store 2, using the revenue to sales ratio of 1:8

    Preconditions:  store2_monthly_sales    float >= 0

    >>> get_store2_revenue(0.0)
    0.0
    >>> get_store2_revenue(200.0)
    25.0
    >>> get_store2_revenue(-200.0)
    Traceback (most recent call last):
    ...
    AssertionError: the sales for store 2 must be greater than or equal to 0
    >>> get_store2_revenue(200)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for store2_monthly_sales parameter
    """

    #checking that input data is of float type and positive
    assert type(store2_monthly_sales) == float, "invalid data type for store2_monthly_sales parameter"
    assert store2_monthly_sales >= 0, "the sales for store 2 must be greater than or equal to 0"

    #ration given in problem description
    revenue_to_sales_ratio = 1/8

    #revenue for the store is the sales multiplied by the given factor
    store2_revenue = store2_monthly_sales * revenue_to_sales_ratio

    return store2_revenue

def get_total_revenue(store1_monthly_sales: float, store2_monthly_sales: float) -> float:
    """
    This function takes the monthly sales for each store and calculates the total revenue for
    all stores combined.

    Preconditions:  store1_monthly_sales    float >= 0
                    store2_monthly_sales    float >= 0

    >>> get_total_revenue(0.0, 0.0)
    0.0
    >>> get_total_revenue(800.0, 600.0)
    235.0
    >>> get_total_revenue(0.0, 37.4)
    4.675
    >>> get_total_revenue(-400.0, 600.0)
    Traceback (most recent call last):
    ...
    AssertionError: the sales for store 1 must be greater than or equal to 0
    >>> get_total_revenue(400.0, -600.0)
    Traceback (most recent call last):
    ...
    AssertionError: the sales for store 2 must be greater than or equal to 0
    >>> get_total_revenue(400, 600.0)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for store1_monthly_sales parameter
    >>> get_total_revenue(400.0, 600)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for store2_monthly_sales parameter
    """

    #checking that input values are of float type
    assert type(store1_monthly_sales) == float, "invalid data type for store1_monthly_sales parameter"
    assert type(store2_monthly_sales) == float, "invalid data type for store2_monthly_sales parameter"

    #checking that the input values are positive
    assert store1_monthly_sales >= 0, "the sales for store 1 must be greater than or equal to 0"
    assert store2_monthly_sales >= 0, "the sales for store 2 must be greater than or equal to 0"

    #total revenue is sum of revenues from all stores
    total_revenue = get_store1_revenue(store1_monthly_sales) + get_store2_revenue(store2_monthly_sales)

    return total_revenue

if __name__ == "__main__":
    doctest.testmod()
