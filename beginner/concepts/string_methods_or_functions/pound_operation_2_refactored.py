import doctest

def pound(expression: str) -> int:
    """
    Return the result of the pound operation that is defined as "x # y" = x^2 - y^2

    Parameters:
        expression (str): string defining the pound expression to be simplified

    Returns:
        (int): result of pound operation computation

    >>> pound("2 # 3")
    -5
    >>> pound("0 # 0")
    0
    >>> pound("6 # 1")
    35
    >>> pound(5)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to expression parameter must be a string object
    >>> pound("6#2f")
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to expression parameter must contain one pound symbol and digits on either side
    >>> pound("6##2")
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to expression parameter must contain one pound symbol and digits on either side
    >>> pound("6#2#3")
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to expression parameter must contain one pound symbol and digits on either side
    """

    # using isinstance instead of type, latter is bad form
    assert isinstance(expression, str), "argument passed to expression parameter must be a string object"

    # removing all whitespaces
    expression = expression.replace(' ', '')

    # splitting using pound symbol
    expression = expression.split('#')

    # checking if strings on either side of pound symbol (obtained from above split) are only composed of digits
    assert expression[0].isdigit() and expression[1].isdigit() and len(expression) == 2, "argument passed to expression parameter must contain one pound symbol and digits on either side"

    # extracting values from list
    x = int(expression[0])
    y = int(expression[-1])

    # return the pound operation
    return x * x - y * y

doctest.testmod()