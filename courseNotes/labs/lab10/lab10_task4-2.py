import doctest
from typing import Dict

def key_value_types(a_dict: dict) -> bool:
    """
    Iterates through keys and values of a dictionary object to determine if all keys are strings
    and all values are integers.

    Parameters:
         a_dict(dict):  dictionary object containing key-value pairs of any type

    Returns:
        (bool): evaluation of whether all keys are string and all values are integers

    >>> key_value_types({'a': 1, 'b': 2, 'c': 3})
    True
    >>> key_value_types({1: 'a', 2: 'b', 3: 'c'})
    False
    >>> key_value_types({'a': 1, 'b': 2, 3: 'c'})
    False
    """
    # iterating through dictionary items, since checking types of both keys and values
    for key, value in a_dict.items():
        # either type for key or value being wrong returns False and exits function
        if type(key) != str or type(value) != int:
            return False
    # if no keys and values trigger the previous conditional
    return True

def return_subject_grade(subject_grade: Dict[str, int], subject: str, new_grade: int) -> Dict[str, int]:
    """
    Copies a given dictionary and updates the grade for the specified subject.

    Parameters:
        subject_grade (Dict[str: int]): dictionary in which subjects (keys)
                                        and their respective grades (values) are stored
        subject (str): name of a subject (key) contained in the dictionary
        new_grade (int): updated grade (value) which will overwrite existing grade in new dictionary object

    Returns:
        (Dict[str, int]):   copy of subject_grade dictionary object, with grade updated for the specified subject

    >>> return_subject_grade({"Math": 90, "English": 75, "Introduction to Python": 95, "Biology": 88}, "Math", 70)
    {'Math': 70, 'English': 75, 'Introduction to Python': 95, 'Biology': 88}
    >>> return_subject_grade({"Math": 90, "English": 75, "Introduction to Python": 95, "Biology": 88}, "English", 55)
    {'Math': 90, 'English': 55, 'Introduction to Python': 95, 'Biology': 88}
    >>> return_subject_grade({"Math": 90, "English": 75, "Introduction to Python": 95, "Biology": 88,\
            "Introduction to Machine Learning": 97, "Database": 100}, "Introduction to Machine Learning", 56)
    {'Math': 90, 'English': 75, 'Introduction to Python': 95, 'Biology': 88, 'Introduction to Machine Learning': 56, 'Database': 100}
    >>> return_subject_grade({"Math": 90, "English": 75, "Introduction to Python": 95, "Biology": 88,\
            "Introduction to Machine Learning": 97, "Database": 100})
    Traceback (most recent call last):
    ...
    TypeError: return_subject_grade() missing 2 required positional arguments: 'subject' and 'new_grade'
    >>> return_subject_grade({"Math": 90, "English": 75, "Introduction to Python": 95, "Biology": 88}, "Spanish", 65)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to subject parameter must be an existing dictionary key
    >>> return_subject_grade({"Math": 90, "English": 75, "Introduction to Python": 95, "Biology": 88}, "Spanish", 60.5)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to new_grade parameter must be an integer object
    >>> return_subject_grade({"Math": 90, "English": 75, "Introduction to Python": 95, "Biology": 88}, 65, 65)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to subject parameter must be a string object
    >>> return_subject_grade(("Math", 90, "English", 75, "Introduction to Python", 95, "Biology", 88), "Math", 65)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to subject_grade parameter must be a dictionary object
    >>> return_subject_grade({90: "Math", 75: "English", 95: "Introduction to Python", 88: "Biology"}, "Math", 65)
    Traceback (most recent call last):
    ...
    AssertionError: keys and values must be string and integer types, respectively
    """
    # checking correct types for arguments passed to function parameters
    assert type(subject) == str, "argument passed to subject parameter must be a string object"
    assert type(new_grade) == int, "argument passed to new_grade parameter must be an integer object"
    assert type(subject_grade) == dict, "argument passed to subject_grade parameter must be a dictionary object"

    # checking correct types for keys and values in dictionary
    assert key_value_types(subject_grade), "keys and values must be string and integer types, respectively"

    # checking that argument passed to subject parameter is existing key in dictionary object
    assert subject in subject_grade.keys(), "argument passed to subject parameter must be an existing dictionary key"

    # initializing new dictionary, to not modify the original one
    subject_grade_copy = subject_grade.copy()

    # updating new dictionary according to subject and new_grade arguments, but only if subject is existing key
    subject_grade_copy.update({subject: new_grade})  # without curly brackets around arguments, interprets left side as str

    # returning new dictionary, not original one
    return subject_grade_copy

doctest.testmod()