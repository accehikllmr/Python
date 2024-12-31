import doctest
from typing import List

def linear_search(target: int, sequence: List[int]) -> int:
    """
    Finds the location of a number in a finite sequence of distinct integers.

    Parameters:
        target (int): number whose location in sequence is sought
        sequence: finite sequence of distinct integers

    Returns:
        (int): location (index) of number in sequence

    >>> linear_search(5, [1, 2, 3, 4, 5])
    4
    >>> linear_search(5, [5, 4, 3, 2, 1])
    0
    >>> linear_search(5, [3, 2, 5, 1, 4])
    2
    >>> import random # unsure of syntax needed to use shuffle without random. preceding it
    >>> distinct_sequence = list(set([random.randint(1, 100) for i in range(100)])) # made distinct by converting to set
    >>> random.shuffle(distinct_sequence) # shuffled since conversion to set orders list
    >>> target_num = random.randint(1, 100) # generating a target number, to search for in sequence
    >>> distinct_sequence.index(target_num) == linear_search(target_num, distinct_sequence) # built-in throws exception if target not found
    True
    >>> linear_search("one", [1, 2, 3, 4, 5])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to target parameter must be an Integer object
    >>> linear_search(1, (1, 2, 3, 4, 5))
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to sequence parameter must be a List object
    >>> linear_search(1, [1, 2, "three", 4, 5])
    Traceback (most recent call last):
    ...
    AssertionError: all elements in List object passed to sequence parameter must be distinct Integer objects
    >>> linear_search(3, [1, 3, 4, 2, 3])
    Traceback (most recent call last):
    ...
    AssertionError: all elements in List object passed to sequence parameter must be distinct Integer objects
    """

    # validating arguments
    assert isinstance(target, int), "argument passed to target parameter must be an Integer object"
    assert isinstance(sequence, list), "argument passed to sequence parameter must be a List object"

    for value in sequence:
        assert isinstance(value, int) and sequence.count(value) == 1, "all elements in List object passed to sequence parameter must be distinct Integer objects"

    # initializing variable to track index through search
    target_index = 0

    # continues iterating so long as still within sequence range AND number has not been matched
    while target_index < len(sequence) and target != sequence[target_index]:
        # increment count through sequence so long as above conditions hold, equals len(sequence) if target not found
        target_index += 1

    # if target_index has exceeded range of list (target not fount), set variable to -1
    if target_index >= len(sequence):
        target_index = -1

    return target_index

doctest.testmod()