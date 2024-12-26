import doctest
from typing import List

def merge_lists(list_1: List[int], list_2: List[int]) -> List[int]:
    """
    Merges two sorted lists into one sorted list.

    Parameters:
        list_1 (List[int]): list of integers, not necessarily sorted
        list_2 (List[int]): list of intengers, not necessarily sorted

    Returns:
        (List[int]): merged list of integers, sorted

    >>> merge_lists([0, 1, 2, 3], [6, 7, 8])
    [0, 1, 2, 3, 6, 7, 8]
    >>> merge_lists([0, 1, 3, 5], [0, 1, 2, 4, 6])
    [0, 0, 1, 1, 2, 3, 4, 5, 6]
    >>> merge_lists([], [1, 5, 10])
    [1, 5, 10]
    >>> merge_lists([3, 1, 9, 8], [7, 1, 1, 4])
    [1, 1, 1, 3, 4, 7, 8, 9]
    >>> merge_lists([1], [2])
    [1, 2]
    >>> merge_lists([], [])
    []
    >>> merge_lists([1, 2, 3], (1, 2, 3))
    Traceback (most recent call last):
    ...
    AssertionError: arguments passed to list_1 and list_2 parameters must be list objects
    >>> merge_lists([1, 2, 3], [1.0, 2, 3])
    Traceback (most recent call last):
    ...
    AssertionError: all elements in list object must be integer objects
    >>> merge_lists([1, 'b', 3], [1, 2, 3])
    Traceback (most recent call last):
    ...
    AssertionError: all elements in list object must be integer objects
    """
    # check preconditions, but no need to check if sorted, since merged list is sorted at the end
    assert isinstance(list_1, list) and isinstance(list_2, list), "arguments passed to list_1 and list_2 parameters must be list objects"

    for num in list_1:
        assert isinstance(num, int), "all elements in list object must be integer objects"

    for num in list_2:
        assert isinstance(num, int), "all elements in list object must be integer objects"

    # declare the new list which will contain the merged elements
    merged_list = list_1 + list_2

    # return the merged list
    return sorted(merged_list)

doctest.testmod()