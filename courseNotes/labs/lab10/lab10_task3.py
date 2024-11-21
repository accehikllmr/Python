import doctest
from typing import List

def all_integers(a_list: list) -> bool:
    """
    Determines whether all elements of a list object are integer objects.

    Parameters:
        a_list (list): list of objects of any type

    Returns:
        (bool): evaluation of whether all objects in list are integer objects

    >>> all_integers([1, 2, 3])
    True
    >>> all_integers([1, 2, '3'])
    False
    >>> all_integers([])
    True
    >>> all_integers((1, 2, 3))
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to function parameter must be a list object
    """
    # checking if argument passed to function parameter is a list object
    assert type(a_list) == list, "argument passed to function parameter must be a list object"

    # checking whether each element in the list is an integer objects
    for i in a_list:
        # stopping loop and function as soon as non integer object is found
        if type(i) != int:
            return False
    return True

def majority_element(nums: List[int]) -> List[int]:
    """
    Returns the numbers which appear most frequently in a list.

    Parameters:
        nums (List[int]): list of integers

    Returns:
        (List[int]):   list of integers which appear most frequently in the list

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
    # checking that argument passed to parameter is a list object
    assert type(nums) == list, "argument passed to nums parameter must be a list object"

    # checking that elements of list object are all integers
    assert all_integers(nums), "all elements in the list must be integer objects"

    # converting to set to identify individual integers contained in list
    unique_nums = set(nums)

    # initializing dictionary object to store and pair integers to their respective frequencies
    frequencies = {}

    # initializing list object to store most integers which most frequently appear in list
    max_frequency = []

    # looping through each unique number
    for num in unique_nums:
        # add integer (key) - frequency (value) pair to dictionary object
        frequencies[num] = nums.count(num)

    # iterating through all dictionary items
    for pair in frequencies.items():
        # checking if value element of tuple (frequency) is equal to the maximum frequency in the dictionary
        if pair[1] == max(frequencies.values()):
            # appending integers associated with maximum frequency to list of most frequently appearing integers
            max_frequency.append(pair[0])

    return max_frequency

doctest.testmod()