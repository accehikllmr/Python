import doctest
from typing import List

def find_maximum(sequence: List[int]) -> int:
    """
    Finds the maximum value integer in a finite sequence of integers.

    Parameters:
        sequence (List[int]): finite sequence of integers

    Returns:
        (int): maximum value integer in finite sequence of integers

    >>> find_maximum([1, 2, 3, 4, 5])
    5
    >>> find_maximum([5, 4, 3, 2, 1])
    5
    >>> find_maximum([3, 2, 5, 1, 4])
    5
    >>> find_maximum([5, 5, 5, 5, 5])
    5
    >>> from random import randint
    >>> finite_sequence = [randint(1, 100) for i in range(1, 100)]
    >>> find_maximum(finite_sequence) == max(finite_sequence) # comparing to known working built-in function
    True
    >>> find_maximum((1, 2, 3, 4, 5))
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to sequence parameter must be a List object
    >>> find_maximum([1, 'two', 3, 4, 5])
    Traceback (most recent call last):
    ...
    AssertionError: all elements in List object passed to sequence argument must be Integer objects
    """

    # argument validation
    assert isinstance(sequence, list), "argument passed to sequence parameter must be a List object"

    for value in sequence:
        assert isinstance(value, int), "all elements in List object passed to sequence argument must be Integer objects"

    # rather than starting at value of 0, set first element in sequence as first maximum value (reduces iteration by one)
    maximum_value = sequence[0]

    # iterating over sequence, but starting at second element, since the first has already been checked, above
    for value in sequence[1:]:
        # checking whether current value is greater than the maximum value
        if maximum_value < value:
            # updating maximum value
            maximum_value = value

    return maximum_value

doctest.testmod()

# commentaire