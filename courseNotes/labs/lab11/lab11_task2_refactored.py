from typing import List, Tuple
import doctest

def pearson_correlation(list_1: List[int], list_2: List[int]) -> float:
    """
    Calculate the Pearson correlation coefficient between two lists.

    Parameters:
        list_1 (List[num]): First list of numerical values.
        list_2 (List[num]): Second list of numerical values.

    Returns:
        (float): Pearson correlation coefficient.

    >>> pearson_correlation([2, 4, 6], [1, 3, 5])
    1.0
    >>> pearson_correlation([2, 4, 6], [])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to list_2 parameter must be a non-empty list object
    >>> pearson_correlation([], [1, 3, 5])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to list_1 parameter must be a non-empty list object
    >>> pearson_correlation((2, 4, 6), [1, 3, 5])
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to list_1 parameter must be a non-empty list object
    >>> pearson_correlation([2, 4, 6], (1, 3, 5))
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to list_2 parameter must be a non-empty list object
    >>> pearson_correlation([2, 4, 6], [1, 3.0, 5])
    Traceback (most recent call last):
    ...
    AssertionError: all elements in list objects must be integer objects
    >>> pearson_correlation([1, 2, 3], [4, 4, 4])
    Traceback (most recent call last):
    ...
    AssertionError: the denominator is equal to zero, so the coefficient cannot be calculated
    """

    # validating arguments, since not done in other function
    assert isinstance(list_1, list) and len(list_1) != 0, "argument passed to list_1 parameter must be a non-empty list object"
    assert isinstance(list_2, list) and len(list_2) != 0, "argument passed to list_2 parameter must be a non-empty list object"

    # rather than iterating through two separate lists, iterate through a single one
    check_list = list_1 + list_2

    for element in check_list:
        assert isinstance(element, int), "all elements in list objects must be integer objects"

    # Calculate the mean of each list, no need for a function, since calculation is trivial
    mean_list_1 = sum(list_1) / len(list_1)
    mean_list_2 = sum(list_2) / len(list_2)

    # Calculate the numerator and denominator of the Pearson correlation formula
    numerator = 0
    for i in range(len(list_1)):
        numerator += (list_1[i] - mean_list_1) * (list_2[i] - mean_list_2)

    # separate loops, since two summations in the denominator, rather than one
    denominator_sum_list_1 = 0
    for x in list_1:
        denominator_sum_list_1 += (x - mean_list_1) ** 2

    denominator_sum_list_2 = 0
    for y in list_2:
        denominator_sum_list_2 += (y - mean_list_2) ** 2

    denominator = (denominator_sum_list_1 * denominator_sum_list_2) ** 0.5

    # Calculate the correlation coefficient and handle division by zero
    assert denominator != 0, "the denominator is equal to zero, so the coefficient cannot be calculated"
    correlation_coefficient = numerator / denominator

    return correlation_coefficient

def find_highest_correlation(reference_list: List[int], nested_list: List[List[int]]) -> Tuple[List[int], float]:
    """
    Find the sublist in the nested list with the highest Pearson correlation with the reference list.

    Parameters:
        reference_list (List[int]): A list of numerical values representing a reference sequence.
        nested_list (List[List[int]]): A nested list where each sublist contains numerical values.

    Returns:
        (Tuple[List[int], float]): (sublist_with_highest_correlation, correlation_coefficient)

    >>> find_highest_correlation([1, 2, 3], [[4, 5, 6], [1, 2, 3], [7, 8, 9]])
    ([4, 5, 6], 1.0)
    >>> find_highest_correlation([1, 3, 6, 7, 8], [[2, 6, 10, 6, -1], [-3, 7, 10, 12, 23], [7, 3, 1, -3, -6]])
    ([-3, 7, 10, 12, 23], 0.9248)
    >>> find_highest_correlation([1, 2, 3], [[4, 5], [1, 2, 3], [7, 8, 9]])
    Traceback (most recent call last):
    ...
    AssertionError: all sublists in nested list must be equal in length to reference list
    """

    # check matching lengths of reference list and sublists in nested list
    for sublist in nested_list:
        assert len(sublist) == len(reference_list), "all sublists in nested list must be equal in length to reference list"

    # Initialize variables to store the current maximum correlation and corresponding sublist
    max_correlation = 0
    max_correlation_sublist = None

    # Iterate through each sublist in the nested list
    for this_sublist in nested_list:
        # Calculate the Pearson correlation with the reference list
        this_correlation = pearson_correlation(reference_list, this_sublist)

        # Update the maximum correlation and sublist if the current correlation is higher
        if this_correlation > max_correlation:
            max_correlation = this_correlation
            max_correlation_sublist = this_sublist

    # Return the sublist with the highest correlation and the corresponding correlation coefficient
    return max_correlation_sublist, round(max_correlation, 4)

doctest.testmod()