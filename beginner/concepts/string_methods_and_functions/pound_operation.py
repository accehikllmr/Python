#taking user input as a string
user_input = input("Please provide an expression in the format of x # y: ")

#locate the position of the pound operator in the string
pound_index = user_input.find('#')

#using the index of the pound operator, find the numbers in the string
x = int(user_input[:pound_index])
y = int(user_input[pound_index + 1:])

#calculating and outputting the result of the operation
