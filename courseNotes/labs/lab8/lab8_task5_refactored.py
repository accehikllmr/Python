import doctest

# strings are already objects, so perhaps making a duplicate object is not useful, but just a matter of practicing here
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

doctest.testmod()