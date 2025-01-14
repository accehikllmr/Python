import doctest
from typing import List
from math import floor
from linear_search import linear_search

def binary_search(target: int, sequence: List[int]) -> int:
    """
    Finds the location of a number in a finite sorted sequence of distinct integers.

    Parameters:
        target (int): number whose location in sequence is sought
        sequence: finite sequence of sorted distinct integers

    Returns:
        (int): location (index) of number in sequence

    >>> binary_search(1, [1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 16, 18, 19, 20, 22])
    0
    >>> binary_search(19, [1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 16, 18, 19, 20, 22])
    13
    >>> binary_search(22, [1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 16, 18, 19, 20, 22])
    15
    >>> from random import randint
    >>> distinct_sequence = list(set([randint(1, 100) for i in range(100)]))
    >>> distinct_sequence.sort() # sorting since algorithm does not work otherwise
    >>> target_num = randint(1, 100)
    >>> linear_search(target_num, distinct_sequence) == binary_search(target_num, distinct_sequence) # comparing to previous algorithm
    True
    >>> binary_search(1.0, [1, 2, 3, 4, 5])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to target parameter must be an Integer object
    >>> binary_search(1, (1, 2, 3, 4, 5))
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to sequence must be a sorted List object
    >>> binary_search(1, [1, 2, 4, 3, 5])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to sequence must be a sorted List object
    >>> binary_search(1, [1, 2, 3, 3, 5])
    Traceback (most recent call last):
    ...
    AssertionError: all elements in List object passed to sequence parameter must be distinct Integer objects
    >>> binary_search(1, [1, 2, 3, "four", 5])
    Traceback (most recent call last):
    ...
    AssertionError: all elements in List object passed to sequence parameter must be distinct Integer objects
    """

    # validating arguments, checking if sorted rather than sorting, otherwise confounding original and new indices
    assert isinstance(target, int), "argument passed to target parameter must be an Integer object"

    for value in sequence:
        assert isinstance(value, int) and sequence.count(value) == 1, "all elements in List object passed to sequence parameter must be distinct Integer objects"

    # placed after validating individual elements, otherwise may make a string to int comparison
    assert isinstance(sequence, list) and sorted(sequence) == sequence, "argument passed to sequence must be a sorted List object"

    # initial delimiters, to define search interval, where sequence has not been split in half, index is length - 1 for last index value
    left_delimiter = 0
    right_delimiter = len(sequence) - 1

    # searching through sequence, initially whole and after some subset taken from splitting it in half
    while left_delimiter < right_delimiter:
        # finding middle delimiter to split sequence in half
        middle_delimiter = floor((left_delimiter + right_delimiter) / 2)
        # comparing target value with value in middle of list
        if target > sequence[middle_delimiter]:
            # update left_delimiter, since target value must be above it (only works because since is sorted)
            left_delimiter = middle_delimiter + 1
        else:
            # update right_delimiter, since target value must be below it
            right_delimiter = middle_delimiter

    # only need to check left delimiter, since eventually every single sequence will be a singleton
    if target == sequence[left_delimiter]:
        return left_delimiter
    else:
        return -1

doctest.testmod()