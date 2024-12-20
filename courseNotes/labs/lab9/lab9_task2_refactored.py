import doctest
from typing import List, Dict

# not taking argument as nested list with different data types, since not sure how to write in function signature
def nested_list_to_dict(item_list: List[List[str]]) -> Dict[str, int]:
    """
    Converts a nested list of strings and integers into a dictionary with string integer pairings.

    Parameters:
        item_list (List[str, int]): nested list containing string-integer pairings

    Returns:
        (Dict[str, int]): dictionary with string-integer pairings of the original nested list

    >>> nested_list_to_dict([['apple', '2']])
    {'apple': 2}
    >>> nested_list_to_dict([['apple', '2'], ['banana', '4'], ['orange', '7'], ['mulberry', '1']])
    {'apple': 2, 'banana': 4, 'orange': 7, 'mulberry': 1}
    >>> nested_list_to_dict([[]])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to item_list parameter must have inner lists of length 2
    >>> nested_list_to_dict({})
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to item_list parameter must be a list object
    >>> nested_list_to_dict([()])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to item_list parameter must only contain list objects in its outer list
    >>> nested_list_to_dict([['apple', 2]])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to item_list parameter must only contain string objects in its inner list
    >>> nested_list_to_dict([['2', '2']])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to item_list parameter must have an alphabetic string as the first element in its inner list
    >>> nested_list_to_dict([['apple', 'apple']])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to item_list parameter must have a non-negative numeric string as the second element in its inner list
    """

    # checking type of outer list
    assert isinstance(item_list, list), "argument passed to item_list parameter must be a list object"

    # checking type of elements in outer list
    for item in item_list:
        assert isinstance(item, list), "argument passed to item_list parameter must only contain list objects in its outer list"
        # checking that inner list has exact length of 2
        assert len(item) == 2, "argument passed to item_list parameter must have inner lists of length 2"
        # checking types of elements in inner list, using range since distinguishing desired values based on positioning
        for i in range(len(item)):
            assert isinstance(item[i], str), "argument passed to item_list parameter must only contain string objects in its inner list"
            # checking that strings are either alphabetic or numeric
            if i == 0:
                assert item[0].isalpha(), "argument passed to item_list parameter must have an alphabetic string as the first element in its inner list"
            else:
                # also checking that numerical values are only non-negative integers
                assert item[1].isdigit() and int(item[1]) >= 0, "argument passed to item_list parameter must have a non-negative numeric string as the second element in its inner list"

    # instantiating dictionary object
    item_dictionary = {}

    # iterating through pair in nested list
    for pair in item_list:
        # assigning alphabetic string object as key, numeric string object as value (need to convert to integer object)
        item_dictionary[pair[0]] = int(pair[1])

    return item_dictionary

doctest.testmod()