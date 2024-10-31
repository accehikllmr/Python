#Q1
def get_larger(num_1: int = 0, num_2: int = 0) -> int:
    """
    Returns the larger of two numbers.

    >>> get_larger(2, 2)
    2
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
    >>> get_larger("")
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type passed as argument
    >>> get_larger(1.0, 2.0)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type passed as argument
    """

    #cheecking that both arguments passed to function are integers
    assert type(num_1) == type(num_2) == int, "invalid data type passed as argument"

    if num_2 > num_1:
        return num_2
    #condition includes when numbers are equal, so which one returned matters not
    else:
        return num_1

#Q2
'''
by default, for loops start at 0 and increment by 1, here we have only defined an end - 10
but this end is not included, so this will print: 0\n1\n2\n3\n4\n5\n6\n7\n8\n9
'''
print(">>> for i in range(10):\n...\t\tprint(i)")

for i in range(10):
    print(i)

'''
this loop starts at 2 and ends at 10 (not included), the increments are 1, by default
this will print: 2\n3\n4\n5\n6\n7\n8\n9
'''
print("\n>>> for i in range(2, 10):\n...\t\tprint(i)")
for i in range(2, 10):
    print(i)

'''
this loop starts at 10 at ends at 2, but the increments are 1
so, this will print: ""
'''
print("\n>>> for i in range(10, 2):\n...\t\tprint(i)")
for i in range(10, 2):
    print(i)

'''
this loop will print the same thing as for i in range(2, 10)
the increments are 1 by default, so specifying them adds nothing new
this will print: 2\n3\n4\n5\n6\n7\n8\n9
'''
print("\n>>> for i in range(2, 10, 1):\n...\t\tprint(i)")
for i in range(2, 10, 1):
    print(i)

'''
this loop starts at 2, ends at 10 and increments by 3
this will print: 2\n5\n8
'''
print("\n>>> for i in range(2, 10, 3):\n...\t\tprint(i)")
for i in range(2, 10, 3):
    print(i)

'''
this loop starts at 10, ends at 2 and increments by -2
this will print: 10\n8\n6\n4
'''
print("\n>>> for i in range(10, 2, -2):\n...\t\tprint(i)")
for i in range(10, 2, -2):
    print(i)

#Q3
'''
moving the statement between the while and if conditions means that the if condition
will be satisfied one iteration earlier, HOWEVER this makes no difference for the output
since in either case, the print statement follows the if condition for the break statement,
so the value of 5 is not printed and the loop stop at when x = 5
'''

x = 0
while x < 10:
    x += 1
    if x == 5:
        break
    print(x)

print("\nloop stopped at " + str(x))

#Q4
'''
the for loop updates the value of x after each iteration, the while loop,
as it is written updates the value of x before each iteration, so the statement
x += 1 must be moved to after the print statement AND inside the loop prior to the
continue statement
'''
print("\nwhile loop:")
x = 0
while x < 10:
    #x += 1
    if x == 5:
        x += 1
        continue
    print(x)
    x += 1

print("\nfor loop:")
for x in range(10):
    if x == 5:
        continue
    print(x)

#Q5
'''
if we simply move the statement after the print statement, without adding it
inside the if conditional block, then the value of x never updates after reaching
5 and the program loops infinitely
'''
print("\nwhile loop:")
x = 0
while x < 10:
    #x += 1
    if x == 5:
        continue
    print(x)
    x += 1