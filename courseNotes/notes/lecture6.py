#BUILT-IN MODULES------------------------------------------------------------------------------

'''
there exist many built-in modules that can be imported into a script
these modules contain data structures (e.g. pre-built functions, pre-defined constants, etc.)
that would otherwise have to be built from scratch (e.g. the math module)
'''

#here is the standard way of importing a module, and using it
import math
print(math.pi)  #prints the value of pi, to 15 decimal places

#when importing a module, you can rename it, and use this new name
import math as m
print(m.pi)

#rather than importing an entire module, you can import a specific data structure
from math import pi
print(pi)

#when importing a specific data structure, you can rename it, and use this new name
from math import pi as delicious_pi
print(delicious_pi)

'''
it is also possible to import all data structures from a module but this is NOT recommended 
since some modules have many data structures and thus importing them all wastes memory
it also makes it more difficult to find from which module a data structure has been imported
imagine having multiple lines with "from (module_name) import * at the beginning of a script
finally, why import data structures that are not needed?
'''
from math import *
print(pi)

#CUSTOM MODULES------------------------------------------------------------------------------

'''
though there exist numerous built-in modules in Python that cover a wide range of functionality,
sometimes it is necessary to create custom modules
rather than existing as a function within a particular script, these modules exist as their own
script, such that the target script is abridged in length and any other script needing the module
can import it and use its data structures
'''

'''
importing a module will execute the script of that module as soon as it is imported, but this is
not usually problematic since modules usually consist of various functions, however, to prevent
execution of code a condition can be added so that execution occurs only if the module in
question is run as the main function
'''

#script of the module, will not print anything unless it is called as the main function

def foo1():
    print('1')

def foo2():
    print('2')

def foo3():
    print('3')

#module not being imported, so the print command executes
if __name__ == "__main__":
    print('a')

#ARGUMENTS------------------------------------------------------------------------------

'''
when calling a function, it is possible to provide positional arguments, such that the
arguments are associated to the function parameters in the order that they are written
'''

def foo4(a, b, c):
    print(f"{a}{b}{c}")

foo4(1,2,3)
foo4(2,1,3)

'''
otherwise, it is also possible to provide keyword arguments, such that the arguments are
associated with the appropriate function parameter, hence the order in which they are
written matters not
'''

foo4(c = 3, b = 1, a = 2)   #outputs the same string as the previous function call
foo4(b = 1, a = 2, c = 3)   #outputs the same string as the previous function call

#keyword and positional arguments can be mixed, but positional arguments cannot follow keyword ones

#foo4(a = 1, 2, 3)          #causes a SyntaxError
foo4(1, 2, c = 2)     #this works just fine
#foo4(1, a = 2, b = 3)      #this might work elsewhere, but PyCharm by default associated position with keyword

#some functions do not accept keyword arguments, this is indicated by a / in the parameters of the docstring

abs(-3)         #no output, but it works
#abs(x = -3)    #causes a TypeError

#to prevent keyword arguments from being passed to a custom function, add a / at the end of the parameters

#seems that Python 3.6 does not support exclusively positional parameter
#def foo5(a, b, c, /):
#    print(f"{a}{b}{c}")

#foo5(1, 2, 5)          #this works
#foo5(a = 1, b = 2, c = 5)      #causes a TypeError