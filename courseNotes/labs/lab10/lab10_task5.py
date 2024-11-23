import doctest
from typing import Dict
from typing import List

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

def invert_dict(a_dict: Dict[str, int]) -> Dict[int, List[str]]:
    """
    Inverts a dictionary, making its keys become values and its values become keys, while
    preserving the key-value pairings.

    Parameters:
        a_dict (List[str, int]):    dictionary object with string object keys and integer object values

    Returns:
        (List[str, int]):   dictionary object with integer object keys and string object values, same key-value pairs
                            as the original dictionary

    >>> invert_dict({"Pikachu": 99, "Snorlex": 30})
    {99: ['Pikachu'], 30: ['Snorlex']}
    >>> invert_dict({})
    {}
    >>> invert_dict({"Pikachu": 99, "Snorlex": 30, "Bulbasaur": 30})
    {99: ['Pikachu'], 30: ['Snorlex', 'Bulbasaur']}
    >>> invert_dict({"Charizard": 360, "Pikachu": 99, "Snorlex": 30, "Bulbasaur": 30, "Kyogre": 360})
    {360: ['Charizard', 'Kyogre'], 99: ['Pikachu'], 30: ['Snorlex', 'Bulbasaur']}
    >>> invert_dict([20, 30])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to parameter must be a dictionary object
    >>> invert_dict({99: "Pikachu", 30: ["Snorlex", "Bulbasaur"]})
    Traceback (most recent call last):
    ...
    AssertionError: keys and values must be string and integer objects, respectively
    """
    # checking that argument passed to parameter is a dictionary
    assert type(a_dict) == dict, "argument passed to parameter must be a dictionary object"

    # checking correct types for keys and values in dictionary
    assert key_value_types(a_dict), "keys and values must be string and integer objects, respectively"

    # initializing empty list, to store inverted dictionary keys, extracted from original dictionary
    key_set = set()

    for value in a_dict.values():
        # values from original dictionary will be used for inverted dictionary keys
        key_set.add(value)

    # no matter what conversions used, set is always 'sorted' in decreasing order, cannot determine why

    # initializing empty dictionary, to store inverted key-value pairings
    inverted_dict = {}

    for key in key_set:
        # initializing empty list, to store values paired with identical keys, for inverted dictionary
        new_value = []
        for item in a_dict.items():
            # finding any key-value pairing from original dictionary with shared values
            if key == item[1]:
                # creating list object, to store inverted dictionary values with shared key
                new_value.append(item[0])
        inverted_dict[key] = new_value

    return inverted_dict

doctest.testmod()