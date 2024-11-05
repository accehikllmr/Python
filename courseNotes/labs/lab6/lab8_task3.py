################################### TASK 3 ###################################
### Starting code ###

import doctest

def approximate_pi(m: int) -> float:
    """
    Calculates the value of the irrational number pi to a precision given by parameter m.

    >>> approximate_pi(0)
    4.0
    >>> approximate_pi(1)
    2.6667
    >>> approximate_pi(5)
    2.976
    >>> approximate_pi(8)
    3.2524
    >>> approximate_pi(20)
    3.1892
    >>> approximate_pi(1000)
    3.1426
    >>> approximate_pi(1.0)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to parameter m must be a non-negative integer
    >>> approximate_pi('ten')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to parameter m must be a non-negative integer
    """
    # checking preconditions
    # parameter m must be a positive integer
    assert type(m) == int and m >= 0, "argument passed to parameter m must be a non-negative integer"

    # variable to contain approximation of pi
    result = 0

    # summation from 0 until m (+1 to include m in summation)
    for n in range(0, m + 1):
        # formula for summation of each term
        result += ((-1) ** n) / (2 * n + 1)

    # multiplying summation by coefficient
    result = 4 * result

    # rounding result of summation, to avoid problems caused by floating point values
    return round(result, 4)

doctest.testmod()