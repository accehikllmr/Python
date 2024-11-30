from typing import List
import doctest

def mean(values: List[int]) -> float:
    """
    Calculate and return the mean of a list

    Parameters:
        values (List[int]): List object containing integer objects

    Returns:
        (float): mean (or average) of the integer objects contained in the list object
    
    >>> mean([2, 3, 4])
    3.0
    >>> mean([1, 2, 3, 4, 5])
    3.0
    >>> mean((2, 3, 4))
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to function parameter must be a list object
    >>> mean([2, 3, '4'])
    Traceback (most recent call last):
    ...
    AssertionError: values in list object must be integer objects
    """
    # checking that argument passed to function parameter is a list object
    assert type(values) == list, "argument passed to function parameter must be a list object"

    # checking that all values in list object are integer objects
    for num in values:
        assert isinstance(num, int), "values in list object must be integer objects"

    # initializing variable to track sum of integer objects
    sum = 0

    # iterating through all integer objects to calculate sum
    for num in values:
        sum += num

    # calculate sum of values, using length of list as denominator
    return sum / len(values)

def pearson_correlation(list_1: List[int], list_2: List[int]) -> float:
    """
    Calculate the Pearson correlation coefficient between two lists.

    Parameters:
        list_1 (list): First list of numerical values.
        list_2 (list): Second list of numerical values.

    Returns:
        (float): Pearson correlation coefficient.
    
    >>> pearson_correlation([2, 4, 6], [1, 3, 5])
    1.0
    >>> pearson_correlation([1, 2, 3], [4, 4, 4])
    Traceback (most recent call last):
    ...
    AssertionError: the denominator is equal to zero, so the coefficient cannot be calculated
    """
    # Calculate the mean of each list
    mean_list_1 = mean(list_1)
    mean_list_2 = mean(list_2)

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

def find_highest_correlation(reference_list: List[int], nested_list: List[List[int]]) -> (List[int], float):
    """
    Find the sublist in the nested list with the highest Pearson correlation with the reference list.

    Parameters:
        reference_list (list): A list of numerical values representing a reference sequence.
        nested_list (list): A nested list where each sublist contains numerical values.

    Returns:
        (tuple): (sublist_with_highest_correlation, correlation_coefficient)
    
    >>> find_highest_correlation([1, 2, 3], [[4, 5, 6], [1, 2, 3], [7, 8, 9]])
    ([4, 5, 6], 1.0)
    >>> find_highest_correlation([1, 3, 6, 7, 8], [[2, 6, 10, 6, -1], [-3, 7, 10, 12, 23],\
    [7, 3, 1, -3, -6]])
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
    for sublist in nested_list:
        # Calculate the Pearson correlation with the reference list
        correlation = pearson_correlation(reference_list, sublist)

        # Update the maximum correlation and sublist if the current correlation is higher
        if correlation > max_correlation:
            max_correlation = correlation
            max_correlation_sublist = sublist

    # Return the sublist with the highest correlation and the corresponding correlation coefficient
    return max_correlation_sublist, round(max_correlation, 4) # please keep the round function

doctest.testmod()