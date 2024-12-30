import doctest

def remove_item(product_tuple: tuple, product_index: int) -> tuple:
    """
    Given a tuple of products and the index of a product in the tuple, returns the tuple
    without the indexed product.

    Parameters:
         product_tuple (Tuple[str]): tuple of product names
         product_index (int): index of the product in the tuple

    Returns:
        (Tuple[str]): tuple of product names with indexed product removed

    >>> remove_item(("cellphone", "laptop", "microphone"), 2)
    ('cellphone', 'laptop')
    >>> remove_item(("laptop",), 0)
    ()
    >>> remove_item(("cellphone", "laptop"), 2)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to product_index parameter must be a non-negative integer within range of tuple indices
    >>> remove_item(("cellphone", "laptop"), -2)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to product_index parameter must be a non-negative integer within range of tuple indices
    >>> remove_item((), 0)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to product_tuple parameter must be a non-empty tuple

    """
    # checking that argument passed to product_tuple parameter is a non-empty tuple
    assert type(product_tuple) == tuple and product_tuple != (),\
        "argument passed to product_tuple parameter must be a non-empty tuple"

    #checking that argument passed to product_index parameter is a non-negative integer and within range of tuple indices
    assert type(product_index) == int and 0 <= product_index < len(product_tuple),\
        "argument passed to product_index parameter must be a non-negative integer within range of tuple indices"

    # no remove method for tuple object, so convert into a list and remove value
    product_list = list(product_tuple)
    product_list.remove(product_list[product_index])

    # return list converted back into tuple
    return tuple(product_list)

doctest.testmod()