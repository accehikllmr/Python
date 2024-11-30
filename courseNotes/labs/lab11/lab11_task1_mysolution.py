from typing import List
from typing import Dict

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

    # initialize outer dictionary object and count, for outer key name
    outer_dictionary = {}
    count = 1

    # iterate through each list in nested list and initialize lists for numbers
    for sublist in nested_list:
        odds = []
        evens = []
        inner_dictionary = {}

    # iterate through sublist to separate odds and evens, placing into new lists
        for num in sublist:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

    # add everything to dictionaries, inner first
        inner_dictionary["list"] = sublist
        inner_dictionary["odd_numbers"] = odds
        inner_dictionary["even_numbers"] = evens
        outer_dictionary[f"list_number_{count}"] = inner_dictionary

    # increment counter for next outer key name
        count += 1

    return outer_dictionary

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)