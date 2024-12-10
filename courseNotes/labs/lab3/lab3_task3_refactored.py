import doctest

def needs_ticket(age: int, height: float) -> bool:
    """
    Computes whether a child of a certain age and height requires a ticket to ride
    a roller coaster.

    Parameters:
         age (int): age of the child, in years
         height (float): height of the child, in centimeters

    Returns:
        (bool): whether the child needs to buy a ticket

    >>> needs_ticket(6, 120.0)
    False
    >>> needs_ticket(7, 120.0)
    True
    >>> needs_ticket(6, 120.1)
    True
    >>> needs_ticket(0, 120.1)
    True
    >>> needs_ticket(7, 0.1)
    True
    >>> needs_ticket(0, 0)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to height parameter must be a positive integer
    >>> needs_ticket(-1, 0.1)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to age parameter must be a non-negative integer
    """

    # checking that age and height are possible values (not checking class, since guaranteed externally)
    assert age >= 0, "argument passed to age parameter must be a non-negative integer"
    assert height > 0, "argument passed to height parameter must be a positive integer"

    # important to stress how simple this evaluation can be, not requiring any conditionals whatsoever
    return age > 6 or height > 120

# conditional which call function and return value is boolean, for simplicity, not checking input inside function
if needs_ticket(int(input("What is the child's age? ")), float(input("What is the child's height? "))):
    print("The child needs a ticket to ride.")
else:
    print("The child doesn't need a ticket to ride.")

doctest.testmod()