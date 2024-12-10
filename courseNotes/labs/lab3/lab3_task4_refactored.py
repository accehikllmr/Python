import doctest

def valid_phone_number(phone_number: str) -> bool:
    """
    Determines whether a given phone number is of valid length (10 digits) and
    contains only valid characters (digits, spaces, dashes and parentheses).

    Parameters:
        phone_number (str): string representing phone number, contains numbers and possibly symbols

    Returns:
        (bool): whether phone number is valid or not, according to criteria

    >>> valid_phone_number(" 1234567890")
    True
    >>> valid_phone_number(" 1234567890       ")
    True
    >>> valid_phone_number("(123) 456 -0000")
    True
    >>> valid_phone_number("123 - 456 - 7890")
    True
    >>> valid_phone_number("e31235h62i")
    False
    >>> valid_phone_number("12345678901")
    False
    """

    # set containing valid symbols, to check against given phone_number, excluding spaces since will be removed
    valid_characters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '(', ')'}

    # removing whitespace from input
    phone_number = phone_number.replace(' ', '')

    # iterating through phone number to validate each individual character, and length
    for char in phone_number:
        # checking for invalid characters
        if char not in valid_characters:
            return False
        # checking for valid symbol characters, replace with empty string
        elif not char.isdigit():
            # method returns a copy of the string, so needs to be assigned
            phone_number = phone_number.replace(char, '')

    # once through full iteration, check if length of phone_number, without symbols, is indeed 10
    if len(phone_number) != 10:
        return False

    return True

# different output to user based on return of function
if valid_phone_number(input("Please enter your phone number: ")):
    print("You have entered a valid phone number.")
else:
    print("You have entered an invalid phone number.")

doctest.testmod()