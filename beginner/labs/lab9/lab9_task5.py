import doctest
from typing import List

def remove_item(product_list: List[str], product: str) -> List[str]:
    """
    Given a list of product and a product name, remove the named product from the list of products.

    Parameters:
        product_list (List[str]): list of products names
        product (str): name of product to be removed from list

    Returns:
        (List[str]): list of products without the named product

    >>> remove_item(["cellphone", "laptop", "microphone"], "laptop")
    ['cellphone', 'microphone']
    >>> remove_item(["cellphone", "laptop", "microphone", "laptop"], "laptop")
    ['cellphone', 'microphone', 'laptop']
    >>> remove_item(["cellphone", "laptop"], "")
    ['cellphone', 'laptop']
    >>> remove_item([], "laptop")
    []
    >>> remove_item(["laptop"], "laptop")
    []
    """
    '''
    checking if argument passed to product_list is a list of strings,
    not specifying List[str] since cannot get it to work properly
    '''
    assert type(product_list) == list or product_list == [], "argument passed to product_list parameter must be a list object"

    # checking if argument passed to product parameter is a string
    assert type(product) == str, "argument passed to product parameter must be a string object"

    # using remove method on list only if product is found in list
    if product in product_list:
        product_list.remove(product)

    # returning original or modified list, depending on above conditional
    return product_list

doctest.testmod()