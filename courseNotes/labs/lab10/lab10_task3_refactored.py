import doctest
from typing import List

def majority_element(nums: List[int]) -> List[int]:
    """
    Returns the numbers which appear most frequently in a list.

    Parameters:
        nums (List[int]): list of integers

    Returns:
        (List[int]): list of integers which appear most frequently in the list

    >>> majority_element([2, 2, 2, 3, 1, 2, 2, 3, 3])
    [2]
    >>> majority_element([3, 3, 1, 1])
    [1, 3]
    >>> majority_element([5, 5, 5, 5, 5])
    [5]
    >>> majority_element([1, 3, 2, 1, 3, 3, 3, 1, 2, 3, 2, 1, 2, 2, 1])
    [1, 2, 3]
    >>> majority_element([1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 2, 2])
    [2]
    >>> majority_element(list((1, 2, 3)))
    [1, 2, 3]
    >>> majority_element([])
    []
    >>> majority_element("132133312321221")
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to nums parameter must be a list object
    >>> majority_element(['1', '2'])
    Traceback (most recent call last):
    ...
    AssertionError: all elements in the list must be integer objects
    >>> majority_element((3, 3, 4, 5))
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to nums parameter must be a list object
    >>> majority_element({3, 3, 4, 5})
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to nums parameter must be a list object
    """

    # validating arguments
    assert isinstance(nums, list), "argument passed to nums parameter must be a list object"

    # converting to set to identify individual integers contained in list, back to list then to sort
    unique_nums = sorted(list(set(nums)))

    # don't need separate function, as in last version
    for num in nums:
        assert isinstance(num, int), "all elements in the list must be integer objects"

    # list containing most frequently occurring numbers from original list
    mode_list = []

    # checking each number, from entire length of list to 1, to see if it appears that many times
    for frequency in range(len(nums), 0, -1):
        for unique_num in unique_nums:
            # condition to add number, according to current value of iteration
            if nums.count(unique_num) == frequency:
                mode_list.append(unique_num)
        # stop iterating if any numbers in list, otherwise n iterates and less frequent numbers could be added
        if len(mode_list) != 0:
            return mode_list

    return mode_list

doctest.testmod()