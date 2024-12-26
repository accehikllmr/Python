import doctest
from typing import Dict

def update_subject_grade(subject_grade: Dict[str, int], subject: str, new_grade: int) -> Dict[str, int]:
    """
    Given a subject and an updated grade, the existing grade for that subject is overwritten in the dictionary containing this information.

    Parameters:
        subject_grade (Dict[str: int]): dictionary in which subjects (keys) and their respective grades (values) are stored
        subject (str): name of a subject (key) contained in the dictionary
        new_grade (int): updated grade (value) which will overwrite existing grade

    >>> update_subject_grade({'math': 75, 'french': 65, 'gym': 85}, 'french', 65)
    {'math': 75, 'french': 65, 'gym': 85}
    >>> update_subject_grade({'math': 75, 'french': 65, 'gym': 85}, 'french', 95)
    {'math': 75, 'french': 95, 'gym': 85}
    >>> update_subject_grade({'math': 75, 'french': 65, 'gym': 85}, 'english', 95)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to subject parameter must be an existing dictionary key
    >>> update_subject_grade({75: 'math', 65: 'french', 85: 'gym'}, 'french', 95)
    Traceback (most recent call last):
    ...
    AssertionError: keys and values must be string and integer types, respectively
    >>> update_subject_grade({'math': 75, 'french': 65, 'gym': 85}, 'english', 95.0)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to new_grade parameter must be an integer object
    >>> update_subject_grade({'math': 75, 'french': 65, 'gym': 85}, 95, 'english')
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to subject parameter must be a string object
    >>> update_subject_grade(['math', 75, 'french', 65, 'gym', 85], 'math', 95)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to subject_grade parameter must be a dictionary object
    """

    # checking correct types for arguments passed to function parameters
    assert isinstance(subject, str), "argument passed to subject parameter must be a string object"
    assert isinstance(new_grade, int), "argument passed to new_grade parameter must be an integer object"
    assert isinstance(subject_grade, dict), "argument passed to subject_grade parameter must be a dictionary object"

    # checking correct types for keys and values in dictionary, no need for a separate function
    for key, value in subject_grade.items():
        assert isinstance(key, str) and isinstance(value, int), "keys and values must be string and integer types, respectively"

    # checking that argument passed to subject parameter is existing key in dictionary object, otherwise no update
    assert subject in subject_grade.keys(), "argument passed to subject parameter must be an existing dictionary key"

    # argument passed to update method must be a dictionary
    subject_grade.update({subject: new_grade})

    # returning updated grade dictionary, to allow docstring tests
    return subject_grade

doctest.testmod()