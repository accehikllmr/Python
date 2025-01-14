import doctest
from typing import List

def bubble_sort(sequence: List[int]) -> List[int]:
    """
    Sorts a sequence of integers in ascending order.

    Parameters:
        sequence (List[int]): sequence of integers

    Returns:
        (List[int]): sorted sequence of integers

    >>> bubble_sort([-3, -2, -4, -1, -5])
    [-5, -4, -3, -2, -1]
    >>> bubble_sort([3, 2, 4, 1, 5])
    [1, 2, 3, 4, 5]
    >>> bubble_sort([-1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1]
    >>> bubble_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> bubble_sort([-5, -4, -3, -2, -1])
    [-5, -4, -3, -2, -1]
    >>> bubble_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> from random import randint
    >>> test_sequence = [randint(1, 100) for k in range(100)]
    >>> bubbled_test_sequence = bubble_sort(test_sequence)
    >>> test_sequence.sort()
    >>> test_sequence == bubbled_test_sequence
    True
    >>> bubble_sort((5, 4, 1, 2, 3))
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to sequence parameter must be a List object of length 2 or greater
    >>> bubble_sort([1])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to sequence parameter must be a List object of length 2 or greater
    >>> bubble_sort([2, 3, 4, 1.0, 5])
    Traceback (most recent call last):
    ...
    AssertionError: all elements of List object must be Integer objects
    """

    # validating arguments
    assert isinstance(sequence, list) and len(sequence) >= 2, "argument passed to sequence parameter must be a List object of length 2 or greater"

    for value in sequence:
        assert isinstance(value, int), "all elements of List object must be Integer objects"

    '''
    iterating over entire list, except for last element (no next element with which to switch)
    starting at 1 rather than 0, since need to remove value from range of inner loop as sort covers smaller range
    hence, initial value of 0 throws IndexError
    '''
    for i in range(1, len(sequence)):
        # iterating over indices of sequence, to compare adjacent values, shortening at each iteration
        for j in range(len(sequence) - i):
            # condition for switching positions of elements
            if sequence[j] > sequence[j + 1]:
                # storing current value, since will be replaced next line
                move = sequence[j]
                # replacing first value with second (switching positions)
                sequence[j] = sequence[j + 1]
                # replacing second value with first (using stored value)
                sequence[j + 1] = move

    return sequence

doctest.testmod()