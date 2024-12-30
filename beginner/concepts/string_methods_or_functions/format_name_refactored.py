import doctest

def last_first(first: str, last: str) -> str:
    """
    Takes a first and last name of a person, and returns last name followed by first name.

    Parameters:
        first (str): first name of person
        last (str): last name of person

    Returns:
        (str): full name, formatted last, first

    >>> last_first('Michel', 'Clark')
    'Clark, Michel'
    >>> last_first('     Michel     ', '     Clark     ')
    'Clark, Michel'
    >>> last_first('','')
    ', '
    """

    # not checking for class of parameters, since guaranteed to be strings

    return f"{last.strip()}, {first.strip()}"

print(last_first(input("First name: "), input("Last name: ")))

doctest.testmod()