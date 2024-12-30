import doctest
from typing import List

# not returning list of strings, since could have an empty list
def intersecting_chars(my_str: str) -> List[str]:
    """
    Given a string of letters from the alphabet, with three distinct substrings separated by underscores,
    returns a list containing each individual letter found in all three substrings.

    Parameters:
        my_str (str): strings of letters from the alphabet with two underscores separating three distinct substrings

    Returns:
        (List[str]): individual letters contained in all three distinct substrings

    >>> intersecting_chars("__")
    []
    >>> intersecting_chars("bob_sue_")
    []
    >>> intersecting_chars("ab_aaab_bCC")
    ['b']
    >>> intersecting_chars("aBcd_aaab_bCC")
    ['b']
    >>> intersecting_chars("Bdk_YB_MWB")
    ['b']
    >>> intersecting_chars("m_CCda_acz")
    []
    >>> intersecting_chars("CAB_cab_cxaxb")
    ['a', 'b', 'c']
    >>> intersecting_chars("Ab_bC_abBC")
    ['b']
    >>> intersecting_chars("Ab_dC_abBC")
    []
    >>> intersecting_chars("za3g34_0a_a")
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to my_str parameter must only have underscores and letters from the alphabet
    >>> intersecting_chars("abcde_FGHagc")
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to my_str parameter must have exactly two underscore characters
    >>> intersecting_chars(2)
    Traceback (most recent call last):
    ...
    AssertionError: argument passed to my_str parameter must be a string object
    """

    assert isinstance(my_str, str), "argument passed to my_str parameter must be a string object"

    # checking that the argument passed to my_str parameter has exactly two underscore characters
    assert my_str.count('_') == 2, "argument passed to my_str parameter must have exactly two underscore characters"

    # checking that all characters in string are letters from the alphabet, challenges than the underscores, or that is only contains underscores (i.e. no substrings)
    assert my_str.replace('_', "").isalpha() or my_str == "__", "argument passed to my_str parameter must only have underscores and letters from the alphabet"

    # converting string characters to lowercase, splitting it using underscore as delimiter, and placing it into a list (character case irrelevant for intersection)
    strings = my_str.lower().split("_")

    # empty strings automatically return an empty list (no characters in common with empty string)
    if "" in strings:
        return []
    else:
        '''
        rather than assigning different sets to variables, to simplify code, doing everything in one line
        however, trying to write single line into many lines, in order to improve readability
        unsure if proper styling has been achieved, trying to separate parentheses like blocks in C
        '''
        return (
            sorted (
                list (
                    set (
                        strings[0]
                    ).intersection (
                            set (
                                strings[1]
                            ).intersection (
                                    set(
                                        strings[2]
                                    )
                            )
                    )
                )
            )
        )

doctest.testmod()