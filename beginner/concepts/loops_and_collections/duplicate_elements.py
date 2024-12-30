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
    """

    # converts list to set, thus eliminating duplicate elements
    set_nums = set(nums)

    # compares length of error_checking_and_collections, if equal then nothing eliminated, hence no duplicates in set
    return len(set_nums) != len(nums)

doctest.testmod()