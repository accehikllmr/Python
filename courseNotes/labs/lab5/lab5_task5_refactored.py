import doctest

def absolute_value(expression: str) -> float:
    """
    Takes an absolute value expression as a string type and evaluates it, returning a float type.

    Parameters:
        expression (str): expression in the following format '|[sign][digits][period][digits]|'

    Returns:
        (float): absolute value of expression

    >>> absolute_value('|2|')
    2.0
    >>> absolute_value('|-2|')
    2.0
    >>> absolute_value('|2.2|')
    2.2
    >>> absolute_value('|-2.2|')
    2.2
    >>> absolute_value(' |2| ')
    2.0
    >>> absolute_value('| 2 |')
    2.0
    >>> absolute_value(1)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for the expression parameter
    >>> absolute_value('|2*a|')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to expression parameter contains an invalid character
    >>> absolute_value('2|')
    Traceback (most recent call last):
    ...
    AssertionError: the expression must begin and end with a vertical bar |
    >>> absolute_value('||2|')
    Traceback (most recent call last):
    ...
    AssertionError: the expression does not have only two vertical bars |
    >>> absolute_value('|--2|')
    Traceback (most recent call last):
    ...
    AssertionError: the expression contains redundant minus signs -
    >>> absolute_value('|2..2|')
    Traceback (most recent call last):
    ...
    AssertionError: the expression contains too many decimal points .
    >>> absolute_value('|2-2|')
    Traceback (most recent call last):
    ...
    AssertionError: the minus sign does not immediately follow the first vertical bar
    >>> absolute_value('|2.|')
    Traceback (most recent call last):
    ...
    AssertionError: the decimal point is not positioned between two digits
    >>> absolute_value('|-.2|')
    Traceback (most recent call last):
    ...
    AssertionError: the decimal point is not positioned between two digits
    """

    # checking that input data is of string type
    assert isinstance(expression, str), "invalid data type for the expression parameter"

    # clearing all space characters from string, but need reassignment otherwise original string is evaluated below
    expression = expression.replace(' ', '')

    # convert string object into a list object with length equivalent to length of string
    expression = list(expression)

    # valid characters
    valid_symbols = {'|', '-', '.'}

    # iterate through list to find invalid characters
    for char in expression:
        # check if character is either valid symbol or digit
        assert char in valid_symbols or char.isdigit(), "argument passed to expression parameter contains an invalid character"

    # checking that vertical bars begin and end the expression, using indices
    assert expression[0] == expression[-1] == '|', "the expression must begin and end with a vertical bar |"

    # checking that there are exactly two vertical bars in the expression
    assert expression.count('|') == 2, "the expression does not have only two vertical bars |"

    # checking that there is a maximum of one minus sign in the expression
    assert expression.count('-') <= 1, "the expression contains redundant minus signs -"

    # checking that there is a maximum of one decimal point in the expression
    assert expression.count('.') <= 1, "the expression contains too many decimal points ."

    # checking that any minus sign in the expression is positioned directly after the first vertical bar, IndexError avoided by lazy evaluation of booleans
    assert '-' not in expression or expression[1] == '-', "the minus sign does not immediately follow the first vertical bar"

    # checking that any decimal point in the expression is positioned between two digits
    assert '.' not in expression or (expression[expression.index('.') - 1].isdigit() and expression[expression.index('.') + 1].isdigit()), "the decimal point is not positioned between two digits"

    #stripping expression and slice of expression to remove all whitespaces
    return abs(float(''.join(expression[1:-1])))

if __name__ == 'main':
    doctest.testmod()