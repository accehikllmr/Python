import doctest

def xor(exp_1: str, exp_2: str) -> bool:
    """
    Compute the truth value of the exclusive or operation, given the truth value of the disjuncts.

    Parameters:
        exp_1 (str): string representing truth value of first disjunct
        exp_2 (str): string representing truth value of second disjunct

    Returns:
        (bool): truth value of exclusive or operation on given boolean value

    >>> xor('TRUE', 'true')
    False
    >>> xor('t', 'T')
    False
    >>> xor('1', 'TRUE')
    False
    >>> xor('true', '1')
    False
    >>> xor('FALSE', 'false')
    False
    >>> xor('f', 'F')
    False
    >>> xor('0', 'FALSE')
    False
    >>> xor('false', '0')
    False
    >>> xor('TRUE', 'false')
    True
    >>> xor('FALSE', 'true')
    True
    >>> xor('t', 'F')
    True
    >>> xor('f', 'T')
    True
    >>> xor('1', 'FALSE')
    True
    >>> xor('0', 'TRUE')
    True
    >>> xor('true', '0')
    True
    >>> xor('false', '1')
    True
    >>> xor('faux', 'T')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to exp_1 parameter cannot be interpreted as a boolean value
    >>> xor('F', 'vraie')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to exp_2 parameter cannot be interpreted as a boolean value
    """

    # instantiating sets to contain different possible representations of truth values
    is_true = {'true', 't', '1'}
    is_false = {'false', 'f', '0'}

    # using method now, to prevent more typing later (no problem with digits, since all in form of string)
    exp_1 = exp_1.lower()
    exp_2 = exp_2.lower()

    # nested conditionals rather than four separate cases (less typing?), also longer than original since not using bool conversion
    if exp_1 in is_true:
        exp_1 = True
        if exp_2 in is_true:
            exp_2 = True
        elif exp_2 in is_false:
            exp_2 = False
    elif exp_1 in is_false:
        exp_1 = False
        if exp_2 in is_true:
            exp_2 = True
        elif exp_2 in is_false:
            exp_2 = False

    # checking if both string have been successfully converted to boolean value (i.e. whether inputs were valid)
    assert isinstance(exp_1, bool), "argument passed to exp_1 parameter cannot be interpreted as a boolean value"
    assert isinstance(exp_2, bool), "argument passed to exp_2 parameter cannot be interpreted as a boolean value"

    # either both true or not one of them true (converted second disjunct using de Morgan's laws)
    return not(exp_1 and exp_2) and (exp_1 or exp_2)

# function call and taking inputs, as strings in order to check validity within function
print(xor(input(f"Truth value of expression 1: "), input(f"Truth value of expression 2: ")))

doctest.testmod()