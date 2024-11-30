import doctest
from typing import List
from typing import Dict

def is_odd(num: int) -> bool:
    """
    Check if a number is odd.

    Parameters:
         num (int): The number to be checked.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return num % 2 != 0

def separate_numbers(nested_list: List[List[int]]) -> Dict[str, Dict[str, List[int]]]:
    """
    Takes a nested list, separates odd and even numbers within each inner list,
    and organizes the results in a dictionary-style format.

    Parameters:
        nested_list (List[List[int]]): A nested list containing inner lists of numerical values.

    Test Cases: # unable to figure out how to wrap docstring test answer to next line
    >>> separate_numbers([[1, 2, 3, 4, 5], [1, 2, 34, 5]])
    {'list_number_1': {'list': [1, 2, 3, 4, 5], 'odd_numbers': [1, 3, 5], 'even_numbers': [2, 4]}, 'list_number_2': {'list': [1, 2, 34, 5], 'odd_numbers': [1, 5], 'even_numbers': [2, 34]}}
    """
    # Step 3: Check pre-conditions
    for inner_list in nested_list:
        for num in inner_list:
            assert isinstance(num, int) and num >= 0, "All elements must be non-negative integers."

    # Step 4: Create empty dictionary for results
    result_dict = {}

    # Step 5: Iterate through the nested list
    for i in range(len(nested_list)):
        inner_list = nested_list[i]

    # Step 6: Create empty lists for odd and even numbers
        odds_list = []
        even_list = []

    # Step 8: Iterate throughout the inner lists and append to the appropriate list:
        for num in inner_list:
            if is_odd(num):
                odds_list.append(num)
            else:
                even_list.append(num)

    # Step 9: Organize results in a dictionary for each inner list
        list_dict = {
            "list": inner_list,
            "odd_numbers": odds_list,
            "even_numbers": even_list
        }

    # Step 10: Add the dictionary to the main result dictionary
        result_dict[f"list_number_{i + 1}"] = list_dict

    return result_dict

doctest.testmod()

# this code has a style issue, which I've not been able to find