import doctest
from typing import List

def contains_duplicates(nums: List[int]) -> bool:
    """
    Returns whether there are duplicate elements in a given list of numbers.

    Parameters:
        nums (List[int]): list of numbers

    Returns:
        (bool): whether list of numbers contains duplicates

    >>> contains_duplicates([1, 2, 3, 4, 1])
    True
    >>> contains_duplicates([5, 6, 7, 8])
    False
    >>> contains_duplicates([2, 0, 1, 4, 5, 9, 10, 0])
    True
    >>> contains_duplicates([0])
    False
    >>> contains_duplicates((1, 2, 3))
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to nums parameter must be a non-empty list object
    >>> contains_duplicates([])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to nums parameter must be a non-empty list object
    >>> contains_duplicates([1, 2.0, 3])
    Traceback (most recent call last):
    ...
    AssertionError: all elements in list must be integer objects
    """

    assert isinstance(nums, list) and nums != [], "argument passed to nums parameter must be a non-empty list object"

    # looping over all numbers in list
    for num in sorted(nums):
        # validating list elements
        assert isinstance(num, int), "all elements in list must be integer objects"
        # checking if number appears in list more than once
        if nums.count(num) > 1:
            return True

    return False

doctest.testmod()