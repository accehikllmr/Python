import doctest

def average_rating(a: int, b: int, c: int) -> float:
    """
    Returns the average of three values.

    Preconditions:      a   1 >= int >= 5
                        b   1 >= int >= 5
                        c   1 >= int >= 5

    >>> average_rating(1, 4, 4)
    3.0
    >>> average_rating(2, 5, 5)
    4.0
    >>> average_rating(0, 0, 0)
    Traceback (most recent call last):
    ...
    AssertionError: all ratings must be values from 1 to 5
    >>> average_rating(-3, 1, 2)
    Traceback (most recent call last):
    ...
    AssertionError: all ratings must be values from 1 to 5
    >>> average_rating(1, True, 2)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for parameter
    >>> average_rating(1, 4, '2')
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for parameter
    >>> average_rating(1, 2, 6)
    Traceback (most recent call last):
    ...
    AssertionError: all ratings must be values from 1 to 5
    >>> average_rating([1], 1, 1)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for parameter
    >>> average_rating(1, {1}, 1)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for parameter
    """

    '''
    checking that the rating for all arguments are of the correct type (int)
    this assertion first to avoid errors comparing different data types
    '''
    assert type(a) == type(b) == type(c) == int, "invalid data type for parameter"

    #checking that the ratings for all arguments are valid (from 1 to 5)
    assert (1 <= a <= 5) and (1 <= b <= 5) and (1 <= c <= 5), "all ratings must be values from 1 to 5"

    return (a + b + c) / 3

if __name__ == '__main__':
    doctest.testmod()