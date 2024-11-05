import doctest

def is_prime(num: int) -> bool:
    """
    Determines if a number is prime.

    >>> is_prime(5)
    True
    >>> is_prime(10)
    False
    >>> is_prime(23)
    True
    """
    # check preconditions
    # num must be a positive int
    assert type(num) == int and num > 0, "num must be a positive int"

    if num == 1:
        return False

    # loop through all numbers from [2, num]
    for i in range(2, num):
    #   if divisible by any number in this range then num is not prime
        if num % i == 0:
            return False

    # return if the number is prime
    return True

def count_primes(start: int, stop: int) -> int:
    """
    Counts the total of prime numbers in the range [start, stop]

    >>> count_primes(3, 10)
    3
    >>> count_primes(2, 12)
    5
    >>> count_primes(1, 100)
    25
    """
    # check preconditions
    # start must be a positive int
    assert type(start) == int and start > 0, "start must be a positive int"
    # stop must be a positive int
    assert type(stop) == int and stop > 0, "stop must be a positive int"

    # create a counter variable
    counter = 0

    # loop from [start, stop]
    for num in range(start, stop + 1):
    #   if prime add 1 to counter
        if is_prime(num):
            counter += 1

    # return total number of primes
    return counter

doctest.testmod()