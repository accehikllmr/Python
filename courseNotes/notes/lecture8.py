#CONDITIONAL STATEMENTS

#for conditional statements, can use pass keyword as placeholder when writing code skeleton
print(">>> if 2 == 2:\n...\t\tpass\t#adding this command prevents a syntax error from leaving empty\n")

if 2 == 2:
    pass    #prevents SyntaxError

'''
Python is "lazy" when evaluating boolean statements, so if the first statement in a compound statement yields 
the truth value of the compound statement, it does not evaluate the second statement, even if doing so would 
result in a runtime error
'''
#a disjunction is true when either statement is true, since the first statement is true, the second one is not evaluated
print(">>> if 2 == 2 or 2 / 0 == 1:")
if 2 == 2 or 2 / 0 == 1:
    print("\t2 == 2 is true, so the disjunction is true, so I was too lazy to evaluate 2 / 0...\n")

print(">>> if 2 == 3 and 2 / 0 == 1:")
if 2 == 3 and 2 / 0 == 1:
    pass
    #the following line will not print, since the condition is false, so added below for output
print("\t2 == 3 is false, so the conjunction is false, so I was too lazy to evaluate 2 / 0...\n")

#REFACTORING

#restructuring code to improve readability and efficiency, should be done at some regular interval

#nested conditional statements can be refactored to be more efficient
print("this nested conditional\n>>> if 2 == 2:\n...\t\tif 1 == 1:\n...\t\t\tif 0 == 0:\n")
if 2 == 2:
    if 1 == 1:
        if 0 == 0:
            print("can be refactored as a single conditional\n>>> if 2 == 2 and 1 == 1 and 0 == 0:\n")
else:
    print("this is unreachable code")

#refactored
if 2 == 2 and 1 == 1 and 0 == 0:
    pass
else:
    print("more unreachable code")

#boolean statements can be refactored to be more efficient
x = 5

if x > 3:
    print("this boolean evaluation\n>>> if x > 3:\n...\t\tprint(True)\n... else:\n...\t\tprint(False)\n")
else:
    print("reachable only if value of x is changed.")

print("can be refactored as\n>>> print(x > 3)")

#refactored, commented out so as to not ruin output
#print(x > 3)

#activity
def get_larger(num_1: int = 0, num_2: int = 0) -> int:
    """
    Returns the larger of two numbers.

    >>> get_larger(3, 2)
    3
    >>> get_larger(2, 3)
    3
    >>> get_larger(-3, 2)
    2
    >>> get_larger(3, -2)
    3
    >>> get_larger(3)
    3
    >>> get_larger(-3)
    0
    >>> get_larger()
    0
    """

    #cheecking that both arguments passed to function are integers
    assert type(num_1) == type(num_2) == int, "invalid data type passed as argument"

    if num_2 > num_1:
        return num_2
    #condition includes when numbers are equal, so which one returned matters not
    else:
        return num_1

#LOOPS

#use for loops when the number of iterations is defined, or known (e.g. entering grades for 25 students)
#use while loops in all other circumstances (e.g. iterating until the user inputs "end")

#break statement exits the loop (stops looping)
#continue exits the CURRENT ITERATION of the loop, thus skipping (continues looping)

#there doesn't seem to exist explicit conventions for naming variables used in loops (using i, j, char) or meaningful names
#perhaps it depends if iterating over a range or over an object (string, set, list, etc.)

#activity 1 - for loop is better because we have a determined number of loops to run
loops = int(input("\nHow many loops? "))
message = input("Message: ")

print("\nfor loop:")
for i in range(loops):
    print(message)

print("\nwhile loop:")
while loops != 0:
    print(message)
    loops -= 1

#activity 2 - for loop is better because we are checking each letter in a string object
for_message = ""
print("\nfor loop")
for j in message:
    if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
        continue
    for_message = for_message + j
print(for_message)

print("\nwhile loop:")
while_message = ""
while loops != len(message):
    letter = message[loops]
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        loops += 1
        continue
    while_message = while_message + letter
    loops += 1
print(while_message)

#activity 3 - for loop is simpler because we are iterating through a string object
for_message = ""
print("\nfor loop:")
for k in message:
    for_message = k + for_message
print(for_message)

while_message = ""
print("\nwhile loop:")
while loops != 0:
    loops -= 1
    while_message = while_message + message[loops]
print(while_message + "\n")

#activity 4 - while loop is much simpler because we are waiting for a condition to be fulfilled before stopping
user_input = ""
while user_input != 'Y' or user_input != 'N':
    user_input = input("Are you a student in this course (Y/N)? ").upper()
    if user_input == 'Y':
        print("GLHF!!\n")
        break
    elif user_input == 'N':
        print(":)\n")
        break

#since the number of loops needed for this activity is not predefined, I am not sure that it's possible to use a for loop