import doctest

# Q1

def while_over_indices(iterable_object: any) -> None:
    """
    Prints values at each index in an iterable object, starting from 0.

    Parameters:
        iterable_object (any): data type through which iteration is possible using indices

    >>> while_over_indices("Hello")
    H
    e
    l
    l
    o
    >>> while_over_indices((123, 45, 1, 25))
    123
    45
    1
    25
    >>> while_over_indices([123, 45, 1, 25])
    123
    45
    1
    25
    """
    # initializing the index variable for the while loop
    position = 0

    # looping until reaching the end of the index range for the iterable object
    while position < len(iterable_object):
        print(iterable_object[position])
        position += 1

# Q2

# assigns list with values in three cells to variable a
a = [1000, 2000, 3000]

# assigns a, the existing list object, to b
print(">>> b = a")
b = a

# hence, a and b have the same id
print(f"The id of variable a is identical to the id of variable b: {id(a) == id(b)}")

# a shallow copy of the list stored in variable a is assigned to variable c
print(">>> c = a.copy()")
c = a.copy()

# hence, a and c do not have the same id
print(f"The id of variable a is identical to the id of variable c: {id(a) == id(c)}")

# these lines change the values stored at different indices of each list stored at b and c, respectively
print(">>> b[0] = 3")
b[0] = 3
c[1] = 5

# since a and b have the same id, they refer to the same data, hence the change to b has also changed a
print(f"b was changed, b = {b} and thus a was changed, a = {a}")

# since a and c have different ids, they refer to different data, hence the change to c has not changed a
print(">>> c[1] = 5")
print(f"c was changed, c = {c} but a was not changed, a = {a}\n")

# Q3

def concatenation_method(a_left: list, item: list) -> tuple:
    """
    >>> concatenation_method([1, 2, 3], [2])
    (True, False)
    >>> concatenation_method([1, 2, 3], ['a'])
    (True, False)
    >>> concatenation_method([1, 2, 3], [(2,)])
    (True, False)
    """
    # need to work on two different list objects since using different methods of concatenation
    a_right = a_left.copy()

    # assigning list objects stored at variables a_left and a_right to new variables, b and c, respectively
    b = a_left
    c = a_right

    '''
    using different methods of concatenation for each list object, though they seem interchangeable the first
    simply adds the item to the existing list object while the second creates an entirely new list object
    '''
    a_left += item
    a_right = a_right + item

    '''
    the list object assigned to a_left was modified, this same list was assigned b, so b was also modified,
    hence their ids are identical
    a new list object was assigned to a_right, so a_right and c no longer have the same list objects assigned to them,
    hence their ids are different
    '''
    return id(b) == id(a_left), id(c) == id(a_right)

# Q4

'''
no matter what argument is passed to parameter a, this value is overwritten by the reassignment of [4, 2, 6]
hence, the function always returns the same value, the list object [4, 2, 6]
'''
def foo(a):
    """
    >>> foo([1, 2, 3])
    [4, 2, 6]
    >>> foo('a')
    [4, 2, 6]
    >>> foo(101)
    [4, 2, 6]
    """
    # reassignment of value assigned to a
    a = [4, 2, 6]
    return a

a = [1, 2, 3]

# value of a is reassigned to the return of the function, which is always the list object: [4, 2, 6]
a = foo(a)
print(f"No matter the argument passed to parameter a, the function always returns: {a}")

doctest.testmod()