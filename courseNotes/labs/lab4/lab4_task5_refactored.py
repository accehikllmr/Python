import doctest

def xor_operator(expression_1: bool, expression_2: bool) -> bool:
    """
    Evaluated the exclusive or operation (XOR) for two boolean expressions.

    Parameters:
        expression_1 (bool): truth value of an expression
        expression_2 (bool): truth value of a different expression

    Returns:
        (bool): truth value of expressions combined using the exclusive or operator

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

    # change to isinstance
    assert isinstance(expression_1, bool), "argument with invalid data type passed to expression_1 parameter"
    assert isinstance(expression_2, bool), "argument with invalid data type passed to expression_2 parameter"

    # modified boolean expressions, using de Morgan's Law
    not_both_true = not expression_1 or not expression_2
    not_both_false = expression_1 or expression_2

    # could combine above into a single statement, but not necessary
    return not_both_true and not_both_false

doctest.testmod()

# could refactor even more, as was done in duplicate refactoring file, but no need to repeat exercise (mostly involving user inputs)