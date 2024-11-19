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
    
    s = {} # initialize an empty set
    result = None # Note: None means the data has no type
    
    for num in nums:
    if not num in s:
    result = True
    continue
    else:
    result = False
    s.append(num)
        
    return result