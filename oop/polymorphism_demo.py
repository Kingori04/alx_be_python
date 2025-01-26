import math

class Shape:
    def area(self):
        """
        Placeholder method to calculate the area of a shape.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initializes a Rectangle instance.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """
        Initializes a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * (self.radius ** 2)

