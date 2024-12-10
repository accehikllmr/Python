import doctest

def calculate_bmi(a_weight: str, a_height: str) -> str:
    """
    Calculates an individual's body-mass index based on their height and weight.

    Parameters:
         a_height (str): height of the individual, in meters
         a_weight (str): weight of the individual, in kilograms

    Returns:
        (str): output statement giving the individual's body-mass index to the user

    >>> calculate_bmi('80.0', '187.0')
    'For a height of 1.87 meters and a weight of 80.0 kilograms, the BMI is 22.9.'
    >>> calculate_bmi('80.0', '187')
    'For a height of 1.87 meters and a weight of 80.0 kilograms, the BMI is 22.9.'
    >>> calculate_bmi('-80.0', '187.0')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to a_weight parameter must be a non-negative float
    """

    # converting only if conversion is possible, otherwise will be caught by assertions below
    if a_weight.replace('.', '').isdigit() and a_height.replace('.', '').isdigit():
        a_weight = float(a_weight)
        a_height = float(a_height)

    # checking class and values for parameters
    assert isinstance(a_weight, float) and a_weight > 0, "argument passed to a_weight parameter must be a non-negative float"
    assert isinstance(a_height, float) and a_height > 0, "argument passed to a_height parameter must be a non-negative float"

    # converting height from meters to centimeters
    a_height = a_height / 100

    # calculation for bmi of an individual
    bmi = round(a_weight / (a_height ** 2), 2)

    return f"For a height of {a_height} meters and a weight of {a_weight} kilograms, the BMI is {round(bmi, 1)}."

#taking user inputs for body specifications, converting height immediately upon receiving input, in function call
print(calculate_bmi(input("What is your weight in kilograms? "), input("What is your height in centimeters? ")))

doctest.testmod()