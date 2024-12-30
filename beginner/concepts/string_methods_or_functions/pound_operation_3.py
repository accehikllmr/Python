import doctest

def pound(expression: str) -> int:
    """
    Performs the pound operation on two numbers (x and y), x # y = x * x - y * y

    >>> pound("      2 # 3")
    -5
    >>> pound("2 # 3      ")
    -5
    >>> pound("2   #     3")
    -5
    >>> pound("2#3")
    -5
    >>> pound("2 ##### 3")
    Traceback (most recent call last):
    ...
    AssertionError: argument with too many # characters passed to expression parameter
    >>> pound("2 # 3 # 4 # 5")
    Traceback (most recent call last):
    ...
    AssertionError: argument with too many # characters passed to expression parameter
    >>> pound(" # 3")
    Traceback (most recent call last):
    ...
    AssertionError: argument with no value before pound operator passed to expression parameter
    >>> pound("2.5 # 3")
    Traceback (most recent call last):
    ...
    AssertionError: argument with possible float data type passed to expression parameter
    """

    assert expression.count('#') == 1, "argument with too many # characters passed to expression parameter"
    assert expression.strip()[0] != '#', "argument with no value before pound operator passed to expression parameter"
    assert expression.count('.') == 0, "argument with possible float data type passed to expression parameter"

    #locating the pound operator within the string
    pound_index = expression.find('#')

    #extracting the numbers from the expression input by the user
    x = int(expression[:pound_index].strip())
    y = int(expression[pound_index + 1:].strip())

    #return the result of the pound operation
    return x * x - y * y

doctest.testmod()