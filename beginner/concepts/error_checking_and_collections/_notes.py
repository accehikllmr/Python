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

# returns None, since function prints multiple lines based on list size
def loop_iteration(some_list: list) -> None:
    """
    >>> loop_iteration(['a', 'b', 'c', 'd', 'e'])
    5
    4
    3
    2
    1
    >>> loop_iteration(['apple', 'banana', 'carotte'])
    3
    2
    1
    """
    # when iterating a for loop over a list, but not using its elements, can use '_' as temporary variable
    n = len(some_list)
    # iterating over list, but using it to count 5 iterations (real-use scenario unclear)
    for _ in some_list:
        print(n)
        n -= 1

    # HOW TO USE DOCSTRING WHEN LOOPS ITERATIONS DEPEND ON A CONDITION? (while loop)

# LISTS
'''
creating an alias for a list is identical to creating an alias for a tuple, but since lists are mutable, 
modifying one list can affect the challenges (methods act on underlying references, hence affecting all object using them),
thus tracking such changes across all aliases can be difficult
'''
def list_alias(this_list: list) -> bool:
    """
    >>> list_alias([1, 2, 3])
    True
    >>> list_alias(['alabama', 'arkansas', 'ma and pa'])
    True
    """
    that_list = this_list
    # changing the newer list
    that_list[0] = 'zero'
    # checking if both lists were modified, or only one
    return that_list == this_list

# strings in a list can be concatenated using the join method, with a specified delimiter
def join_list(string_list: list, delimiter: str) -> str:
    """
    >>> join_list(['a', 'b', 'c'], ' ')
    'a b c'
    >>> join_list(['a', 'b', 'c'], ' and ')     # any desired string can be inserted between the list values
    'a and b and c'
    """
    return delimiter.join(string_list)

# a string can be separated and stored as values in a list, with a specified delimiter
def split_string(some_string: str, some_delimiter: str) -> list:
    """
    >>> split_string("This is sparta!", ' ')
    ['This', 'is', 'sparta!']
    >>> split_string("This is sparta!", 's')    # any desired string can be used to separate the string into values
    ['Thi', ' i', ' ', 'parta!']
    """
    return some_string.split(some_delimiter)

# repetition operator makes multiple copies of a list and joins them together


# TUPLES
# though tuples can contain different data types, it is bad practice to do so
# tuples can be unpacked such that their different values are assigned to different variables
def unpack_tuple(a_tuple: tuple, coordinate: str) -> int:
    """
    >>> unpack_tuple((1, 2, 3), 'x')
    1
    >>> unpack_tuple((1, 2, 3), 'y')
    2
    >>> unpack_tuple((1, 2, 3), 'z')
    3
    >>> unpack_tuple((1, 2, 3), 'a')
    invalid coordinate
    """
    # unpacking tuple values to three different variables, values are unpacked from left to right
    x, y, z = a_tuple

    # returning different values depending argument passed to coordinate parameter, error controlled by else branch
    if coordinate == 'x':
        return x
    elif coordinate == 'y':
        return y
    elif coordinate == 'z':
        return z
    else:
        print("invalid coordinate")

# for the tuple index method, start and stop positions can be specified
def tuple_index(some_tuple: tuple, a_value: any, start: int, stop: int) -> int:
    """
    >>> tuple_index((1, 2, 1, 2, 3), 1, 0, 4)   # start position is 0, so first 1 found is at position 0
    0
    >>> tuple_index((1, 2, 1, 2, 3), 1, 2, 4)   # start position is 2, so first 1 found is at position 2
    2
    >>> tuple_index((1, 2, 1, 2, 3), 3, 0, 3)   # stop before finding 3, so raises ValueError
    Traceback (most recent call last):
    ...
    ValueError: tuple.index(x): x not in tuple
    """
    # rather than creating an assertion statement to define error, can use built-in error raised by interpreter (see above)

    return some_tuple.index(a_value, start, stop)

