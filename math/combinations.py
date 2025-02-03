# not importing from existing module, since conflicting functionality
def factorial(n: int) -> int:
    """
    Computes the factorial of an integer.

    Parameters:
         n (int): number for which to compute factorial

    Returns:
        (int): factorial of n

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    """

    # ADD ASSERTIONS TO VALIDATE INPUTS (if not covered in other function, which calls this one)

    # instantiating integer object to store value of factorial, beginning with 1 to allow multiplication
    fact = 1

    # iterating through all numbers from n to 2, 1 already accounted for and has no effect on product
    for num in range(n, 1, -1):
        fact *= num

    return fact
def combinations(n: int, k: int) -> int:
    """
    Computes n choose k, possible combinations of k elements from a set of size n.

    Parameters:
        n (int): size of set from which k elements are chosen
        k (int): number of elements chosen from set of size n

    Return:
        (int): possible combinations of k elements from a set of size n

    >>> combinations(0, 0)
    1
    >>> combinations(1, 0)
    1
    >>> combinations(1, 1)
    1
    >>> combinations(10, 1)
    10
    >>> combinations(4, 2)
    6
    >>> combinations(7, 5)
    21

    """

    # ADD ASSERTIONS TO VALIDATE INPUTS

    # formula for calculating n choose k
    combos = int(factorial(n) / (factorial(n - k) * factorial(k)))

    return combos

# aborting loop with invalid entry
n = 0

# looping to prevent unnecessary inputs
while n != -1:
    n = int(input("\nn = "))
    if n == -1:
        break
    k = int(input("k = "))
    print("combinations =", combinations(n, k))