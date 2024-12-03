# CLASSES

# int and float are basic data types, usually not treated as classes in other languages, but so in Python
# str, list, dict, set, etc. are other examples of classes, or types, that are built-in to Python
# in the current version of Python, there is no functional difference between types and classes

# by convention, class names are written in uppercase camelCase (or PascalCase)
class Person:

    # constructor method which instantiates the object, defines all of its attributes upon object instantiation
    def __init__(self, name: str, age: int, gender: str, height: float, weight: float):
        """
        Constructor method, gives person object all fundamental attributes.

        Parameters:
            name (str): person's name, in English alphabet
            age (int): person's age, in years
            gender (str): person's gender, on a non-binary spectrum
            height (float): person's height, in centimeters
            weight (float): person's weight, in kilograms

        >>> first_person = Person("Michel", 33, "Male", 187.0, 80.0)
        >>> print(f"{first_person._name} is a {first_person._age}-year-old {first_person._gender} standing at {first_person._height}"\
        f" centimeters and weighing in at {first_person._weight} kilograms.")
        Michel is a 33-year-old Male standing at 187.0 centimeters and weighing in at 80.0 kilograms.
        >>> first_person = Person("", 33, "Male", 187.0, 80.0)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to name parameter must be a string object at least 1 character in length
        >>> first_person = Person("Michel", -33, "Male", 187.0, 80.0)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to age parameter must be an integer object larger than or equal to 0 years
        >>> first_person = Person("Michel", 33, "", 187.0, 80.0)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to gender parameter must be a string object at least 1 character in length
        >>> first_person = Person("Michel", 33, "Male", -187.0, 80.0)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to height parameter must be a float object larger than or equal to 10 centimeters
        >>> first_person = Person("Michel", 33, "Male", 187.0, 80)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to weight parameter must be a float object larger than 0 kilograms
        """
        # checking preconditions
        assert isinstance(name, str) and len(name) > 0, \
            "argument passed to name parameter must be a string object at least 1 character in length"
        assert isinstance(age, int) and age >= 0, \
            "argument passed to age parameter must be an integer object larger than or equal to 0 years"
        assert isinstance(gender, str) and len(gender) > 0, \
            "argument passed to gender parameter must be a string object at least 1 character in length"
        assert isinstance(height, float) and height >= 10, \
            "argument passed to height parameter must be a float object larger than or equal to 10 centimeters"
        assert isinstance(weight, float) and weight > 0, \
            "argument passed to weight parameter must be a float object larger than 0 kilograms"

        '''
        _ prior to variable name indicates that the variable is private (simply convention) and should not be accessed
        or updated outside of the class
        '''
        self._name = name
        self._age = age
        self._gender = gender
        self._height = height
        self._weight = weight

    # setter functions allow changing the attributes of an object from outside the class, but adds protections from invalid data
    def set_name(self, name: str):
        """
        Setter function for name attribute.

        Parameters:
            name (str): new name for person

        >>> first_person = Person("Michel", 33, "Male", 187.0, 80.0)
        >>> first_person._name
        'Michel'
        >>> first_person.set_name("Bob")
        >>> first_person._name
        'Bob'
        >>> first_person.set_name("")
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to name parameter must be a string object at least 1 character in length
        """
        # method has parameter, therefore need to check preconditions
        assert isinstance(name, str) and len(name) > 0, \
            "argument passed to name parameter must be a string object at least 1 character in length"

        self._name = name

    # usually, would have setter function for all attributes, which would have more or less the same composition

    # getter function allow extracting the attributes of an object from outside the class
    def get_name(self) -> str:
        """
        Getter function for name attribute.

        >>> first_person = Person("Michel", 33, "Male", 187.0, 80.0)
        >>> first_person.get_name()
        'Michel'
        """

        return self._name

    # usually, would have getter function for all attributes, which would have more or less the same composition

    # all other methods (functions within classes) must also begin with self as the first parameter
    def grow_older(self):
        """
        Makes person grow older by one year.

        >>> first_person = Person("Michel", 33, "Male", 187.0, 80.0)
        >>> first_person._age
        33
        >>> first_person.grow_older()
        >>> first_person._age
        34
        """
        # no need to check assertions, since method has no parameters other than self, which is already validated upon instantiation
        self._age += 1

    # other methods could be created to define what objects can do (e.g. grow_taller, gain_weight, lost_weight, etc.)

    # method used to output the string representation of an object, rather than the standard which gives the memory address
    def __str__(self) -> str:
        """
        Output string representation of an object.

        Returns:
            (str): string representation of an object

        >>> first_person = Person("Michel", 33, "Male", 187.0, 80.0)
        >>> print(first_person)
        Person(Michel, 33, Male, 187.0, 80.0)
        """
        # format in which we want object printed, using print function (below is the standard)
        return f"Person({self._name}, {self._age}, {self._gender}, {self._height}, {self._weight})"

    # method used to compare objects according to desired criteria (e.g. age, height, etc.), need other parameter for second object
    def __eq__(self, other) -> bool:
        """
        Outputs whether two objects have the same name.

        Parameters:
            other (Person): object with which the comparison is being made

        Returns:
            (bool): whether two objects have the same names

        >>> first_person = Person("Michel", 33, "Male", 187.0, 80.0)
        >>> second_person = Person("Michel", 61, "Male", 173.0, 87.0)
        >>> first_person == second_person
        True
        >>> first_person = Person("Michel", 33, "Male", 187.0, 80.0)
        >>> second_person = Person("Kelly", 61, "Male", 173.0, 87.0)
        >>> first_person == second_person
        False
        """
        return self._name == other._name

    # the two previous methods are known as 'magic methods', and many more exists in Python (e.g. ** is __pow__, != is __ne__)

# FILE I/O

# to open a file and bind it to a variable, last character specifies the mode (read, write, overwrite, etc.)
demo_file = open("lecture_2.txt", 'r')

# when accessing a file in a different directory than the Python source file, can use the absolute path (but this varies by system)
abs_demo_file = open("C:/Users/acceh/GitHub/Python/courseNotes/notes/lecture_2.txt", 'r')
# can switch directions of slashes to avoid problems with escape characters

# open files must be closed when finished using them, lest they become corrupted or overextend CPU resources
demo_file.close()
abs_demo_file.close()

# better to open the following way, since automatically closed once finished
with open("lecture_2.txt", 'r') as demo_file:
    # by default, readline() prints the first line of the file
    print(demo_file.readline())
    # but, can specify how many bytes to read line (in this case second, since last call read first line)
    print(demo_file.readline(90))
    # can read entire file with read()
    print(demo_file.read())
    # can store entire file, line by line, as elements of a list
    file_lines = demo_file.readlines()
    for line in file_lines:
        print(line)