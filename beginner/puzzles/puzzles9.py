import doctest

# Q1 - LISTS

'''
the index method finds the first appearance of a value in a list and returns its position;
since a list is unordered, if the same value appears multiple times, only the first position is returned; 
the list object is not altered and its id (memory address) is unchanged;
'''
def list_index(lst: list, value: int) -> int:
    """
    >>> list_index([1, 2, 3, 1], 1)     #since the value 1 appears twice in the list, its first position is returned
    0
    """
    return lst.index(value)

'''
the copy method creates a duplicate of a list object, in this case known as a 'shallow copy', and returns it;
as such, the values in each list have the exact same ids; the original list object is not altered;
its id (memory address) is unchanged, but the copied list object has a new id;
'''
def copy_list(lst: list) -> list:
    """
    >>> copy_list([1, 2, 3, 1])
    [1, 2, 3, 1]
    """
    return lst.copy()

def value_id(lst: list) -> bool:
    """
    >>> value_id([1, 2, 3, 1])
    True
    """
    # making shallow copy of list object
    copy = lst.copy()

    # checking if all values have same id
    for i in range(len(lst)):
        # this condition will never be true, since copied list values have same id
        if id(lst[i]) != id(copy[i]):
            return False
    return True

'''
the pop method extracts a value from a specified index and returns that value;
the original list object is not altered and its id (memory address) is unchanged;
'''
def pop_list(lst: list, index: int) -> any:    # using any, since allows returning any data type
    """
    >>> pop_list([1, 2, 3, 1], 2)       # extracting the value from position 2
    3
    """
    return lst.pop(index)

'''
the extend method adds a given number of values to the end of a list and returns nothing;
this contrasts with the append method, which only adds one value to a list;
the original list object is altered, but its id (memory address) is unchanged;
'''
def extend_list(lst: list, values: list) -> list:
    """
    >>> extend_list([1, 2, 3, 1], [1, 2])
    [1, 2, 3, 1, 1, 2]

    """
    lst.extend(values)      # this method returns None, so it must be called prior to the return command
    return lst

'''
the sort method arranges the values in a list in ascending order and returns nothing;
the original list object is altered, but its id (memory address) is unchanged
'''

# Q2 - SETS

'''
the add method adds a single given element to a set, assuming that it is not already present;
the original set object is altered, but its id (memory address) is unchanged;
the method returns nothing;
'''
def add_element(a_set: set, element: any) -> set:
    """
    >>> add_element({1, 2, 3}, 4)       # element not already in set, so added to set
    {1, 2, 3, 4}
    >>> add_element({1, 2, 3}, 1)       # element already in set, so not added in set
    {1, 2, 3}
    """
    a_set.add(element)      # return type None, so using method on set prior to returning it
    return a_set

'''
the discard method removes a single given element from a set, assuming that it is part of the set;
the original set object is altered, but its id (memory address) is unchanged;
the method returns nothing;
'''
def discard_element(a_set: set, element: any) -> [set]:
    """
    >>> discard_element({1, 2, 3}, 3)       # element in set, so removed from it
    {1, 2}
    >>> discard_element({1, 2, 3}, 4)       # element not in set, so nothing done to set
    {1, 2, 3}
    """
    a_set.discard(element)      # return type None, so using method on set prior to returning it
    return a_set

'''
the is subset method compares two sets to determine if the first is a subset of the second;
neither set is altered and their ids (memory addresses) are unchanged;
this method returns a boolean value;
'''
def is_subset(a_set: set, b_set: set) -> bool:
    """
    >>> is_subset({1, 2, 3}, {1, 2})    # first set does not contain all elements in second set
    False
    >>> is_subset({1, 2}, {1, 2, 3})    # second set contains all elements in first set
    True
    """
    return a_set.issubset(b_set)

'''
the copy method creates a duplicate of a set object, in this case known as a 'shallow copy', and returns it;
the original set object is not altered and its id (memory address) is unchanged, but the copied set object has a new id;
since the set elements cannot be indexed, I could not check whether their ids are identical (as they were with lists);
'''
def copy_set(a_set: set) -> set:
    """
    >>> copy_set({1, 2, 3})
    {1, 2, 3}
    """
    return a_set.copy()

# Q3 - DICTIONARIES

'''
the get method finds the value associated to a given key in a dictionary and returns that value;
the dictionary object is not altered and its id (memory address) is unchanged;
'''
def get_value(a_dict: dict, a_key: any) -> any:
    """
     >>> get_value({'a': 1, 'b': 2, 'c': 3}, 'c')
     3
    """
    return a_dict.get(a_key)

'''
the update method modifies one or many key value pairs in a dictionary object and returns nothing;
the dictionary object is not altered and its id (memory address) is unchanged;
'''
def update_pair(a_dict: dict, a_key: any, a_value: any) -> dict:
    """
    >>> update_pair({'a': 1, 'b': 2, 'c': 3}, 'a', 4)
    {'a': 4, 'b': 2, 'c': 3}
    >>> update_pair({'a': 1, 'b': 2, 'c': 3}, 'a', 'bob')
    {'a': 'bob', 'b': 2, 'c': 3}
    """
    a_dict.update({a_key: a_value})     # returns None
    return a_dict

'''
the copy method creates a duplicate of a dictionary object, in this case known as a 'shallow copy', and returns it;
as such, the values in each dictionary have the exact same ids;
the original dictionary object is not altered and its id (memory address) is unchanged, but the copied dictionary object has a new id;
'''
def copy_dict(a_dict: dict) -> dict:
    """
    copy_dict({'a': 1, 'b': 2, 'c': 3}
    {'a': 1, 'b': 2, 'c': 3}
    """
    return dict.copy()

doctest.testmod()