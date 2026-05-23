"""
Abstraction Example
-------------------
The process of hiding the internal implementation and showing the
necessary data to the end user is called as Abstraction.



"""

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract class Shape
    ---------------------
    Represents a generic geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass


class Rectangle(Shape):
    """
    Rectangle class
    ----------------
    Inherits from Shape and implements the abstract methods.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """
    Circle class
    -------------
    Inherits from Shape and implements the abstract methods.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


# Instantiate objects of concrete classes
rectangle = Rectangle(4, 5)
circle = Circle(3)

# Call the area and perimeter methods
print("Rectangle:")
print("Area:", rectangle.area())       # Output: Area: 20
print("Perimeter:", rectangle.perimeter())  # Output: Perimeter: 18

print("\nCircle:")
print("Area:", circle.area())           # Output: Area: 28.27331
print("Perimeter:", circle.perimeter())     # Output: Perimeter: 18.84954
