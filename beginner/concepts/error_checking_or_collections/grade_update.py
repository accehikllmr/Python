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
    # only if no keys and values trigger the previous conditional
    return True

def update_subject_grade(subject_grade: Dict[str, int], subject: str, new_grade: int) -> None:
    """
    Given a subject and an updated grade, the existing grade for that subject is overwritten
    in the dictionary containing this information.

    Parameters:
        subject_grade (Dict[str: int]): dictionary in which subjects (keys)
                                        and their respective grades (values) are stored
        subject (str): name of a subject (key) contained in the dictionary
        new_grade (int): updated grade (value) which will overwrite existing grade
    """
    # checking correct types for arguments passed to function parameters
    assert type(subject) == str, "argument passed to subject parameter must be a string object"
    assert type(new_grade) == int, "argument passed to new_grade parameter must be an integer object"
    assert type(subject_grade) == dict, "argument passed to subject_grade parameter must be a dictionary object"

    # checking correct types for keys and values in dictionary
    assert key_value_types(subject_grade), "keys and values must be string and integer types, respectively"

    # checking that argument passed to subject parameter is existing key in dictionary object
    assert subject in subject_grade.keys(), "argument passed to subject parameter must be an existing dictionary key"

    # updating dictionary according to subject and new_grade arguments, but only if subject is existing key
    subject_grade.update({subject: new_grade})  # without curly brackets around arguments, interprets left side as str

doctest.testmod()