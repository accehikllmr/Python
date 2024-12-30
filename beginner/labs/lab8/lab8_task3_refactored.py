import doctest
from math import pi

def approximate_pi(m: int) -> str:
    """
    Calculates the value of the irrational number pi to a precision given by parameter m.

    Parameters:
        m (int): degree of precision in calculation of pi constant

    Returns:
        (str): output to user with approximated value of pi

    >>> approximate_pi(0)
    'pi = 4.0, difference from actual value is 0.8584.'
    >>> approximate_pi(1)
    'pi = 2.6667, difference from actual value is 0.4749.'
    >>> approximate_pi(5)
    'pi = 2.976, difference from actual value is 0.1655.'
    >>> approximate_pi(8)
    'pi = 3.2524, difference from actual value is 0.1108.'
    >>> approximate_pi(20)
    'pi = 3.1892, difference from actual value is 0.0476.'
    >>> approximate_pi(1000)
    'pi = 3.1426, difference from actual value is 0.001.'
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
    assert isinstance(m, int) and m >= 0, "argument passed to parameter m must be a non-negative integer"

    # variable to contain approximation of pi
    result = 0

    # summation from 0 until m (+1 to include m in summation)
    for n in range(0, m + 1):
        # formula for summation of each term
        result += ((-1) ** n) / (2 * n + 1)

    # multiplying summation by coefficient
    result *= 4

    # rounding result of summation, to avoid problems caused by floating point values
    return f"pi = {round(result, 4)}, difference from actual value is {abs(round(result - pi, 4))}."

doctest.testmod()