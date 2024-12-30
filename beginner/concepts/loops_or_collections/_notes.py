import doctest

# UNARY TUPLES
'''
defining a tuple with a single value requires a comma following the value
otherwise, interpreter interprets assignment as a value of its own type
'''
def tuple_or_no(value: any) -> type:
    """
    >>> tuple_or_no((1,))
    <class 'tuple'>
    >>> tuple_or_no((1))
    <class 'int'>
    >>> tuple_or_no(('a', ))
    <class 'tuple'>
    >>> tuple_or_no(('a'))
    <class 'str'>
    """
    return type(value)

# UNDEFINED NUMBER OF ARGUMENTS
'''
it is possible to create a function with accepts an undefined number of arguments
use * before parameter name, interpreter expects a tuple object
"args" is the standard naming convention for such a parameter
'''
def args_parameter(*args) -> tuple:
    """
    >>> args_parameter(2,)
    (2,)
    >>> args_parameter(2, 3)
    (2, 3)
    >>> args_parameter(2, 3, 4)
    (2, 3, 4)
    """
    return args

'''
to pass the arguments with keywords, which will create a dictionary object,
use ** before parameter name, interpreter expects a tuple object
"kwargs" is the standard naming convention for such a parameter
'''
def kwargs_parameter(**kwargs) -> dict:
    """
    >>> kwargs_parameter(a = 1)
    {'a': 1}
    >>> kwargs_parameter(a = 1, b = 2)
    {'a': 1, 'b': 2}
    >>> kwargs_parameter(a = 1, b = 2, c = 3)
    {'a': 1, 'b': 2, 'c': 3}
    """
    return kwargs

# CONVERSION BETWEEN COLLECTION TYPES
# some objects can be converted into tuple objects, using the tuple() function
def to_tuple(to_convert: any) -> tuple:
    """
    >>> to_tuple([1, 2, 3])
    (1, 2, 3)
    >>> to_tuple({1, 2, 3})
    (1, 2, 3)
    >>> to_tuple({'a': 1, 'b': 2, 'c': 3})  # keys are in tuple, values are lost
    ('a', 'b', 'c')
    >>> to_tuple("bob")    #strings are separated, character by character
    ('b', 'o', 'b')
    """
    return tuple(to_convert)

# some objects can be converted into list objects, using the list() function
def to_list(to_convert: any) -> list:
    """
    >>> to_list((1, 2, 3))
    [1, 2, 3]
    >>> to_list({1, 2, 3})
    [1, 2, 3]
    >>> to_list({'a': 1, 'b': 2, 'c': 3})
    ['a', 'b', 'c']
    >>> to_list("bob")
    ['b', 'o', 'b']
    """
    return list(to_convert)

# some objects can be converted into set objects, using the set() function
def to_set(to_convert: any) -> set:
    """
    >>> to_set((1, 2, 3))
    {1, 2, 3}
    >>> to_set([1, 2, 3])
    {1, 2, 3}
    >>> to_set({'a': 1, 'b': 2, 'c': 3})    # upon conversion, characters are organized in random order, so sometimes this test fails
    {'a', 'b', 'c'}
    >>> to_set("bob")   # random order for characters, so sometimes fails
    {'b', 'o'}
    >>> to_set({1: 'a', 2: 'b', 3: 'c'})    # since keys are integers, order is always ascending, not random
    {1, 2, 3}
    """
    return set(to_convert)

# ITERATION OVER COLLECTION OBJECT ELEMENTS
# for some objects, it is possible to iterate over their elements (hence, conversions between these types is possible)
def iterate_over(to_iterate: any) -> None:
    """
    >>> iterate_over("bob")
    b
    o
    b
    >>> iterate_over((1, 2, 3))
    1
    2
    3
    >>> iterate_over([1, 2, 3])
    1
    2
    3
    >>> iterate_over({1, 2, 3})     # follows the expected order, every single time
    1
    2
    3
    >>> iterate_over({'1', '2', '3'})   # characters, so order is random and some tests will fail
    1
    2
    3
    """
    for i in to_iterate:
        print(i)

# it is possible to iterate over dictionary objects, but their key value pairs make it slightly more complicated
def dicterate(some_dict: dict, over_what: str = "") -> None:
    """
    >>> dicterate({'a': 1, 'b': 2, 'c': 3})
    a
    b
    c
    >>> dicterate({'a': 1, 'b': 2, 'c': 3}, "keys")
    a
    b
    c
    >>> dicterate({'a': 1, 'b': 2, 'c': 3}, "values")
    1
    2
    3
    >>> dicterate({'a': 1, 'b': 2, 'c': 3}, "items")
    ('a', 1)
    ('b', 2)
    ('c', 3)
    >>> dicterate({'a': 1, 'b': 2, 'c': 3}, "key, value")
    a: 1
    b: 2
    c: 3
    """
    if over_what == "":
        for key in some_dict:   # by default, dictionary iterates over keys
            print(key)
    elif over_what == "keys":
        for key in some_dict.keys():
            print(key)
    elif over_what == "values":
        for value in some_dict.values():
            print(value)
    elif over_what == "items":
        for item in some_dict.items():  # each item in dictionary is a key value pair tuple
            print(item)
    elif over_what == "key, value":
        for key, value in some_dict.items():    # iterates through keys and values, at the same time (nested loop?)
            print(f"{key}: {value}")

# ITERATING OVER COLLECTION OBJECT INDICES
# beyond iterating through iterable object elements, for some objects, it is possible to loop through indices
def index_looping(some_collection: any) -> None:
    """
    >>> index_looping("123")
    1
    2
    3
    >>> index_looping((1, 2, 3))
    1
    2
    3
    >>> index_looping([1, 2, 3])
    1
    2
    3
    >>> index_looping({1, 2, 3})
    Traceback (most recent call last):
    ...
    TypeError: 'set' object does not support indexing
    """
    for i in range(len(some_collection)):
        print(some_collection[i])

# LIST COMPREHENSION
# Python offers a concise way of creating a list of elements, known as list comprehension
def list_comprehension(a_collection: any) -> list:
    """
    >>> list_comprehension(range(5))
    [0, 2, 4, 6, 8]
    >>> list_comprehension("12345")
    ['11', '22', '33', '44', '55']
    >>> list_comprehension((1, 2, 3, 4, 5))
    [2, 4, 6, 8, 10]
    """
    return [i + i for i in a_collection]    # iterates through collection and adds i + i as an element in the list

# PASSING COLLECTIONS AS ARGUMENTS
'''
passing a collection data type as an argument, the address itself is passed rather than the object
otherwise, in some cases it would be necessary to copy very large quantities of data, which is inefficient
as such, mutable types (lists, sets and dictionaries) modified within the function will be modified globally
'''
s = {1}
l = [1]
d = {'a': 1}

def modify_mutable() -> None:
    s.add(2)
    l.append(2)
    d['b'] = 2

print(f"before function call:\t{s}\t\t{l}\t\t{d}")  # all error_checking_or_collections before function call
modify_mutable()
print(f"after function call:\t{s}\t{l}\t{d}")  # all error_checking_or_collections, being mutable objects, are modified following the function call

# PYTHON
'''
challenges languages require than elements in a collection are of the same data type, 
Python does not but it is good practice to avoid mixing data types in a collection
'''

# ASSIGNING VS COPYING
'''
assigning an existing object to another variable simply gives that object a second way of referring to it
there is one object and either name can be used to access it, use it and modify its values
copying an existing object creates a new object
there are two objects and either name accesses different objects
'''

doctest.testmod()