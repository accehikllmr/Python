print("\nDYNAMIC TYPING")
#although Python is a dynamic typing programming language, it is possible to use type hinting
num: int = 10
print(f"-type hinting as integer, num = {num}")
#since it is only type hinting, the user can still change the data type assigned to a variable
num = "hello"
print(f"-having changed the value of the integer to a string, num = '{num}'")
#type hinting can also be used in the definition of function parameters types and return types
def type_hinting_test(x: int, y: str, z: float) -> str:
    return str(x) + y + str(z)
#again, the user can pass values which do not conform to the parameters type hints, and the function still works
string = type_hinting_test('1', 'a', 'b')
print(f"*return of a function with type hinting for integers, despite having passed string values: '{string}'")
#type hinting for a list parameter is as follows (unclear whether it is possible to hint at data type of list)
def list_function(some_list: list) -> None:
    return None

print("\nFUNCTION RETURNS")
#a function which returns multiples values can be assigned to one or multiple values
def return_values():
    return 1, 2
#in this case, each variable will be assigned a returned value, in the order that it appears to the left of the equal sign
a, b = return_values()
print(f"-these are the returned values of a function, assigned to separate variables: {a}, {b}")
#in this case, the variable will be assigned a tuple containing the returned values, in the order that they are returned
c = return_values()
print(f"-these are those same values, assigned to a single variable: {c}")

print("\nLOCAL VS GLOBAL VARIABLES")
#--variables used within a function are called local variables (deleted from memory once function call has completed)
#-----below, the variable p is local, so trying to use it outside the function causes a NameError
def variables():
    var_1 = 2
    print(f"*this is a local variable, within a function, var_1 = {var_1}")
    return var_1
variables()
print("*error message when attempting to access it in the main function: \"NameError: name 'var_1' is not defined.\"")
#--as such, local variables do not change the values of global variables which go by the same name
def no_change():
    var_2 = 5
    print(f"-value assigned to a local variable of the same name, var_2 = {var_2}")
    return None
var_2 = 1
print(f"-value assigned to a global variable, var_2 = {var_2}")
print(f"-function call attempting to change the value of the global variable, var_2")
no_change()
print(f"-value of global variable after function call: var_2 = {var_2}")
#--global variables can be used within functions
def use_global():
    print(f"*value of global variable inside function, var_3 = '{var_3}'\n"
          f"*function returns variable, var_3")
    return var_3
var_3 = "this is my global variable"
print(f"*value of global variable, var_3 = '{var_3}'")
print(f"*function call attempting to use global variable, var_3")
var_4 = use_global()
print(f"*new global variable assigned value returned from function, var_4 = '{var_4}'")
#--that is, unless we use a local variable with the same name to temporarily overwrite its value
#--in challenges words, the computer looks for the value in the local space and if it is not found, it looks in the global space
def overwrite_global():
    print(f"-cannot check value of the global variable, var_5, since following line overwrites assignment")
    var_5 = 5
    print(f"-value of local variable overwriting global variable, var_5 = {var_5}\n"
          f"-function returns var_5")
    return var_5
var_5 = 1
print(f"-global variable, var_5 = {var_5}\n"
      f"-function call to temporarily overwrite variable, var_5")
var_6 = overwrite_global()
print(f"-global variable, having its value preserved, var_5 = {var_5}, and returned value assigned to variable, var_6 = {var_6}")
#--if we add the global keyword within a function, we can reassign its value within a function, such that it is stored permanently
#--this is not good programming practice and should be avoided as much as possible (is there a legitimate use case for this?)
def global_keyword():
    global var_7
    var_7 = 5
var_7 = 1
print(f"*value assigned to global variable, var_7 = {var_7}\n"
      f"*function call attempting to change value of the global variable, var_7")
global_keyword()
print(f"*value assigned to global variable, var_7 = {var_7}")
#--a global variable can be instantiated within a function, using the global keyword
#--this is also not good programming practice (again, is there ever a use case for this?)
def do_not_do_this():
    global var_8
    var_8 = 1
print(f"-error message when attempting to access global variable which is instantiated by function not yet called:"
      "NameError: name 'var_8' is not defined\n"
      "-function call to instantiate var_8")
do_not_do_this()
print(f"-value assigned to global variable, var_8 = {var_8}")
#--avoid using global variables as much as possible

#FUNCTION SCOPING
#--every variable contained within the __main__ frame is global in scope
#--best practice is to pass global variable as an argument to a function parameter, rather than calling it directly (kind of like magic number)
#--best practice is return a new value for a changed global variable, rather than using the global keyword
#--when a is function is called, temporary memory is created within which everything that happens in a function is stored (local memory)
#--the call stack shows the order in which functions within a program are called
#--a RecursionError occurs when the maximum depth of the call stack has been reached, when it is full (run out of local memory)
#--see slides (which ones?) for more

#OTHER NOTES
#--in function preconditions and postconditions, beyond specifying data types we can specify a range of values
#--rather than using conditional statements to prevent invalid inputs from the user, we use assert statements
#--doctests can fail when there are syntactical issues with the docstring (e.g. incorrect indentation, extra spaces, etc.)