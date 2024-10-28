import doctest

def formatting(statement: str) -> str:
    '''
    Converts a string of the form "print(int)" to "return int".

    >>> formatting("print(34)")
    'return 34'
    >>> formatting("print(0)")
    'return 0'
    >>> formatting("print(24357987862)")
    'return 24357987862'
    >>> formatting("print(2)")
    'return 2'
    >>> formatting("print(-875)")
    'return -875'
    >>> formatting("  print(75)     ")
    'return 75'
    >>> formatting("print(variable_a)")
    Traceback (most recent call last):
    ...
    AssertionError: too many letters
    >>> formatting("prin(27)")
    Traceback (most recent call last):
    ...
    AssertionError: print statement in the statement is incomplete
    >>> formatting("print27)")
    Traceback (most recent call last):
    ...
    AssertionError: the statement has too many or too few brackets
    >>> formatting("print(27")
    Traceback (most recent call last):
    ...
    AssertionError: the statement has too many or too few brackets
    >>> formatting("print(-27*)")
    Traceback (most recent call last):
    ...
    AssertionError: value within brackets of print statement is not a number
    >>> formatting("print(-2-7)")
    Traceback (most recent call last):
    ...
    AssertionError: value within brackets of the print statement has too many minus signs
    >>> formatting("print((2)")
    Traceback (most recent call last):
    ...
    AssertionError: the statement has too many or too few brackets
    >>> formatting("print(2)print")
    Traceback (most recent call last):
    ...
    AssertionError: too many letters
    '''

    #removing any whitespace in statement, to have consistent indices for brackets
    statement = statement.strip()

    #checking if print is statement string is complete
    assert 'print' in statement, "print statement in the statement is incomplete"

    #checking that there is no more than one print statement
    assert statement.count('p') == 1 and statement.count('r') == 1 and statement.count('i') == 1 and statement.count('n') == 1 and statement.count('t') == 1, "too many letters"

    #checking for too many minus signs
    assert statement.count('-') < 2, "value within brackets of the print statement has too many minus signs"

    #checking for too many brackets
    assert (statement.count('(') == 1) and (statement.count(')') == 1), "the statement has too many or too few brackets"

    #checking first bracket index
    assert statement[5] == '(', "the first bracket is missing from the statement"

    #checking for positioning of right bracket
    assert statement[-1] == ')', "the second bracket is missing from the statement"

    #finding brackets in order to extract number from statement in following lines
    first_bracket = statement.find('(')
    second_bracket = statement.find(')')

    #extracting number from input value and trimming all surrounding whitespace
    number = statement[first_bracket + 1: second_bracket].strip()

    #checking if value between brackets of print statement is indeed a number
    assert number.replace('-', "").isdigit(), "value within brackets of print statement is not a number"

    return f"return {number}"

if __name__ == "__main__":
    doctest.testmod()