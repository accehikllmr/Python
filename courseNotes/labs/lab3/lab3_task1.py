#taking user input as a string
user_input = input("Please provide an expression in the format of x # y: ")

#locate the position of the pound operator in the string
pound_index = user_input.find('#')

#using the index of the pound operator, find the numbers in the string
x = int(user_input[:pound_index])
y = int(user_input[pound_index + 1:])

#calculating and outputting the result of the operation
print(x ** 2 - y ** 2)

'''
MY SOLUTION, BUT NOT SUBMITTED IN ORDER TO GET FULL MARKS

#taking user input in the form of a string, not converted since includes symbol
#using the split function to separate the characters, using spaces as delimiters
input_values = [i for i in input("Please provide an expression in the format of x # y: ").split()]

#extracting digits from above list, using indexing, and converting them to integers
#assuming no mistakes in user input, string will have three only elements
first_number = int(input_values[0])
second_number = int(input_values[2])

#perform the calculation which corresponds to the # operator
print((first_number ** 2) - (second_number ** 2))
'''
