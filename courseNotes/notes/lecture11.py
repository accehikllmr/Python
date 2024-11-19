import doctest

# possible to concatenate and slice lists and tuples, just like strings

# rather than using .copy(), used to use [:] (slicing) or [] + new_list (concatenation)

# '==' checks if the data in two objects are equal, whereas 'is' checks if two objects are the same (like id() function)

# *args and **kwargs are not positional arguments, hence they are not required; they should also be placed after positional arguments

# classes are blueprints for potential objects; objects created from this class are related but not interdependent

# use camelCase to name classes

'''
when using the sort method on a list object,
can pass reverse=True as an argument
can pass key to sort according to a desired criteria (e.g. string length, uppercase, etc.)
'''
def sort_by_len(string):
    char_num = len(string)
    return char_num

def sort_by_upper(string):
    return string.upper()

phrase = "I can't believe what I've just seen!"
phrase = phrase.split(' ')
phrase.sort(key=sort_by_len)
print(phrase)
phrase.sort(key=sort_by_upper)
print(phrase)


doctest.testmod()