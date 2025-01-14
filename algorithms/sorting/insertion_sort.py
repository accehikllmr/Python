import doctest
from typing import List

def insertion_sort(sequence: List[int]) -> List[int]:
    """
    Sorts a sequence of integers in ascending order.

    Parameters:
        sequence (List[int]): sequence of integers

    Returns:
        (List[int]): sorted sequence of integers

    >>> insertion_sort([-3, -2, -4, -1, -5])
    [-5, -4, -3, -2, -1]
    >>> insertion_sort([3, 2, 4, 1, 5])
    [1, 2, 3, 4, 5]
    >>> insertion_sort([-1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1]
    >>> insertion_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> insertion_sort([-5, -4, -3, -2, -1])
    [-5, -4, -3, -2, -1]
    >>> insertion_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> from random import randint
    >>> test_sequence = [randint(1, 100) for k in range(100)]
    >>> bubbled_test_sequence = insertion_sort(test_sequence)
    >>> test_sequence.sort()
    >>> test_sequence == bubbled_test_sequence
    True
    >>> insertion_sort((5, 4, 1, 2, 3))
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to sequence parameter must be a List object of length 2 or greater
    >>> insertion_sort([1])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to sequence parameter must be a List object of length 2 or greater
    >>> insertion_sort([2, 3, 4, 1.0, 5])
    Traceback (most recent call last):
    ...
    AssertionError: all elements of List object must be Integer objects
    """

    # validating arguments
    assert isinstance(sequence, list) and len(sequence) >= 2, "argument passed to sequence parameter must be a List object of length 2 or greater"

    for value in sequence:
        assert isinstance(value, int), "all elements of List object must be Integer objects"

    # iterating through entire sequence of numbers, but starting at second number in list
    for index_sort in range(1, len(sequence) - 1):
        # since sorting starts at second number, first comparison is with first number
        index_compare = 0
        # checking if number to be sorted is larger than some number
        while sequence[index_sort] > sequence[index_compare]:
            # so long as it is larger, increment index to compare it to next number in list
            index_compare += 1
        # storing number which can be sorted
        num_sort = sequence[index_sort]

        # something is not working after this point, but random case works, and mirror cases don't work

        # iterating through already sorted slice of sequence
        for k in range(index_sort - index_compare - 1):
            sequence[index_sort - k] = sequence[index_sort - k - 1]

        sequence[index_compare] = num_sort


    return sequence

doctest.testmod()