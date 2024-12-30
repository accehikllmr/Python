#STRING METHODS
#it is possible to use multiple methods on a string object, all at once, on one line
from symbol import pass_stmt
string = "    Hello World!    "
new_string = string.lower().strip().capitalize()[1:6]
print(new_string)

#STRING FORMATTING
#there are several different ways that a string can be formatted

#--concatenation
#----- adding strings together using addition
a = "Gaston"
print("Hello, my name is " + a + ".")

#--using % (similar to the C programming language), with a variable or a literal
print("Hello, %s is my name." %a)
print("Hello, %s is my name." %'Gaston')
print("Hello, %.1f is my name." %105.789)       #like C, can use rounding by adding .number after %
print("Hello, %5f is my name." %105.789)        #use number immediately after % to specify width of string

#--string format method, using curly braces in string
print("Hello, {} is my name.".format(a))
age = 300
print("Hello, {0:s} is my name and I am {1:20.10f} years old.".format(a, age))     #format as in % approach
print("Hello, {a} is my name and I am {age} years old".format(a = "Gaston", age = 300))

#--f-strings leading f and curly brackets
print(f"Hello, {a} is my name.")
print(f"Hello, {a.upper()} is my name.")                        #can use string methods within the output string
print(f"Hello, {a} is my name and I am {age ** 2} years old.")  #can also perform mathematical operations

#FUNCTIONS
'''
below we see some crucial elements of a function and its docstring, which is documentation explaining what a 
function does, gives instructions for use to the programmer, and even has measures to counteract invalid inputs
'''
#function header contains not only parameter names, but their types, followed by the type of the return value
def is_equal(number_1: int = 0, number_2: int = 0) -> bool:
    """
    #the following line describes what the function does
    Compares whether two integers are of equal value.

    #the preconditions specify what type of input data is expected for the function
    Preconditions: number_1 int
                   number_2 int

    '''
    the following lines are example test cases, they run even if the function is not called in the program
    the chosen test cases cover different scenarios, but none which include invalid inputs as specified in
    the preconditions, since all such cases are handled in the body of the function
    '''
    >>> is_equal(1, 1)      #equal positive integers should return the boolean value True
    True
    >>> is_equal(1, 2)      #different integers should return the boolean value False
    False
    >>> is_equal(-1, -1)    #equal negative integers should return the boolean value True
    True
    >>> is_equal()          #a function call without passing arguments returns True, since the default values are equal
    True
    """
    '''
    this test checks the preconditions specified in the docstring, if it fails (the assertion is false), 
    then the function outputs the associated string and returns an AssertionError, instead of its intended output
    this test is only triggered when the function is called outside of itself, unlike the tests contained within the 
    docstring, above this comment
    '''
    assert type(number_1) == type(number_2) == int, "The values passed to the function must be integers."

    #this line returns a value from the function, it will not print anything since there is no print statement
    return number_1 == number_2

'''
the following lines allow us to see the output of the docstring tests when running the program using the shell
(side note: i have been unable to get this to work using the python console here in pycharm...)
but in windows powershell, we first navigate to the correct file path: C:\...\PycharmProjects\courseNotes\notes
and run the command python filename.py -v (the -v flag stands for verbose and will show the results of the tests)
'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()

#UNIT TESTING
'''
to create unit tests, we create a new type of class specifically for testing the function in question
in this class, we import the function in question so that it can be called, we also import the unittest module
final, we create methods (name for a function inside of a class) which will test the desired cases
i will return to this later, when i learn more about classes
'''