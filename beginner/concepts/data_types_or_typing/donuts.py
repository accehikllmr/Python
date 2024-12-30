# take input from user
money = float(input("How much money do you have? "))

#price of a single donut
donut_price = 2.3

#number of whole donuts (using floor division) purchased given the user's money
num_donuts = int(money // donut_price)

# show the result
print(num_donuts)