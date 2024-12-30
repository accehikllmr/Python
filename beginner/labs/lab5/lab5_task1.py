import doctest

PI = 3.14159

def circle_area(radius: float) -> float:
    """
    This function takes radius r as input and returns the area of the circle
    using the formula Area = pi * r ** 2

    Preconditions:  radius  0.0 <= float <= 1000.0

    >>> circle_area(2.0)
    12.56636
    >>> circle_area(4.0)
    50.26544
    """

    assert type(radius) == float, "radius must be a float"
    assert 0.0 <= radius <= 1000.0, "radius must be in range of 0.0 to 1000.0"

    return PI * radius ** 2

def circle_circumference(radius: float) -> float:
    """
    This function takes radius r as input and returns the circumference of the circle
    using the formula Circumference = 2 * pi * r

    Preconditions:  radius  0.0 <= float <= 1000.0

    >>> circle_circumference(2.0)
    12.56636
    >>> circle_circumference(4.0)
    25.13272
    """

    assert type(radius) == float, "radius must be a float"
    assert 0.0 <= radius <= 1000.0, "radius must be in range of 0.0 to 1000.0"

    return 2 * PI * radius

doctest.testmod()