# a function can return multiple values, will be returned as a tuple by default
def multiple_returns(a: int, b: int) -> tuple:
    """
    >>> multiple_returns(1, 2)
    (3, 2)
    >>> multiple_returns(5, 7)
    (12, 35)
    """
    return a + b, a * b

# no methods exist to change the length of (size) or values in (references) the tuple (e.g. insert, append, remove, etc.)
def print_dir(data_type: any) -> None:
    """
    >>> print_dir(tuple)    # tuple directory has only two methods, none of which allows changing its size or its references
    count
    index
    >>> print_dir(list)     # list directory has numerous methods, some of which allow changing its size or its references
    append
    clear
    copy
    count
    extend
    index
    insert
    pop
    remove
    reverse
    sort
    """
    # looping through all content of directory
    for method in dir(data_type):
        # condition to ignore all content that isn't a method
        if "__" not in method:
            print(method)

'''
giving different names to the same data (aliasing), hence the id for each variable is identical
since tuples are immutable, neither can be modified and thus affect the challenges
'''
def tuple_alias(young_tuple: tuple) -> bool:
    """
    >>> tuple_alias((1, 2, 3))
    True
    >>> tuple_alias(('a', 'b', 'c'))
    True
    """
    old_tuple = young_tuple
    # verifying that both tuples have identical id values
    return id(old_tuple) == id(young_tuple)

# SETS

# since dictionaries and sets both use curly brackets, to declare an empty consider the following
def empty_set(declaration: any) -> type:
    """
    >>> empty_set(set())    # this declares an empty set
    <class 'set'>
    >>> empty_set({})       # two empty curly brackets declares an empty dictionary, as opposed to a set
    <class 'dict'>
    >>> empty_set(dict())
    <class 'dict'>
    """
    data_structure = declaration
    return type(data_structure)

# DICTIONARIES
'''
to associate and record pairs of data, dictionaries are preferred to nested lists, especially when these pairs consist
of different data types
'''

# the mapping of dictionary keys to their corresponding values is known as a hash function

# to access a value stored in a dictionary, consider the following
def access_value(a_dictionary: dict, a_key: any) -> any:
    """
    >>> access_value({'a': 1, 'b': 2, 'c': 3}, 'b')
    2
    >>> access_value({'a': 1, 'b': 2, 'c': 3}, 'c')
    3
    >>> access_value({'a': 1, 'c': 2, 'c': 3}, 'c')     # for duplicate keys, last mapping overwrites previous ones
    3
    >>> access_value({1: 1, 2: 2, 3: 3}, 3)             # integers can be used as keys
    3
    >>> access_value({[1]: 1, [2]: 2, [3]: 3}, [2])     # lists cannot be used as keys
    Traceback (most recent call last):
    ...
    TypeError: unhashable type: 'list'
    """
    return a_dictionary[a_key]      # syntax for accessing a value from a dictionary, given a key

# values associated with keys can be of different types, and even combined
# can create nested dictionaries

# COLLECTIONS AS PARAMETERS
# can specify parameters as collection type with types in collection, in function declaration
from typing import Dict, List, Set, Tuple

# not sure why this is not working, but at least we can see the syntax
def collection_parameter(the_dict: Dict[str, int], the_list: List[int], the_set: Set[int]) -> any: #, the_tuple: Tuple[int]) -> any:
    """
    >>> collection_parameter({'a': 1, 'b': 2}, [1], {1}) #, (1,))
    {'a': 1, 'b': 2}
    >>> collection_parameter({'a':1}, [1, 2], {1}) #, (1,))
    [1, 2]
    >>> collection_parameter({'a':1}, [1], {1, 2}) #, (1,))
    {1, 2}
    #>>> collection_parameter({'a':1}, [1], {1}, (2,))
    #(2,)
    """
    if the_dict != {'a': 1}:
        return the_dict
    elif the_list != [1]:
        return the_list
    elif the_set != {1}:
        return the_set
    #elif the_tuple != (1,):
    #    return the_tuple

doctest.testmod()