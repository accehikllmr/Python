import doctest

def is_healthy(height: float, weight: float) -> bool:
    """
    Return True if someone is healthy given the height in centimeters and the weight in kilograms.

    >>> is_healthy(158.0, 61.3)
    True
    >>> is_healthy(187.3, 70.5)
    True
    >>> is_healthy(195.1, 45.1)
    False
    >>> is_healthy(4.0, 98.7)
    False
    >>> is_healthy(170.0, 71.9)
    True
    >>> is_healthy(175.0, 76.4)
    True
    >>> is_healthy(180.0, 60.0)
    True
    >>> is_healthy(185.5, 63.5)
    True
    >>> is_healthy("178.3", 60.4)
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument type: height
    >>> is_healthy(178.3, 60)
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument type: weight
    >>> is_healthy(0.0, 50.0)
    Traceback (most recent call last):
    ...
    AssertionError: One's height must be positive and cannot be over 3 m
    >>> is_healthy(173.0, 0.0)
    Traceback (most recent call last):
    ...
    AssertionError: One's weight must be positive and cannot be over 640 kg
    >>> is_healthy(-10.0, 50.0)
    Traceback (most recent call last):
    ...
    AssertionError: One's height must be positive and cannot be over 3 m
    >>> is_healthy(173.0, -50.0)
    Traceback (most recent call last):
    ...
    AssertionError: One's weight must be positive and cannot be over 640 kg
    >>> is_healthy(300.0, 150.0)
    Traceback (most recent call last):
    ...
    AssertionError: One's height must be positive and cannot be over 3 m
    >>> is_healthy(173.0, 640.0)
    Traceback (most recent call last):
    ...
    AssertionError: One's weight must be positive and cannot be over 640 kg
    """

    #changed type from int to float
    assert type(height) == float, "invalid argument type: height"
    assert type(weight) == float, "invalid argument type: weight"

    '''
    changed values to not be inclusive, since values must be positive and not inclusive of upper bound
    changed from 3.0 to 300.0, since height is given in cm not m
    '''
    assert 0.0 < height < 300.0, "One's height must be positive and cannot be over 3 m"
    assert 0.0 < weight < 640.0, "One's weight must be positive and cannot be over 640 kg"

    #converting height from meters to centimeters
    height = height / 100

    #added brackets around the denominator since it is squared
    bmi = weight / (height * height)

    #added 1 after comma to include one digit after the decimal value
    bmi = round(bmi,1 )

    #added equal sign for values to be inclusive
    return 18.5 <= bmi <= 24.9

doctest.testmod()