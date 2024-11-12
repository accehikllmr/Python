import doctest

def remove_vowels(a_string: str) -> str:
    """
    Removes the vowels (a, e, i, o, u) from a string.

    >>> remove_vowels("moving")
    'mvng'
    >>> remove_vowels("a")
    ''
    >>> remove_vowels("")
    ''
    >>> remove_vowels("APple")
    'Ppl'
    >>> remove_vowels(" ch erry")
    ' ch rry'
    >>> remove_vowels("")
    ''
    >>> remove_vowels(" all ABout Da BAse")
    ' ll Bt D Bs'
    >>> remove_vowels("abc123")
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to a_string parameter has invalid characters
    >>> remove_vowels(123)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to a_string parameter is not of string type

    >>> remove_vowels("'check out this string'")
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to a_string parameter has invalid characters
    """
    # checking preconditions
    # a_string must be of string data type
    assert type(a_string) == str, "argument passed to a_string parameter is not of string type"

    # a_string cannot have invalid characters (only letters and spaces)
    assert a_string.replace(' ', "").isalpha() or a_string == "", "argument passed to a_string parameter has invalid characters"

    # list of vowels to iterate through in loop
    vowels = ['a', 'e', 'i', 'o', 'u']

    # looping through vowels to search for them in string
    for vowel in vowels:
        # looping through string to compare with each vowel
        for char in a_string:
            # comparing vowel to character, independent of case
            if vowel == char.casefold():
                # replacing vowel, uppercase and lowercase, with empty string
                a_string = a_string.replace(vowel.upper(), "")
                a_string = a_string.replace(vowel.lower(), "")

    # string with no vowels, uppercase and lowercase
    return a_string


doctest.testmod()