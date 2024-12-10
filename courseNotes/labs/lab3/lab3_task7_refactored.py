import doctest

# instead of compelling user to follow a specific inputting format, using function from previous problem to format input
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

def get_first(full_name: str) -> str:
    """
    Extracts first name from full name.

    Parameters:
        full_name (str): person's full name, in this format: last, first

    Returns:
        (str): person's first name

    >>> get_first("Clark, Michel")
    'Michel'
    >>> get_first(", ")
    ''
    """

    # input to function is guaranteed to be a string object, so no need for validation

    # splitting string at comma, to find last name
    full_name = full_name.split(',')

    # returning first name (first element in list) stripped of whitespace, if any
    return full_name[1].strip()

# nested function call, first call returns correctly formatted input
print(get_first(last_first(input("First name: "), input("Last name: "))))

doctest.testmod()