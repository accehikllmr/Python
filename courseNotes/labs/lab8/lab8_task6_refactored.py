import doctest
import copy

# reusing code from last problem, but adding method for removing vowels
class String:

    def __init__(self, a_string: str) -> None:
        """
        Method to instantiate a String object

        Parameters:
            a_string (str): the object, a string of characters

        >>> word = String("banana")
        >>> print(word)
        String(banana)
        >>> word = String(1)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to a_string parameter must be a string object
        """

        # checking that argument passed to object instantiation method is of correct type
        assert isinstance(a_string, str), "argument passed to a_string parameter must be a string object"

        self._the_string = a_string
        self._length = len(self._the_string)

    def __str__(self) -> str:
        """
        Outputs string representation of the object.

        >>> word = String("banana")
        >>> word.__str__()
        'String(banana)'
        """

        return f"String({self._the_string})"

    def is_alphabetic(self) -> bool:
        """
        Determines whether a string has exclusively alphabetic characters, excluding spaces.

        Returns:
            (bool): whether a string has exclusively alphabetic characters

        >>> word = String("banana")
        >>> word.is_alphabetic()
        True
        >>> word = String("banan3")
        >>> word.is_alphabetic()
        False
        """

        # using isalpha method insufficient, since spaces are valid characters in a meaningful string
        return self._the_string.replace(' ', '').isalpha()

    def reverse_str(self) -> str:
        """
        Reverses the order of characters in a string.

        >>> word = String("''")
        >>> word.reverse_str()
        "''"
        >>> word = String("abcdefgh")
        >>> word.reverse_str()
        'hgfedcba'
        >>> word = String("c")
        >>> word.reverse_str()
        'c'
        >>> word = String("")
        >>> word.reverse_str()
        ''
        >>> word = String("123")
        >>> word.reverse_str()
        '321'
        >>> word = String(" a@54! ")
        >>> word.reverse_str()
        ' !45@a '
        >>> word = String("93hfg2vb3 [12]3fo1]-vckme91[")
        >>> word.reverse_str()
        '[19emkcv-]1of3]21[ 3bv2gfh39'
        """

        '''
        no need to loop here, simply take the original string (default from index 0 to -1, inclusive)
        but increment in the opposite direction, so -1 instead of default which is 1
        '''
        return self._the_string[::-1]

    def voweless(self) -> str:
        """
        Removes the vowels from a copy of the string object.

        Returns:
             (str): copy of string object, without vowels

        >>> word = String("moving")
        >>> word.voweless()
        'mvng'
        >>> word = String("a")
        >>> word.voweless()
        ''
        >>> word = String("APple")
        >>> word.voweless()
        'Ppl'
        >>> word = String(" ch erry")
        >>> word.voweless()
        ' ch rry'
        >>> word = String(" all ABout Da BAse")
        >>> word.voweless()
        ' ll Bt D Bs'
        >>> word = String("")
        >>> word.voweless()
        Traceback (most recent call last):
        ...
        AssertionError: string object contains non-alphabetic characters and thus cannot be transformed
        """

        # checking precondition, using custom method (method is for object, so use on self, not its attribute)
        assert self.is_alphabetic(), "string object contains non-alphabetic characters and thus cannot be transformed"

        # only lowercase vowels, redundant to add uppercase given existing string methods
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # string objects are immutable, so no need to make a deepcopy, assigning here so that every loop below updates same string
        no_vowel_string = self._the_string

        # iterate through each character of original string, since copy will change in length, so that it can be checked case independently against lowercase vowels
        for char in self._the_string:
            if char.casefold() in vowels:
                # casefold method insufficient for removal, need to specify upper and lower, need assignment since method returns a copy
                no_vowel_string = no_vowel_string.replace(char.upper(), '')
                no_vowel_string = no_vowel_string.replace(char.lower(), '')

        return no_vowel_string

doctest.testmod()