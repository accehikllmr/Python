import doctest

def is_prime(num: int) -> bool:
    """
    Determines if a number is prime.

    Parameters:
        nums (int): number to be evaluated for its primeness

    Returns:
        (bool): whether a given number is prime

    >>> is_prime(5)
    True
    >>> is_prime(10)
    False
    >>> is_prime(23)
    True
    """
    # check preconditions
    # num must be a positive int
    assert isinstance(num, int) and num > 0, "num must be a positive int"

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

    Parameters:
        start (int): lower bound of range in which prime numbers are searched for
        stop (int): upper bound of range in which prime numbers are searched for

    Returns:
        (int): count of prime numbers in given range

    >>> count_primes(3, 10)
    3
    >>> count_primes(2, 12)
    5
    >>> count_primes(1, 100)
    25
    """
    # check preconditions
    # start must be a positive int
    assert isinstance(start, int) and start > 0, "start must be a positive int"
    # stop must be a positive int
    assert isinstance(stop, int) and stop > 0, "stop must be a positive int"

    # create a counter variable
    counter = 0

    # loop from [start, stop]
    for num in range(start, stop + 1):
    #   if prime add 1 to counter
        if is_prime(num):
            counter += 1
            prime_or_not['prime'].append(num)
        else:
            # appending to list of not prime numbers in global dictionary object
            prime_or_not['not prime'].append(num)

    # return total number of primes
    return counter

# adding dictionary to store numbers, either prime or not, could put within a function instead, either it allows to see primes, not just count
prime_or_not = {
    'prime': [],
    'not prime': []
}

# function call to populate dictionary
print("Prime numbers in given range: " + str(count_primes(1, 10000)))

# output updated dictionary to user
for item in prime_or_not.items():
    print(item)

doctest.testmod()