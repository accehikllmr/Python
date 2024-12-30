# Q1

# this tuple has three elements, 1 list object and 2 integer objects
a = ([1, 2, 3], 4, 5)
print(f"tuple prior to attempted modification: \t{a}")

'''
this command targets the first element in the tuple, the list object, and then targets the 
first element in the list object, the integer 1
'''
a[0][0] = 100

# since this element belongs to a list object, which is a mutable data type, its value can be modified
print(f"tuple after attempted modification: \t{a}")

# initially, it seems that we are trying to modify a tuple object, but in fact we are modifying a list object

# Q2

# this list has three elements, 1 tuple object and 2 integer objects
a = [(1, 2, 3), 4, 5]
print(f"\nlist prior to attempted modification: \t{a}")

'''
this command targets the first element in the list, the tuple object, and then targets the 
first element in the tuple object, the integer 1
using try and except, otherwise TypeError crashes program
'''
try:
    # this item assignment is unsuccessful, because tuples are immutable objects
    a[0][0] = 100
except:
    # hence, the list remains unchanged - no element has been modified
    print(f"list after attempted modification: \t\t{a}\n")

# initially, it seems that we are trying to modify a list object, but in fact we are trying to modify a tuple object

# Q3

# characters used to make ASCII eyes and noses
eyes = ['O', '0', '^']
noses = ['.', '|', '>', '-', 'o']

# iterate through all eyes, since every possibility must be used in making faces
for eye in eyes:
    # iterate through all noses, since every possibility must be used in making faces
    for nose in noses:
        # concatenating eyes and nose to create face
        face = eye + nose + eye
        # printing on same line, to avoid lengthening output space
        print(face, end = '\t\t')

# Q4

# initializing list in which user inputs will be stored
a = [[], [], []]

print(f"\n\nthe list a = {a}")

# counting iterations to index elements of a and show their ids
count = 0

# iterating through elements of list object a
for lst in a:
    letters = input("Input 3 chars (e.g., X Y Z): ")
    x = letters.split()
    # this list object is not identical to the list object in a
    lst = x
    # showing respective ids, they are not identical, so assigning x to lst does not change the elements in a
    print(f"lst id = {id(lst)}, a[{count}] id = {id(a[count])}")

    '''
    in fact, we see that the ids for lst repeat every 2 iterations of the loop, so it seems that a copy of the
    element in a is created, used for one iteration, and then erased before being used in the after next iteration
    meanwhile, the ids for all elements in a are consistent and equal, suggesting that their id is equal to that 
    of the entire list
    '''

print(f"the new list a = {a}")

# here is a program that works according to the specifications
a = [[], [], []]

print(f"\n\nthe list a = {a}")

# counting iterations to index elements of a, i.e. find their position
position = 0

# iterating through indices of list object a, instead of items
for position in range(0, len(a)):
    letters = input("Input 3 chars (e.g., X Y Z): ")
    x = letters.split()
    a[position] = x

print(f"the new list a = {a}")