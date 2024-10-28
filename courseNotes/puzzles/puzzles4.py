#QUESTION 1

name = "Bob"
lab1_grade = 67
lab2_grade = 86
midterm = 92
final = 63

#using concatenation
print("Student name: " + name + "\n- Lab grade:\n\t\tlab1_grade: " + str(lab1_grade)
      + "\n\t\tlab2_grade: " + str(lab2_grade) + "\n- midterm: " + str(midterm) + "\n- final: " + str(final))

#using %
print("\nStudent name: %s\n- Lab grade:\n\t\tlab1_grade: %d\n\t\tlab2_grade: %d"
      "\n- midterm: %d\n- final: %d" % (name, lab1_grade, lab2_grade, midterm, final))

#using the method format
print("\nStudent name: {}\n- Lab grade:\n\t\tlab1_grade: {}\n\t\tlab2_grade: {}"
      "\n- midterm: {}\n- final: {}".format(name, lab1_grade, lab2_grade, midterm, final))

#using f string
print(f"\nStudent name: {name}\n- Lab grade:\n\t\tlab1_grade: {lab1_grade}\n\t\tlab2_grade: {lab2_grade}"
      f"\n- midterm: {midterm}\n- final: {final}")

#QUESTION 2

def perimeter(length, width):
    """return the perimeter of a rectangle given length and width"""
    return (length + width) * 2

def area(length, width):
    """return the area of a rectangle given length and width"""
    return length * width

def geometric(length, width):
    """return the perimeter and area of a rectangle given length and width"""
    shape_perimeter = perimeter(length, width)
    shape_area = area(length, width)

    return shape_perimeter, shape_area

#shape_length = 4
#shape_width = 3
#geometric(shape_length, shape_width)

# max(area(3.3, 4.2), area(4.5, 3.1))
'''
the following order of execution is based on the lines numbers in the python file, where 
the first line of code for this program is line 27 and the function call is at line 46

- line 27 (creation of a function object)
- line 31 (creation of a function object)
- line 35 (creation of a function object)
- ignoring lines 42, 43, 44 (omitted from the puzzle question)
- line 46 (max function call, first area function call)
- line 33 (return value of first area function call)
- line 46 (second area function call)
- line 33 (return value of second area function call)
- line 46 (return value of max function call)
'''

#QUESTION 3

def average_rating(rating_1: int, rating_2: int, rating_3: int) -> float:
    """
    return the average rating given the ratings are 1 to 5.

    Precondition:   rating_1: int
                    rating_2: int
                    rating_3: int
    """

    #the precondition of the above function is that all arguments passed to it are integers

#QUESTION 4

def is_palindrome(s: str = "") -> bool:
    """ return True if and only if s is a palindrome (e.g., symmetric).
    For example, noon is palindrome, but hello is not.

    Precondition: s: str

    >>> is_palindrome("noon")       #'noon' is equal to 'noon'
    True
    >>> is_palindrome("Noon")       #does not consider visual symmetry, only alphabetic
    True
    >>> is_palindrome("hello")      #'hello' is not equal to 'olleh'
    False
    >>> is_palindrome("a")          #singleton 'a' is equal to singleton 'a'
    True
    >>> is_palindrome("race car")   #can identify palindrome phrases, spaces replaced with empty string
    True
    >>> is_palindrome("")           #zero case: '' does not have a length greater than zero
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument: s must have a length greater than zero
    >>> is_palindrome("n00n")
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument: s must only have Latin-script alphabetic characters
    >>> is_palindrome("he!!o")
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument: s must only have Latin-script alphabetic characters
    """

    #to allow spaces between characters without triggering an assertion error
    s = s.replace(" ", "")

    assert len(s) != 0, "invalid argument: s must have a length greater than zero"
    assert type(s) == str, "invalid argument: s does not have the correct type."
    assert s.isalpha() == True, "invalid argument: s must only have Latin-script alphabetic characters"

    #using casefold to disregard case of characters in argument
    s = s.casefold()

    return s == s[::-1]

print(is_palindrome(input()))

if __name__ == "__main__":
    import doctest
    doctest.testmod()