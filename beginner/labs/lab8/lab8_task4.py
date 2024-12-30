################################### TASK 4 ###################################
### Starting code ###

import doctest

def encrypt(message: str, shift: int) -> str:
    """
    Given a shift value, uses the Caesar cipher to encrypt a message.

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
    assert type(message) == str and message.isupper(), "argument passed to message parameter must be an uppercase string"

    # shift must be a non-negative integer
    assert type(shift) == int and shift >= 0, "argument passed to shift parameter must be a non-negative integer"

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
                '''
                subtracts 90 from shifted orders larger than 90, which shows by how much 90 has been surpassed 
                take this number and floor divide by 26, size of alphabet, to see how many times alphabet has been surpassed
                add 1 to this value, otherwise values less than 25 would give 0
                this value is multiplied by 26
                to see how many times we must move back by 26 to return within the range of the uppercase alphabet
                '''
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