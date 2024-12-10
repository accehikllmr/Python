import doctest

def compute_expression(exp: str) -> int:
    """
    Computes the result of the expression, the difference of the first number squared
    and the second number squared (pound operation).

    Parameters:
         exp (str): expression containing digits to be squared separated by the pound symbol

    Returns:
        (int): difference of first number squared and the second number squared

    >>> compute_expression('4 # 3')
    7
    >>> compute_expression('3#1')
    8
    >>> compute_expression('0 # 0')
    0
    >>> compute_expression('3 # 2.0')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to exp parameter must contain only digits and the pound symbol
    >>> compute_expression('3 ## 2')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to exp parameter must contain exactly 1 pound symbol
    >>> compute_expression('# 3 2')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to exp parameter must neither begin nor end with pound symbol
    """

    # replace all empty spaces, not an invalid character, with nothing, to not fail upcoming assertion
    exp = exp.replace(' ', '')

    # checking that expression string only contains hash symbol and digits, guaranteed to be string however
    for char in exp:
        assert char.isdigit() or char == '#', "argument passed to exp parameter must contain only digits and the pound symbol"

    # checking that there is a single pound symbol in the expression
    assert exp.count('#') == 1, "argument passed to exp parameter must contain exactly 1 pound symbol"

    # checking that pound symbol is neither at the beginning nor at the end of the string
    assert exp[0] != '#' and exp[-1] != '#', "argument passed to exp parameter must neither begin nor end with pound symbol"

    # splitting string using pound index
    pound_index = exp.find('#')
    x = int(exp[: pound_index])
    y = int(exp[pound_index + 1 :])

    return x ** 2 - y ** 2

# taking user input, again not within function since complicated writing doctests
expression = input("Please provide an expression in the format of x # y: ")

# printing return of function
print(compute_expression(expression))

doctest.testmod()