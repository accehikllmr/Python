import doctest

def xor_operator(expression_1: bool, expression_2: bool) -> bool:
    """
    Evaluated the exclusive or operation (XOR) for two boolean expressions.

    Preconditions:  expression_1    bool
                    expression_2    bool

    >>> xor_operator(False, False)
    False
    >>> xor_operator(False, True)
    True
    >>> xor_operator(True, False)
    True
    >>> xor_operator(True, True)
    False
    >>> xor_operator(1, True)
    Traceback (most recent call last):
    ...
    AssertionError: argument with invalid data type passed to expression_1 parameter
    >>> xor_operator(True, 1)
    Traceback (most recent call last):
    ...
    AssertionError: argument with invalid data type passed to expression_2 parameter
    """

    assert type(expression_1) == bool, "argument with invalid data type passed to expression_1 parameter"
    assert type(expression_2) == bool, "argument with invalid data type passed to expression_2 parameter"

    not_both_true = not(expression_1 and expression_2)
    not_both_false = not(not expression_1 and not expression_2)

    return not_both_true and not_both_false

doctest.testmod()

# another duplicate from lab 2