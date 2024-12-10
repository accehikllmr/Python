import doctest
from math import ceil as ceiling
from typing import Dict

# don't need to pass global variables as arguments, but doing so allows testing
def calculate_average(gradebook: Dict[str, int], weightbook: Dict[str, float]) -> float:
    """
    Calculate the average grade given a list of grades and weights for each task.

    Parameters:
        gradebook (Dict[str, int]): dictionary with tasks paired to their respective grades
        weightbook (Dict[str, float]): dictionary with tasks paired to their respective weights

    Returns:
        (float) : average grade of tasks, with weights accounted for

    >>> calculate_average({'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}, {'a': 0.05, 'b': 0.05, 'c': 0.2, 'd': 0.25, 'e': 0.5})
    0
    >>> calculate_average({'a': 100, 'b': 100, 'c': 100, 'd': 100, 'e': 100}, {'a': 0.05, 'b': 0.05, 'c': 0.2, 'd': 0.25, 'e': 0.5})
    100
    >>> calculate_average({'a': 90, 'b': 70, 'c': 80, 'd': 60, 'e': 66}, {'a': 0.05, 'b': 0.05, 'c': 0.2, 'd': 0.25, 'e': 0.5})
    69
    >>> calculate_average({'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': -1}, {'a': 0.05, 'b': 0.05, 'c': 0.2, 'd': 0.25, 'e': 0.5})
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to gradebook parameter must have non-negative integer values
    """

    # checking preconditions, no need to check strings since already hardcoded in dictionary, also not checking weightbook since hardcoded
    for value in gradebook.values():
        assert isinstance(value, int) and value >= 0, "argument passed to gradebook parameter must have non-negative integer values"

    # using list comprehension on grades dictionary values in order to extract task names
    grade_list = [i for i in gradebook.values()]

    # using list comprehension on weights dictionary values in order to extract task weights
    weight_list = [j for j in weightbook.values()]

    # calculating average, using ceiling for benefit of the student
    return ceiling(max(grade_list[0], grade_list[1]) * weight_list[0] + grade_list[2] * weight_list[2]\
                 + grade_list[3] * weight_list[3] + grade_list[4] * weight_list[4])

# instantiating dictionary object so that corresponding grades can be inserted into it
grades = {'lab1_grade': 0, 'lab2_grade': 0, 'assignment_grade': 0, 'midterm_grade': 0, 'final_grade': 0}

# instantiating dictionary object for the tasks and respective weights
weights = {'lab1_grade': 0.05, 'lab2_grade': 0.05, 'assignment_grade': 0.2, 'midterm_grade': 0.25, 'final_grade': 0.5}

# iterate through dictionary keys in order to update their values
for task in grades.keys():
    # taking user input according to specific assignment
    grades[task] = int(input(f"{task} score: "))

#output the course score to the user, added sentence to explain output
print(f"Your score for the entire course is {calculate_average(grades, weights)}%.")

doctest.testmod()