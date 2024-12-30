#__identical__ data types can be compared using __all___ comparison operators
#__different__ data types can be compared using __some__ comparison operators

#the following comparisons are possible
print(2 < 2.2)
print('2' == 2)

#the following comparisons are not possible
#print('abc' < 2)

#in general, strings data types cannot be compares with integer or float data types using the greater than (>)
#or lesser than (<) operators

#beyond strings, integers and floats, it is also possible to use these operators on sets, lists and tuples
#the truth values of these comparisons can be anticipated based on knowledge from EECS 1019 - Discrete Math
print((2,3) == (3,2))   #__tuples__ are __ordered______, so this comparison is __False
print({2,3} == {3,2})   #__sets____ are __not ordered__, so this comparison is __True
print([2,3] == [3,2])   #__list____ are __ordered______, so this comparison is __False

#perhaps these operators can also be used on dictionaries...

#the precedence of logical operators is as follows: not, and, or
#brackets can be used to remove ambiguity from a boolean expression

#in order to write text over multiple lines, use triple quotes '''
#to add quotation marks within a string, use escape characters
#___ \" for a double quote
#___ \' for a single quote
#___ \n for a new line
#___ \t for a tab
#___ \\ for a backslash
#to output these escape characters as part of a string, we can include an r or R prior to the string

#the lexicographical order of characters is as follows
#___empty string
#___space
#___digits
#___uppercase
#___underscore
#___lowercase

#when slicing a string, a second colon can be added to specify the step
#[start:end:step]
#hence the reason for which [::-1] reverses the order of the string
#VERY USEFUL TRICK TO KNOW, FOR EXAMPLE WHEN BUILDING STRINGS CHARACTER BY CHARACTER
a = "string"
print(a[::])        #prints the string from beginning to end, with step of 1 (default values since empty)
print(a[::-1])      #does the same as above, but backwards, since the step is -1

#to get an explanation of how a method works, use the help function
help(str.capitalize)       #no need to print, since this function does so on its own
#MANY PROBLEMS REQUIRE COMPARING CASES OF STRINGS, so casefold function is very useful

#commentaire