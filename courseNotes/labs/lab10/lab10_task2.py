import doctest
from typing import List

def contains_duplicates(nums: List[int]) -> bool:
    """
    returns whether there are duplicate elements in a given list
    
    >>> contains_duplicates([1, 2, 3, 4, 1])
    True
    >>> contains_duplicates([5, 6, 7, 8])
    False
    >>> contains_duplicates([2, 0, 1, 4, 5, 9, 10, 0])
    True
    >>> contains_duplicates([0])
    False
    """
    
    s = set() # initialize an empty set

    # looping over all numbers in list
    for num in nums:
        # add each number to the set, since duplicates will automatically be discarded
        s.add(num)

    # if lengths of set and list are not equal, then there are duplicates in the list which have been discarded by set
    return len(s) != len(nums)

doctest.testmod()