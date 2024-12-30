import doctest
from typing import List

def is_sorted(nums: List[int]) -> bool:
    """
    determines if a list is sorted

    >>> is_sorted([1, 2, 2, 3, 4])
    True
    >>> is_sorted([9, 5, 10])
    False
    >>> is_sorted([6])
    True
    """
    # check pre-conditions
    assert type(nums) == list, "the input must be a list"

    # create variable to index into the list
    i = 1

    # loop through elements checking if current element is >= the last
    while i < len(nums):
        if nums[i] < nums[i - 1]:
            return False
        i += 1
    return True

def merge_lists(list_1: List[int], list_2: List[int]) -> List[int]:
    """
    merges two sorted lists into one

    >>> merge_lists([0, 1, 2, 3], [6, 7, 8])
    [0, 1, 2, 3, 6, 7, 8]
    >>> merge_lists([0, 1, 3, 5], [0, 1, 2, 4, 6])
    [0, 0, 1, 1, 2, 3, 4, 5, 6]
    >>> merge_lists([], [1, 5, 10])
    [1, 5, 10]
    """
    # check preconditions
    assert is_sorted(list_1), "list_1 is unsorted"
    assert is_sorted(list_2), "list_2 is unsorted"

    # declare variables to index into our lists
    i = 0 # for iterating through list_1
    j = 0 # for iterating through list_2

    # declare the new list which will contain the merged elements
    merged_list = []

    # loop through lists adding elements until we are at the end of one
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            merged_list.append(list_1[i])
            i += 1
        else:
            merged_list.append(list_2[j])
            j += 1

    # add the rest of the elements from the challenges list
    if i >= len(list_1):
        merged_list.extend(list_2[j:])
    else:
        merged_list.extend(list_1[i:])

    # return the merged list
    return merged_list

doctest.testmod()