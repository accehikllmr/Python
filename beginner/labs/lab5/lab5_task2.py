def function1(value: float) -> None:
    global x
    x = value + y
    return

def function2(value: float) -> None:
    global y
    y = value
    return

def problematic_function(x_value: float, y_value: float) -> float:
    """
    >>> problematic_function(10.0, 5.0)
    20.0
    """
    #added second assertion, in order to also validate value of x
    assert type(x_value) == float, "invalid argument"
    assert type(y_value) == float, "invalid argument"

    #switched the function calls, since need value of y to calculate value of x
    function2(y_value)
    function1(x_value)
    
    # Do not modifiy anything below this line
    return x + y 


