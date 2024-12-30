import doctest

def raw_food_credits(food_ate: float, credit_multiplier: int) -> float:
    """
    This function calculates the quantity of raw food credits, based on the mass of food eaten and
    the multiplier for the competitor class (e.g. featherweight)

    Preconditions:      food_ate            float >= 0
                        credit_multiplier   int >= 0

    >>> raw_food_credits(0.0, 10)
    0.0
    >>> raw_food_credits(15.0, 15)
    225.0
    >>> raw_food_credits(20, 20)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for food_ate parameter
    >>> raw_food_credits(20.0, 20.0)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for credit_multiplier parameter
    >>> raw_food_credits(-10.0, 10)
    Traceback (most recent call last):
    ...
    AssertionError: the food_ate parameter must be greater than or equal to zero
    >>> raw_food_credits(10.0, -10)
    Traceback (most recent call last):
    ...
    AssertionError: the credit_multiplier parameter must be greater than or equal to zero
    """

    #checking for correct data types
    assert type(food_ate) == float, "invalid data type for food_ate parameter"
    assert type(credit_multiplier) == int, "invalid data type for credit_multiplier parameter"

    #checking for positive values
    assert food_ate >= 0, "the food_ate parameter must be greater than or equal to zero"
    assert credit_multiplier >= 0, "the credit_multiplier parameter must be greater than or equal to zero"

    #formula given in problem description
    raw_food_credits = food_ate * credit_multiplier

    return raw_food_credits

def my_food_credit(food_ate: float, opp_food_ate: float) -> float:
    """
    This function calculates my food credits, by subtracting the deduction from the raw value.

    Preconditions:  food_ate >= 0
                    opp_food_ate >= 0

    >>> my_food_credit(20.0, 10.0)
    170.0
    >>> my_food_credit(6.12, 36.172)
    0.0
    >>> my_food_credit("10", 20.0)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for food_ate parameter
    >>> my_food_credit(20.0, "10")
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for opp_food_ate parameter
    """

    #checking that input data are of float type
    assert type(food_ate) == float, "invalid data type for food_ate parameter"
    assert type(opp_food_ate) == float, "invalid data type for opp_food_ate parameter"

    #checking that input values are positive values
    assert food_ate >= 0, "food_ate parameter must be equal to or greater than 0"
    assert opp_food_ate >= 0, "oop_food_ate parameter must be equal to or greater than 0"

    #function call to calculate raw food credits
    gross_food_credits = raw_food_credits(food_ate, featherweight_multiplier)

    #function call to calculate deduction, adjusted using the multiplier
    deduction = raw_food_credits(opp_food_ate, strawweight_multiplier) * 0.2

    #formula given in problem description
    net_food_credits = gross_food_credits - deduction

    #return largest value, 0.0 if net_food_credits is negative
    return max(0.0, round(net_food_credits, 1))

def opponent_food_credit(opp_food_ate: float, food_ate: float) -> float:
    """
    This function calculates opponent food credits, by subtracting the deduction from the raw value.

    Preconditions:  opp_food_ate >= 0
                    food_ate >= 0

    >>> opponent_food_credit(10.0, 20.0)
    110.0
    >>> opponent_food_credit(263.1, 126.6)
    3693.3
    >>> opponent_food_credit(10.0, 1000.0)
    0.0
    >>> opponent_food_credit("10", 20.0)
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for opp_food_ate parameter
    >>> opponent_food_credit(20.0, "10")
    Traceback (most recent call last):
    ...
    AssertionError: invalid data type for food_ate parameter
    """

    #checking that input data are of float type
    assert type(food_ate) == float, "invalid data type for food_ate parameter"
    assert type(opp_food_ate) == float, "invalid data type for opp_food_ate parameter"

    #checking that input values are positive values
    assert food_ate >= 0, "food_ate parameter must be equal to or greater than 0"
    assert opp_food_ate >= 0, "oop_food_ate parameter must be equal to or greater than 0"

    #function call to calculate raw food credits
    gross_food_credits = raw_food_credits(opp_food_ate, strawweight_multiplier)

    #function call to calculate deduction, adjusted using the multiplier
    deduction = raw_food_credits(food_ate, featherweight_multiplier) * 0.2

    #formula given in problem description
    net_food_credits = gross_food_credits - deduction

    #return largest value, 0.0 if net_food_credits is negative
    return max(0.0, round(net_food_credits, 1))

featherweight_multiplier = 10
strawweight_multiplier = 15

if __name__ == "__main__":
    doctest.testmod()
