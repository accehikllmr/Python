# PyCharm flagged numerous errors for this script, despite there being none (reset and they disappeared!)

import doctest
from typing import List, Dict

APPLE = "apple"
BANANA = "banana"
GRAPE = "grape"
ORANGE = "orange"

def list_to_dict(input_list: List[int]) -> Dict[str, int]:
    """
    Converts a list into a dictionary where the keys are the indices of the elements in the list.
    
    Parameters:
        input_list (list): The input list to be converted.
        
    Returns:
        dict: A dictionary where keys are strs and values are elements from the list.
    
    >>> list_to_dict([10, 15, 20, 25])
    {'apple': 10, 'banana': 15, 'grape': 20, 'orange': 25}
    >>> list_to_dict([10, 10, 10, 10])
    {'apple': 10, 'banana': 10, 'grape': 10, 'orange': 10}
    >>> list_to_dict([])
    Traceback (most recent call last):
    ...
    AssertionError: there must be 4 elements in the list
    >>> list_to_dict([5, 10, 15])
    Traceback (most recent call last):
    ...
    AssertionError: there must be 4 elements in the list
    >>> list_to_dict([30, 10, 4])
    Traceback (most recent call last):
    ...
    AssertionError: there must be 4 elements in the list
    >>> list_to_dict([0.3, 10, 4, 6])
    Traceback (most recent call last):
    ...
    AssertionError: the element must be a non-negative int
    >>> list_to_dict([0.5, 5, 10, 15])
    Traceback (most recent call last):
    ...
    AssertionError: the element must be a non-negative int
    """
    # checking that argument passed to function parameter is of list type
    assert type(input_list) == list, "the input must be a list"

    # checking that list is not empty
    assert len(input_list) == 4, "there must be 4 elements in the list"

    # checking that each element in the argument passed to function parameter is of int type
    assert type(input_list[0]) == int and input_list[0] >= 0, "the element must be a non-negative int"
    assert type(input_list[1]) == int and input_list[1] >= 0, "the element must be a non-negative int"
    assert type(input_list[2]) == int and input_list[2] >= 0, "the element must be a non-negative int"
    assert type(input_list[3]) == int and input_list[3] >= 0, "the element must be a non-negative int"

    # initializing empty dictionary object
    result = dict()

    # adding keys and corresponding values to dictionary
    result[APPLE] = input_list[0]
    result[BANANA] = input_list[1]
    result[GRAPE] = input_list[2]
    result[ORANGE] = input_list[3]

    return result

doctest.testmod()