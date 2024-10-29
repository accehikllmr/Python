#quantity for each type of fruit
num_apples = int(input("How many apples? "))
num_peaches = int(input("How many peaches? "))
num_watermelon = int(input("How many watermelons? "))

#price for each type of fruit
price_apples = 2.94
price_peaches = 3.99
price_watermelon = 7.99

#price of all fruit purchased
total_price = num_apples * price_apples + num_peaches * price_peaches + num_watermelon * price_watermelon

#output the total price to the user
print(total_price)

#in Pycharm, use the following instructions to run the code in the Python Console (or Shell)
#exec(open('filepath').read())