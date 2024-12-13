import doctest

def function1(value: float) -> None:
    """
    Assigns a value to global variable x.

    Parameters:
         value (float): value used to create global variable x

    # no tests, since the value of x is not returned until return from problematic function
    """
    global x
    x = value + y
    return


def function2(value: float) -> None:
    """
    Assigns a value to global variable y.

    Parameters:
         value (float): value used to create global variable y

    # no tests, since the value of y is not returned until return from problematic function
    """
    global y
    y = value
    return


def problematic_function(x_value: float, y_value: float) -> float:
    """
    A problematic function that has no practical use.

    Parameters:
        x_value (float): a value passed to the function
        y_value (float): a separate value passed to the function

    Returns:
        (float): sum of

    >>> problematic_function(10.0, 5.0)
    20.0
    >>> problematic_function(10, 5.0)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to x_value parameter must be a float object
    >>> problematic_function(10.0, 5)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to y_value parameter must be a float object
    """
    # using isinstance instead of type, latter is bad practice
    assert isinstance(x_value, float), "argument passed to x_value parameter must be a float object"
    assert isinstance(y_value, float), "argument passed to y_value parameter must be a float object"

    # switched the function calls, since need value of y to calculate value of x, these functions actually instantiate these objects
    function2(y_value)
    function1(x_value)

    # these values are global variables, as assigned in other functions (global variables)
    return x + y

doctest.testmod()