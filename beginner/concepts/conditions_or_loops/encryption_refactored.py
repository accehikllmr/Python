import doctest

def encrypt(message: str, shift: int) -> str:
    """
    Given a shift value, uses the Caesar cipher to encrypt a message.

    Parameters:
        message (str): message to be encrypted
        shift (int): value to determine the left/right movement in the Caesar cipher encryption

    Returns:
        (str): encrypted message

    >>> encrypt("ABCDEFG", 4)
    'EFGHIJK'
    >>> encrypt("SEND 5 PIZZAS", 12)
    'EQZP 5 BULLME'
    >>> encrypt("READY THE TROOPS!!", 20)
    'LYUXS NBY NLIIJM!!'
    >>> encrypt("SUPER SECRET MESSAGE 123", 13)
    'FHCRE FRPERG ZRFFNTR 123'
    >>> encrypt("ABCDEFG", 0)
    'ABCDEFG'
    >>> encrypt("ABCDEFG", 94)
    'QRSTUVW'
    >>> encrypt("", 0)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to message parameter must be an uppercase string
    >>> encrypt("ABCDEFG", -1)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to shift parameter must be a non-negative integer
    """

    # checking preconditions
    # message must be of type string and have only uppercase letters (works because it does not evaluate challenges types of characters)
    assert isinstance(message, str) and message.isupper(), "argument passed to message parameter must be an uppercase string"

    # shift must be a non-negative integer
    assert isinstance(shift, int) and shift >= 0, "argument passed to shift parameter must be a non-negative integer"

    # variable to store message once encrypted
    encrypted_message = ""

    # looping through every character in message
    for char in message:
        # checking if character is an uppercase letter
        if 65 <= ord(char) <= 90:
            # integer corresponding to character order
            char_order = ord(char)
            # shifting to encrypted value for character order
            encrypted_char_order = char_order + shift
            # correcting for shifts which reach beyond end of alphabet
            if encrypted_char_order > 90:
                # see note in older version of script
                encrypted_char_order -= 26 * (((encrypted_char_order - 90) // 26) + 1)
            # converting new order for character into the encrypted character itself
            encrypted_char = chr(encrypted_char_order)
            # concatenating the encrypted character to the encrypted message string
            encrypted_message += encrypted_char
        # for all characters which are not uppercase letters
        else:
            # concatenate the original character (no encryption necessary)
            encrypted_message += char

    return encrypted_message

doctest.testmod()