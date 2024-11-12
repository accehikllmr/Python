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

# to avoid index out of range errors, check if given string is in a list prior to or while iterating

'''
passing  mutable data (e.g. List) as an argument to a function, Python does not copy the data (for efficiency), 
so instead pass a copy, not so for immutable data (e.g. string)
'''

# dictionary keys can only be of immutable type

# each collection type has a function that can be used to convert other objects into its type

# looping over a list is the same as looping over a tuple (same syntax)
# with set, no indexing
# with dictionary, looping through the keys (e.g. for key in...) or values or both is possible
# so, possible to iterate through a tuple of tuples (i.e. two variables at a time)

