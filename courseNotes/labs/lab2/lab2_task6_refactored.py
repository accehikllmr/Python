#getting user inputs for all numbers
first_num = float(input("First number: "))
second_num = float(input("Second number: "))
third_num = float(input("Third number: "))
fourth_num = float(input("Fourth number: "))

#determine the maximum and minimum values among four input values
maximum = max(first_num, second_num, third_num, fourth_num)
minimum = min(first_num, second_num, third_num, fourth_num)

#output average of maximum and minimum values to user, added sentence to explain output
print(f"The average of {maximum} and {minimum} is {(maximum + minimum) / 2}.")