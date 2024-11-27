import copy

# NESTED DATA TYPES

# can be reformatted to improve readability, like a dictionary with a dictionary with lists and tuples
some_dict = {
    "a_key": {
        'a': [1, 2, 3],
        'b': [2, 4, 6],
        'c': [3, 6, 9]
    },
    "another_key": {
        'f': (1, 2, 3),
        'g': (2, 3, 5),
        'h': (7, 11, 77)
    }
}

'''
accessing an element in a nested dictionary since this dictionary has strings as keys, 
use indexing with the strings but for the nested list, use index as usual
'''
print(f"\nthe element from the dictionary at keys a_key and a, at index 0, is: {some_dict['a_key']['a'][0]}\n")

# when copying nested data types, it is important to distinguish between shallow and deep copies
# recall that with non-nested lists...
a = [1, 2, 3]
# creating a shallow copy of a list and assigning it to another variable...
b = a.copy()
# means that there are now two separate lists, referring to different data...
b[0] = 0
# which means that changing the copy will not change the original list...
print(f"using shallow copy of non-nested list \t\ta = {a}\t\t\t\t\t\tlist b = {b}")

# with nested lists, it is different...
a = [[1, 2], [2, 3], [3, 4]]
# creating a shallow copy of alist and assigning it to another variable...
b = a.copy()
# means that the outer structure of the list has been copied, but both are referring to the same data...
b[0][0] = 0
# which means that changing the copy will change the original list
print(f"using shallow copy of nested list \t\t\ta = {a}\t\tlist b = {b}")

# this issue can be avoided using a deep copy
a = [[1, 2], [2, 3], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 0
print(f"using deep copy of nested list \t\t\t\ta = {a}\t\tlist b = {b}\n")

# SORTING STRINGS

'''
when using the sort method on a list object, can pass reverse=True as an argument
can pass key to sort according to a desired criteria (e.g. string length, uppercase, etc.)
'''
def sort_by_len(string):
    char_num = len(string)
    return char_num

def sort_by_upper(string):
    return string.upper()

# string to be sorted
phrase = "I can't believe what I've just seen!"

# converting to list so that it can be sorted
phrase = phrase.split(' ')

# sorting according to length of strings
phrase.sort(key=sort_by_len)
print(f"phrase sorted by length of substrings: \t\t\t\t{phrase}")

# sorting according to uppercase characters
phrase.sort(key=sort_by_upper)
print(f"string sorted by uppercase leading characters: \t\t{phrase}")

# MORE ABOUT COPYING

# rather than using .copy(), used to use [:] (slicing) or [] + new_list (concatenation)
a = [1, 2, 3]
b = a.copy()
c = a[:]
d = [] + a
print(f"\nlists: {a}, {b}, {c}, {d}")
print(f"ids of above lists are all different: {id(a)}, {id(b)}, {id(c)}, {id(d)}")

# '==' checks if the data in two objects are equal, whereas 'is' checks if two objects are the same (like id() function)
print(f"\nbut instead of using id to check, we can use 'is': a = {a} is b = {b} = {a is b}")