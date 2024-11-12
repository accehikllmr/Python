import doctest
from typing import List

def remove_item(product_list: List[str], product_index: int) -> List[str]:
    """
    Given a list of products and the index of a product in the list, returns the list
    without the indexed product.

    Parameters:
        product_list (List[str]): list of product names
        product_index (int): index of a product in the product list

    Returns:
        (List[str]): list of product names with indexed product removed

    >>> remove_item(["cellphone", "laptop", "microphone"], 1)
    ['cellphone', 'microphone']
    >>> remove_item(["laptop"], 0)
    []
    >>> remove_item(["cellphone", "laptop", "microphone"], 3)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to product_index parameter must be a non-negative integer within the range of the product_list indices
    >>> remove_item(["cellphone", "laptop", "microphone"], -2)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to product_index parameter must be a non-negative integer within the range of the product_list indices
    >>> remove_item([], 0)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to product_list parameter must be a non-empty list
    """
    # checking that argument passed to product_list parameter is a non-empty list object
    assert type(product_list) == list and product_list != [], "argument passed to product_list parameter must be a non-empty list"

    # checking that argument passed to product_index parameter is a non-negative integer within the range of the product_list indices
    assert type(product_index) == int and 0 <= product_index < len(product_list),\
        "argument passed to product_index parameter must be a non-negative integer within the range of the product_list indices"

    # indexing product_list using product_index, which gives the value to remove, and then using the remove method on the product_list
    product_list.remove(product_list[product_index])

    # returning result
    return product_list

doctest.testmod()