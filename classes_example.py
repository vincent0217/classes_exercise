# Classes example

# Create some classes and objects

import math


class Shape:
    """Represents a 2-dimensional polygon

    Attributes:
        num_sides: An integer count of the sides
        side_length: A float of side length
    """

    def __init__(self):
        """Creates a new shape with default values."""
        self.num_sides = 4
        self.side_length = 10.0

    def area(self) -> float:
        """Return the area of a square."""
        return self.side_length ** 2

    def perimeter(self) -> float:
        """Return the perimeter of a square"""
        return self.side_length * self.num_sides


class Circle(Shape):
    """Represents a circle which IS a shape.

    Attributes:
        radius: A float indicating the radius
    """

    def __init__(self, radius: float = 5):
        """Creates a circle with default radius of 5."""
        # Call the superclass constructor
        super().__init__()
        self.radius = radius

    def area(self) -> float:
        """returns the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """Returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


some_shape = Shape()
print(some_shape.num_sides)
print(some_shape.area())
print(some_shape.perimeter())

some_circle = Circle(10)
print(some_circle.area())
print(some_circle.perimeter())
