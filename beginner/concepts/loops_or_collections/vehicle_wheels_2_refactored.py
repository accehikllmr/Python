import doctest

def count_wheels(num_bicycles: int, num_tricycles: int, num_cars: int, num_trucks: int) -> int:
    """
    Given a number of bicycles, tricycles, car and trucks, the total number of wheels is calculated.

    Parameters:
        num_bicycles (int): quantity of bicycles
        num_tricycles (int): quantity of tricycles
        num_cars (int): quantity of cars
        num_trucks (int): quantity of trucks

    Returns:
        (int): total wheels for all vehicles combined

    >>> count_wheels(0, 0, 0, 0)
    0
    >>> count_wheels(10, 1, 3, 2)
    71
    >>> count_wheels(-1, 1, 3, 2)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to num_bicycles parameter must be a non-negative integer
    >>> count_wheels('1', 1, 3, 2)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to num_bicycles parameter must be a non-negative integer
    """

    # use isinstance rather than type, latter is bad form, also combining assertions to make more concise
    assert isinstance(num_bicycles, int) and num_bicycles >= 0, "argument passed to num_bicycles parameter must be a non-negative integer"
    assert isinstance(num_tricycles, int) and num_tricycles >= 0, "argument passed to num_tricycles parameter must be a non-negative integer"
    assert isinstance(num_cars, int) and num_cars >= 0, "argument passed to num_cars parameter must be a non-negative integer"
    assert isinstance(num_trucks, int) and num_trucks >= 0, "argument passed to num_trucks parameter must be a non-negative integer"

    # dictionary object to contain attributes of each vehicle type (but OOP would probably be better here)
    vehicles = {
        'bicycle': {
            'wheels': 2,
            'quantity': num_bicycles
        },
        'tricycle': {
            'wheels': 3,
            'quantity': num_tricycles
        },
        'car': {
            'wheels': 4,
            'quantity': num_cars
        },
        'truck': {
            'wheels': 18,
            'quantity': num_trucks
        }
    }

    # to count total wheels
    total_wheels = 0

    # iterating through outer dictionary keys
    for vehicle in vehicles.keys():
        # set to 1, since each iteration multiplies the value (instantiating it at 0 keeps it as 0)
        wheels = 1
        # iterating through inner dictionary keys, but need to specify temporary variable for outer key to access inner keys
        for attribute in vehicles[vehicle].keys():
            # calculate wheels for single vehicle
            wheels *= vehicles[vehicle][attribute]
        total_wheels += wheels

    # above is not as concise as previous approach, but it helps better understand how to manipulate dictionaries

    return total_wheels

doctest.testmod()