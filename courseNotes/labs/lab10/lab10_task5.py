import doctest
from typing import Dict

def invert_dict(a_dict: Dict[str, int]) -> Dict[str, int]:
    """
    Inverts a dictionary, making its keys become values and its values become keys, while
    preserving the key-value pairings.

    Parameters:
        a_dict (List[str, int]):    dictionary object with string object keys and integer object values

    Returns:
        (List[str, int]):   dictionary object with integer object keys and string object values, same key-value pairs
                            as the original dictionary


    """
    

doctest.testmod()