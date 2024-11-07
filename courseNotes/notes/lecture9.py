import doctest

# CONDITIONAL STATEMENTS
# can be used to catch errors (in what circumstances use these instead of assertions?)
def add_nums(num1: int, num2: int) -> any:
    """
    >>> add_nums(1, 2)
    3
    >>> add_nums('one', 2)
    'invalid argument passed to num1 or num2 parameter'
    """
    # checking data types for argument parameters, using this instead of assertion statement
    if type(num1) != int or type(num2) != int:
        return "invalid argument passed to num1 or num2 parameter"

    return num1 + num2

# flowcharts can be used to help organize code structure (is there a standard approach to doing this?)

# LOOPS
# a for loop can always be replaced by a while loop, but the converse is not true

# can use while loops for error checking (e.g. take input until a certain condition is met)
def sub_nums() -> int:
    """
    CANNOT USE TESTS IN DOCSTRINGS IF FUNCTION TAKES NO PARAMETERS
    """
    # default values to initiate loop condition
    num1 = 0
    num2 = 0

    # continue looping until at least one variable is not assigned default value
    while num1 == 0 and num2 == 0:
        num1 = int(input("num1 = "))
        num2 = int(input("num2 = "))

    return num1 - num2

# when iterating a for loop over a list, but not using its elements, can use '_' as temporary variable
a_list = ['a', 'b', 'c', 'd', 'e']
n = len(a_list)
# iterating over list, but using it to count 5 iterations (real-use scenario unclear)
for _ in a_list:
    print(n)
    n -= 1

# LISTS
# repetition operator makes multiple copies of a list and joins them together
# pop removes an item from the end of the list

# DICTIONARIES
# values associated with keys can be of different types, combined
# can create nested dictionaries

# REVIEW LECTURE NOTES, INCLUDING NOTEBOOOKS
# PERHAPS I SHOULD LOOK AT THE NOTES IN ADVANCE, TO BETTER KNOW WHEN I SHOULD BE LISTENING, OR NOT

doctest.testmod()