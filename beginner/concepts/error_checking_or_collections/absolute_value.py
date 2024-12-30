import doctest

def absolute_value(expression: str) -> float:

    """
    Takes an absolute value expression as a string type and evaluates it, returning a float type.

    Preconditions:      expression  str = '|[sign][digits][period][digits]|'

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
    AssertionError: the expression contains invalid symbols or characters
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
    #checking that input data is of string type
    assert type(expression) == str, "invalid data type for the expression parameter"

    #checking that all non-symbol characters in the expression are digits, by removing all valid symbols and checking if remainder is only digits
    assert expression.replace('|', "").replace('.', "").replace('-',"").replace(' ', "").isdigit()\
        , "the expression contains invalid symbols or characters"

    #checking that vertical bars begin and end the expression, using indices
    assert expression.strip()[0] == expression.strip()[-1] == '|', "the expression must begin and end with a vertical bar |"

    #checking that there are exactly two vertical bars in the expression
    assert expression.count('|') == 2, "the expression does not have only two vertical bars |"

    #checking that there is a maximum of one minus sign in the expression
    assert expression.count('-') <= 1, "the expression contains redundant minus signs -"

    #checking that there is a maximum of one decimal point in the expression
    assert expression.count('.') <= 1, "the expression contains too many decimal points ."

    '''
    checking that any minus sign in the expression is positioned directly after the first vertical bar
    split expression string using minus sign as delimiter, which creates list, where first element (index = 0) should ONLY have vertical bar
    otherwise, minus is somewhere else in the expression (no more than a single minus sign since previous assertions have ruled that out)
    if there is no minus sign in the expression, the first element of the split is equivalent to the original expression
    stripping to rid of white space which changes desired indices
    '''
    assert expression.split('-')[0].strip() == '|' or expression.split('-')[0] == expression, "the minus sign does not immediately follow the first vertical bar"

    '''
    checking that any decimal point in the expression is positioned between two digits
    split expression using decimal point as delimiter, which creates list, where last element (index = -1) CANNOT be vertical bar, 
    otherwise it is preceded by decimal point, AND first element of list must have a digit as its last character, otherwise decimal point is adjacent to a vertical bar
    or a minus sign, which is not a valid mathematical expression (no more than a single decimal point since previous assertions have ruled that out)
    if there is no decimal point in the expression, the first element of the split is equivalent to the original expression
    stripping to rid of white space which changes desired indices
    '''
    assert (expression.split('.')[-1].strip() != '|' and expression.split('.')[0][-1].strip().isdigit()) or expression.split('.')[0] == expression\
        , "the decimal point is not positioned between two digits"

    #stripping expression and slice of expression to remove all whitespaces
    return abs(float(expression.strip()[1:-1]))

if __name__ == 'main':
    doctest.testmod()