import doctest

# instantiate dictionary object with allowed vehicles and corresponding number of wheels
vehicles = {'bicycle': 2, 'tricycle': 3, 'car': 4, 'truck': 18}

'''
implementing these functions does not simplify the program, although it does make it more robust, protecting from
invalid inputs and semantic errors (e.g. incorrect mathematical operations)
though there are no explicit tests for the calculation of total wheels, there are for the algorithms calculations
'''
def add_to_total(all_wheels: int, some_wheels: int) -> int:
    """
    Updates total number of wheels for all vehicles being counted.

    Parameters:
        all_wheels (int): updated count of total wheels, updated and passed anew every iteration, non-negative integer
        some_wheels (int): number of wheels for a given vehicle type, non-negative integer

    Returns:
        (int): updated count of total wheels

    >>> add_to_total(5, 5)
    10
    >>> add_to_total(0, 0)
    0
    >>> add_to_total(-5, 5)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to all_wheels parameter must be a non-negative integer
    >>> add_to_total(5, -5)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to some_wheels parameter must be a non-negative integer
    """

    # checking that values for wheels are not negative
    assert isinstance(all_wheels, int) and all_wheels >= 0, "argument passed to all_wheels parameter must be a non-negative integer"
    assert isinstance(some_wheels, int) and some_wheels >= 0, "argument passed to some_wheels parameter must be a non-negative integer"

    return all_wheels + some_wheels


def calculate_wheels(vehicle_type: str, num: int) -> int:
    """
    Calculates the number of wheels for a vehicle type, given the quantity of vehicles.

    Parameters:
        vehicle_type(str): type of vehicle taken from keys in dictionary of vehicles
        num (int): quantity of the type of vehicles

    Returns:
        (int): number of wheels for the total quantity of vehicles

    >>> calculate_wheels('bicycle', 2)
    4
    >>> calculate_wheels('tricycle', 4)
    12
    >>> calculate_wheels('car', 8)
    32
    >>> calculate_wheels('truck', 16)
    288
    >>> calculate_wheels('car', -2)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to num parameter must be a non-negative integer
    """

    # no need to check for valid string, since pulled directly from dictionary, so just checking user input integer
    assert isinstance(num, int) and num >= 0, "argument passed to num parameter must be a non-negative integer"

    return num * vehicles[vehicle_type]

# initialize string for output message
output_message = f"\nFor "

# initialize variable to track total number of wheels
total_wheels = 0

# iterate outside of function, since each loop gets user input (keep outside function to permit testing)
for vehicle in vehicles.keys():
    # get quantity of vehicle
    quantity = int(input(f"How many {vehicle}s? "))
    # add product of vehicles and wheels per vehicle to total wheel count
    these_wheels = calculate_wheels(vehicle, quantity)
    # add wheels for this vehicle to total number of wheels, need both inputs for tests ot validate values
    total_wheels = add_to_total(total_wheels, these_wheels)
    # update output message
    output_message += f"{quantity} {vehicle}s, "

print(output_message + f"there are {total_wheels} total wheels.")

doctest.testmod()