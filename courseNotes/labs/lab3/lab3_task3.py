# get input
age = int(input("What is the child's age? "))
height = int(input("What is the child's height? "))

# you can add any line of code between this line and the line with return
child_buy_ticket = age > 6 or height > 120

# show result
print(child_buy_ticket)
