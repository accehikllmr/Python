import math
import random

#the ceil method (for ceiling) rounds a value, x, to the next highest integer
x = 3.1
int_above_x = math.ceil(x)
print(f"using the ceiling method on {x} gives {int_above_x}")

#the cos method (for cosine) takes the cosine of the given value, x
x = 0.5
cosine_of_x = math.cos(x)
print(f"the cosine of {x} is {cosine_of_x}")

#the radians method converts an angle from degrees to radians
x = 57.3
degrees_in_radians = math.radians(x)
print(f"{x} in radians is{degrees_in_radians}")

#the exp method (for exponential) is the natural number e raised to the power of a value, x
x = 3
exponential_raised = math.exp(x)
print(f"the natural number e raised to the power of {x} is {exponential_raised}")

#the inf variable represents a floating point value of positive infinity
print(f"this is what inifity looks like in Python: {math.inf}")

'''
the normalvariate method, given a mean, outputs a random number within the given standard deviation from that mean
CAREFUL - the first time that I ran this in PyCharm, the script would restart over and over and I don't know why...
'''
mean = 67
standard_deviation = 2
x = random.normalvariate(mean, standard_deviation)
print(f"{x} is within {standard_deviation} standard deviations of {mean}")

#the randint method outputs a random integer within the given range, between a and b (both inclusive)
x = random.randint(1,100)
print(f"{x} is a random number between 1 and 100")

'''
the randrange method is similar to the randint method, but it provides the option of defining an interval
below, only the following numbers can be returned: 1, 11, 21, 31, ... 91
'''
x = random.randrange(0, 100, 10)
print(f"{x} is a random number between 1 and 100, but by steps of 10")

#the random method returns a random value between 0 and 1 (inclusive)
x = random.random()
print(f"{x} is a random number between 0 and 1")

#the uniform method returns a random value between rational numbers
x = random.uniform(0.5, 0.6)
print(f"{x} is a random number between 0.5 and 0.6")