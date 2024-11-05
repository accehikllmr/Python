import doctest

def reverse_str(a_string: str) -> str:
    """
    Reverses the order of characters in a string.

    >>> reverse_str("''")
    "''"
    >>> reverse_str("abcdefgh")
    'hgfedcba'
    >>> reverse_str("c")
    'c'
    >>> reverse_str("")
    ''
    >>> reverse_str("123")
    '321'
    >>> reverse_str(" a@54! ")
    ' !45@a '
    >>> reverse_str("93hfg2vb3 [12]3fo1]-vckme91[")
    '[19emkcv-]1of3]21[ 3bv2gfh39'
    >>> reverse_str(True)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for argument passed to a_string parameter
    >>> reverse_str(1)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for argument passed to a_string parameter
    """
    # checking preconditions
    # a_string must be of string data type
    assert type(a_string) == str, "invalid data type for argument passed to a_string parameter"

    '''
    no need to loop here, simply take the original string (default from index 0 to -1, inclusive)
    but increment in the opposite direction, so -1 instead of default which is 1
    '''
    return a_string[::-1]

doctest.testmod()