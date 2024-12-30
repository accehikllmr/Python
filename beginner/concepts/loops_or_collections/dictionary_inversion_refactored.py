import doctest
from typing import Dict
from typing import List

def invert_dict(a_dict: Dict[str, int]) -> Dict[int, List[str]]:
    """
    Inverts a dictionary, making its keys become values and its values become keys, while preserving the key-value pairings.

    Parameters:
        a_dict (List[str, int]): dictionary object with string object keys and integer object values

    Returns:
        (List[str, int]): dictionary object with integer object keys and string object values, same key-value pairs as the original dictionary

    >>> invert_dict({"Pikachu": 99, "Snorlex": 30})
    {99: ['Pikachu'], 30: ['Snorlex']}
    >>> invert_dict({})
    {}
    >>> invert_dict({"Pikachu": 99, "Snorlex": 30, "Bulbasaur": 30})
    {99: ['Pikachu'], 30: ['Snorlex', 'Bulbasaur']}
    >>> invert_dict({"Charizard": 360, "Pikachu": 99, "Snorlex": 30, "Bulbasaur": 30, "Kyogre": 360})
    {360: ['Charizard', 'Kyogre'], 99: ['Pikachu'], 30: ['Snorlex', 'Bulbasaur']}
    >>> invert_dict({99: "Pikachu", 30: "Snorlex", 30: "Bulbasaur"})
    Traceback (most recent call last):
    ...
    AssertionError: keys and values must be string and integer objects, respectively
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
    assert isinstance(a_dict, dict), "argument passed to parameter must be a dictionary object"

    # instantiating dictionary object to store inverted key-value pairings
    inverted_dict = {}

    # iterating through values, since keys will be collected according to their shared values
    for value in a_dict.values():
        assert isinstance(value, int), "keys and values must be string and integer objects, respectively"
        # instantiating list to store keys that have same values, in original dictionary
        inverted_value = []
        # iterating through all keys and adding to above list if they share the same value pairing
        for key in a_dict.keys():
            assert isinstance(key, str), "keys and values must be string and integer objects, respectively"
            if a_dict[key] == value:
                inverted_value.append(key)

        # building inverted dictionary
        inverted_dict[value] = inverted_value

    return inverted_dict

doctest.testmod()