def bunch_price(quantity: int, price: float) -> float:
    """
    Calculates the price for a bunch of fruit or a single kind.

    >>> bunch_price(0, 0.0)
    0.0
    >>> bunch_price(2, 5.0)
    10.0
    >>> bunch_price(2.0, 5.0)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for quantity parameter
    >>> bunch_price(2, 5)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for price parameter
    """

    #checking that arguments passed to function are of correct data type
    assert type(quantity) == int, "invalid data type for quantity parameter"
    assert type(price) == float, "invalid data type for price parameter"

    #checking that value for quantity is non-negative
    assert quantity >= 0, "quantity of fruits must be greater than or equal to zero"

    #checking that value for price is greater than zero
    assert price > 0, "price of fruits must be greater than zero"

    return quantity * price


#quantity for each type of fruit
num_apples = int(input("How many apples? "))
num_peaches = int(input("How many peaches? "))
num_watermelon = int(input("How many watermelons? "))

#price for each type of fruit
price_apples = 2.94
price_peaches = 3.99
price_watermelon = 7.99

'''
total price for each type of fruit purchased, separated from total calculation
for ease of reading (symmetry with getting input and constants above)
so adding another fruit to the bunch involves adding one new line in each chunk
'''
total_price_apples = num_apples * price_apples
total_price_peaches = num_peaches * price_peaches
total_price_watermelon = num_watermelon * price_watermelon

#total price for all fruits purchased, added rounding to avoid many position after decimal (limitations of computer)
total_price = round(total_price_apples + total_price_peaches + total_price_watermelon, 2)

#output the total price to the user, added sentence to explain result (error: when only one fruit, still plural)
print(f"The total price for {num_apples} apples, {num_peaches} peaches and {num_watermelon} watermelon is ${total_price}.")

#in Pycharm, use the following instructions to run the code in the Python Console (or Shell)
#exec(open('filepath').read())