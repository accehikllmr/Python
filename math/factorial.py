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

n = 0

while n != -1:
    n = int(input("\nn = "))
    if n == -1:
        break
    print(f"{n}! = {factorial(n)}")