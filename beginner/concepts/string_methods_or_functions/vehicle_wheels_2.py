import doctest

def count_wheels(num_bicycles: int, num_tricycles: int, num_cars: int, num_trucks: int) -> int:
    """
    Given a number of bicycles, tricycles, car and trucks, the total number of wheels is calculated.

    Preconditions:  num_bicycles    int >= 0
                    num_tricycles   int >= 0
                    num_cars        int >= 0
                    num_trucks      int >= 0

    >>> count_wheels(0, 0, 0, 0)
    0
    >>> count_wheels(10, 1, 3, 2)
    71
    >>> count_wheels(-1, 1, 3, 2)
    Traceback (most recent call last):
    ...
    AssertionError: num_bicycles must be a non-negative integer
    >>> count_wheels('1', 1, 3, 2)
    Traceback (most recent call last):
    ...
    AssertionError: argument with invalid data type passed to num_bicycles parameter
    """

    assert type(num_bicycles) == int, "argument with invalid data type passed to num_bicycles parameter"
    assert type(num_tricycles) == int, "argument with invalid data type passed to num_tricycles parameter"
    assert type(num_cars) == int, "argument with invalid data type passed to num_cars parameter"
    assert type(num_trucks) == int, "argument with invalid data type passed to num_trucks parameter"

    assert num_bicycles >= 0, "num_bicycles must be a non-negative integer"
    assert num_tricycles >= 0, "num_tricycles must be a non-negative integer"
    assert num_cars >= 0, "num_cars must be a non-negative integer"
    assert num_trucks >= 0, "num_trucks must be a non-negative integer"

    wheels_bicycle = 2
    wheels_tricycle = 3
    wheels_car = 4
    wheels_truck = 18

    return num_bicycles * wheels_bicycle + num_tricycles * wheels_tricycle + num_cars * wheels_car + num_trucks * wheels_truck

doctest.testmod()

# again, lab2 activity turned into a function