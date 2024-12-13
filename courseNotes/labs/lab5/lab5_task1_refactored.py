import doctest
from math import pi

class Circle:
    """ A class representing circles """

    def __init__(self, radius: float) -> None:
        """
        Instantiates an object belonging to the circle class.

        Parameters:
            radius (float): distance from the centre of the circle to its edge

        >>> circle_1 = Circle(1.0)
        >>> circle_1.get_radius()
        1.0
        """

        # checking that radius is float object
        assert isinstance(radius, float) and radius > 0, "argument passed to radius parameter must be a positive integer"

        # could create attributes for diameter, area and circumference, not sure if better to have as method...
        self._radius = radius

    def __str__(self) -> str:
        """
        Outputs string representation of the circle object.

        Returns:
             (str): string representation of the circle object

        >>> circle_1 = Circle(1.0)
        >>> circle_1.__str__()
        'Circle(1.0)'
        >>> print(circle_1)
        Circle(1.0)
        """

        return f"Circle({self._radius})"

    def get_radius(self) -> float:
        """
        Retrieves radius attribute from a circle object.

        Returns:
            (float): radius of circle

        >>> circle_1 = Circle(1.0)
        >>> circle_1.get_radius()
        1.0
        """

        return self._radius

    def set_radius(self, new_radius: float) -> None:
        """
        Updates radius attribute for a circle object.

        Parameters:
            new_radius (float): value assigned to radius attribute of circle object

        >>> circle_1 = Circle(1.0)
        >>> circle_1.set_radius(2.0)
        >>> circle_1.get_radius()
        2.0
        >>> circle_1.set_radius(-2.0)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to new_radius parameter must be a positive float
        >>> circle_1.set_radius(2)
        Traceback (most recent call last):
        ...
        AssertionError: argument passed to new_radius parameter must be a positive float
        """

        # checking validity of new_radius argument
        assert isinstance(new_radius, float) and new_radius > 0, "argument passed to new_radius parameter must be a positive float"

        self._radius = new_radius

    def calculate_diameter(self) -> float:
        """
        Calculates the diameter of a circle object.

        Returns:
            (float): diameter of a circle object

        >>> circle_1 = Circle(1.0)
        >>> circle_1.calculate_diameter()
        2.0
        """

        return self._radius * 2

    def calculate_area(self) -> float:
        """
        Calculates the area of a circle object to two digits after the decimal point.

        Returns:
            (float): area of a circle object to two digits after the decimal point

        >>> circle_1 = Circle(1.0)
        >>> circle_1.calculate_area()
        3.14
        """

        return round(pi * self._radius ** 2, 2)

    def calculate_circumference(self) -> float:
        """
        Calculates the circumference of a circle object to two digits after the decimal point.

        Returns:
            (float): circumference of the circle object to two digits after the decimal point

        >>> circle_1 = Circle(1.0)
        >>> circle_1.calculate_circumference()
        6.28
        """

        return round(2 * pi * self._radius, 2)

doctest.testmod()