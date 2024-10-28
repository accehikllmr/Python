def is_both_true(x : bool, y : bool) -> bool:
    '''
    Determines whether the conjunction of two boolean values is true.

    ====== ====== ========
        Inputs     Output
    ------------- --------
      x      y    x and y
    ====== =====  ========
    True   True    True
    True   False   False
    False  True    False
    False  False   False
    ====== ====== ========

     >>> is_both_true(True, True)
     True
     >>> is_both_true(True, False)
     False
     >>> is_both_true(False, True)
     False
     >>> is_both_true(False, False)
     False

    :param bool x: truth value of x
    :param bool y: truth value of y
    :return boolean: truth value of conjunction of x and y

    '''
    return x and y

def is_both_false(x : bool, y : bool) -> bool:
    '''
    Determines whether the conjunction of the negation of two boolean values is true.

    ====== ====== ===============
        Inputs         Output
    ------------- ---------------
    not x  not y   not x and not y
    ====== =====  ===============
    True   True    True
    True   False   False
    False  True    False
    False  False   False
    ====== ====== ===============

    >>> is_both_false(not True, not True)
    True
    >>> is_both_false(not True, not False)
    False
    >>> is_both_false(not False, not False)
    False
    >>> is_both_false(not False, not False)
    False

    :param bool x: truth value of x
    :param bool y: truth value of y
    :return boolean: truth value of conjunction of x and y
    '''
    return not x and not y

# get input
# type 1 for True, leave empty for False, and then press enter
a = bool(input("a = "))
b = bool(input("b = "))
    
# function calls to determine whether a and b are both true or both false
both_true = is_both_true(a, b)
both_false = is_both_false(a, b)

# The result is True iff it is not both True and both False
result = not both_true and not both_false
    
# show the result
print(result)