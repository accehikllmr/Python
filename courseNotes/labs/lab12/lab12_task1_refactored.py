import doctest

class Rectangle:

    def __init__(self, length: float, width: float) -> None:
        """
        The constructor of the Rectangle class.

        Parameters:
             length (float): longer side of the rectangle
             width (float): shorter side of the rectangle

        >>> rectangle_1 = Rectangle(4.6, 1.2)
        >>> rectangle_1._length
        4.6
        >>> rectangle_1._width
        1.2
        """

        '''
        checking correct data types for values passed to arguments, but not using type() since this is bad style
        instead using isinstance, which verifies whether the object assigned to a variable is of a certain class
        '''
        assert isinstance(length, float) and length > 0, "length is not a positive float"
        assert isinstance(width, float) and width > 0, "width is not a positive float"

        # adding more attributes, since perimeter and area are calculated using constants and so are constants too
        self._length = length
        self._width = width
        self._perimeter = 2 * (self._width + self._length)
        self._area = self._width * self._length

    def get_length(self) -> float:
        """
        Retrieves the value of the length attribute for a Rectangle object.

        Returns:
            (float): value of the length

        >>> rectangle_1 = Rectangle(4.6, 1.2)
        >>> rectangle_1.get_length()
        4.6
        """

        return self._length

    # this method takes a parameter, since the attribute is being set to a new value, which must be passed
    def set_length(self, length: float) -> float:
        """
        A class method that sets the value of the length.

        Parameters:
            length (float): value to which length will be set

        Returns:
            (float): value of the length

        >>> rectangle_1 = Rectangle(4.6, 1.2)
        >>> rectangle_1.set_length(1.3)
        >>> rectangle_1._length
        1.3
        """

        assert isinstance(length, float) and length > 0, "length is not a positive float"

        # no return here, since simply updating value of attribute for object instance
        self._length = length

    def get_width(self) -> float:
        """
        Retrieves the value of the width attribute for a Rectangle object.

        Returns:
            (float): value of the width

        >>> rectangle_1 = Rectangle(4.6, 1.2)
        >>> rectangle_1.get_width()
        1.2
        """

        return self._width

    def set_width(self, width: float) -> float:
        """
        A class method that sets the value of the width.

        Parameters:
            width (float): value to which width will be set

        Returns:
            (float): value of the width

        >>> rectangle_1 = Rectangle(4.6, 1.2)
        >>> rectangle_1.set_width(4.7)
        >>> rectangle_1._width
        4.7
        """

        assert isinstance(width, float) and width > 0, "width is not a positive float"

        self._width = width

    def get_perimeter(self) -> float:
        """
        Retrieves the value of the perimeter attribute for a Rectangle object.

        Returns:
            (float): perimeter of the Rectangle object

        >>> rectangle_1 = Rectangle(4.6, 1.2)
        >>> rectangle_1.get_perimeter()
        11.6
        """

        return self._perimeter

    def get_area(self) -> float:
        """
        Retrieves the value of the area attribute for a Rectangle object.

        Returns:
            (float): area of the Rectangle object

        >>> rectangle_1 = Rectangle(4.6, 1.2)
        >>> rectangle_1.get_area()
        5.52
        """

        return self._area

doctest.testmod()