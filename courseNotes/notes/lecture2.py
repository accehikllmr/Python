#strings:       ordered____ immutable__ sequence____ of__ characters______ using ""
#list:          ordered____ mutable____ sequence____ of__ objects_________ using []
#tuple:         ordered____ immutable__ sequence____ of__ objects_________ using ()
#dictionaries:  unordered__ mutable____ pairs_______ of__ (key:value)_____ using {}
#sets:          unordered__ mutable____ collection__ of__ unique_objects__ using {}

#string objects are immutable
stringExample = "helloworld"
#stringExample[0] = "H"         #this will throw a TypeError, since a string object does not support item assignment
                                #more generally, string objects cannot be modified

#list objects are mutable
listExample = [4, 1, 9]
listExample[0] = 44             #this modifies the element at index 0 in the list
print(listExample)              #this prints the list with the updated value for the element at position 0
                                #[44, 1, 4]
                                #list objects can be modified

#tuple objects are immutable
tupleExample = (4, 1, 9)
#tupleExample[0] = 44           #this will throw a TypeError, since a tuple object does not support item assignment
                                #more generally, tuple objects cannot be modified

#dictionary objects are mutable
dictExample = {"one": 1, "two": 2, "three": 3}
dictExample["two"] = 22         #this modifies the value for the key "two" in the dictionary
print(dictExample)              #this prints the dictionary with the updated value for the key "two"
                                #{"one": 1, "two": 2, "three": 3}
                                #dictionary objects can be modified

#set objects are mutable
setExample = {4, 1, 9}
#setExample[0] = 44             #this will throw a Type Error, since a set object does not support item assignment
setExample.clear()              #however, set objects are mutable, so we can clear its contents
print(setExample)               #this prints the set with the updated values (it is empty)
                                #set objects are mutable

#JUST BECAUSE TWO DATA TYPES ARE MUTABLE, IT DOES NOT MEAN THAT THEY CAN BE MODIFIED IN THE EXACT SAME WAYS


#Python uses dynamic typing - you can reassign the data type of the variable (not efficient for the interpreter)
x = "helloworld"
print(x)            #this prints the value of x, which is a string data type
x = 10
print(x)            #this prints the value of x, which is an int data type

#___as opposed to C, where initializing variables requires declaring its type (e.g. int x = 4)
#___advantages:
#______more freedom
#___disadvantages:
#______more difficult to debug
#______prone to runtime and semantic errors
#______slower code execution
#___if possible, avoid changing the data type of the variable

#rules for valid variable names
#___avoid using the following characters: 'l', 'O', 'I' for single character variable names (i.e. for loop iteration)
#___best practice (PEP8* - https://www.peps.python.org/pep-0008/) is having names in lowercase

#mathematical operator shortcuts
#___place the operator symbol (eg. +, -, *, %, etc.) prior to the equal symbol (a = a % b -> a %= b)